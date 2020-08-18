import json
import csv


def macd_strategy(data: dict):
    """
    Calculates and stores data on moving averages and MACD strategies.
    Searches for entry points to a position according to the conditions of the strategy
    :param data: dictionary with data
    :return: deals in matrix type [[open deal, price, close deal, price]]
    """
    ema12, ema26, macd, smacd = 0, 0, 0, 0
    a12 = (2 / (1 + 12))
    a26 = (2 / (1 + 26))
    asgnl = (2 / (1 + 9))
    trades = [['open trade', 'price', 'close trade', 'price']]
    history_stat = [['datetime', 'price', 'ema12', 'ema26', 'macd', 'smacd']]
    trade = False
    temp = []

    for date, price in data.items():
        if history_stat[-1][0] == 'datetime':
            history_stat.append([date, price, price, price, 0, 0])  # initial row
        else:
            ema12 = (price * a12) + (float(history_stat[-1][2]) * (1 - a12))
            ema26 = (price * a26) + (float(history_stat[-1][3]) * (1 - a26))
            macd = ema12 - ema26
            smacd = (macd * asgnl) + float(history_stat[-1][-1]) * (1 - asgnl)
            history_stat.append([date, price, round(ema12, 3), round(ema26, 3), round(macd, 3), round(smacd, 3)])

        if not trade and smacd > macd and smacd > 0:
            temp.append(date)
            temp.append(price)
            trade = True
        if trade and smacd < macd and smacd < 0:
            temp.append(date)
            temp.append(price)
            trade = False
            trades.append(temp)
            temp = []
    return trades


with open('history.json')as file:  # loading history
    DATA = json.load(file)  # save history, format {datetime: price}

TRADES = macd_strategy(DATA)  # save in variables

with open('result.csv', 'a') as file:  # save in CSV file
    writer = csv.writer(file)
    for row in TRADES:
        writer.writerow(row)
