import json
import csv


def macd_strategy(data: dict):
    """
    Calculates and stores data on moving averages and MACD strategies.
    Searches for entry points to a position according to the conditions of the strategy
    :param data: dictionary with data
    :return: deals in matrix type [[open deal, price, close deal, price]]
    """
    ema30, ema100 = 0, 0
    a30 = (2 / (1 + 30))
    a100 = (2 / (1 + 100))

    trades = [['open trade', 'price', 'close trade', 'price']]
    history_stat = [['datetime', 'price', 'ema30', 'ema100']]
    trade = False
    temp = []

    for date, price in data.items():
        if history_stat[-1][0] == 'datetime':
            history_stat.append([date, price, price, price])  # initial row
        else:
            ema30 = (price * a30) + (float(history_stat[-1][2]) * (1 - a30))
            ema100 = (price * a100) + (float(history_stat[-1][3]) * (1 - a100))

            history_stat.append([date, price, round(ema30, 3), round(ema100, 3)])

        if not trade and ema30 > ema100:
            temp.append(date)
            temp.append(price)
            trade = True

        if trade and ema30 < ema100:
            temp.append(date)
            temp.append(price)
            trade = False
            trades.append(temp)
            temp = []
    return trades


with open('history.json')as file:  # loading history
    DATA = json.load(file)  # save history, format {datetime: price}

TRADES = macd_strategy(DATA)  # save in variables

with open('ma_strategy.csv', 'a') as file:  # save in CSV file
    writer = csv.writer(file)
    for row in TRADES:
        writer.writerow(row)
