from binance_api import Binance
from datetime import datetime
import json
import time

with open('API.txt')as apikeys:
    API = apikeys.read().split()

bot = Binance(API_KEY=API[0], API_SECRET=API[1])

STARTTIME = 1514754000000  # Begin from 01.01.2018 in ms
INTERVAL = 1000 * 60 * 60 * 24  # 1 day in ms
ENDTIME = datetime.now().timestamp() * 1000  # Current date in ms
cls = 4  # Closed price index from response
tcls = 6  # Closed candle index from response
TIMEFRAME = '1h'  # time frame 1 hour
TRADE_PAIR = 'BTCUSDT'  # trade pair BTC/USDT


def get_history(pair, tf, start, end, interval=86400000, cd=100):
    """
    Getting the history of the chart from Binance
    :param pair: cryptocurrency pair, a story have to get
    :param tf: time frame
    :param start: date in ms, starting point
    :param end: date in ms, end point
    :param interval: step in ms, max step 90 days, default=1 day
    :param cd: cooldown, if we don't want to get banned
    :return: dictionary with historical data, {date+time: price}
    """
    history = {}
    cooldown = 0
    while start < end:
        DATA = bot.klines(symbol=pair, interval=tf, startTime=start, endTime=start + interval)

        for day in DATA:
            history[str(datetime.fromtimestamp((day[tcls] + 1) / 1000))] = round(float(day[cls]), 2)
        start += interval
        cooldown += 1

        if cooldown >= cd:
            time.sleep(5)
            cooldown = 0
    return history


history = get_history(TRADE_PAIR, TIMEFRAME, STARTTIME, ENDTIME)

with open('history.json', 'w')as file:  # save history in json file
    json.dump(history, file)
