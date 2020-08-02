# # Script to read records from a csv file and submit GET requests to the kdb+ API

# import pandas as pd
# import requests as req

# INPUT_FILE_PATH = './high_freq_201906.csv'
# TABLE_NAME = 'trades'

# def create_query(tabname, row):
#     "Create a query to insert the row data into table tab"
#     date, hour, minute, ticker, op, hp, lp, cp, volume, amount = row
#     date = str(date)
#     date = "{}.{}.{}".format(date[0:4], date[4:6], date[6:])
#     hour = str(hour)
#     if len(hour) == 1:
#         hour = "0" + hour
#     timespan = "{}:{}:00.000000000".format(hour, minute)
#     volume = int(volume)
#     query = "`{} insert ({} ; {} ; `{} ; {} ; {} ; {} ; {} ; {} ; {})".format(
#         tabname, date, timespan, ticker, op, cp, hp, lp, volume, amount)
#     return query

# if __name__ == '__main__':
#     protocol = "http"
#     host = 'localhost'
#     port = 5000
#     get_url_formatter = "{}://{}:{}/?{}"
#     data = pd.read_csv(INPUT_FILE_PATH)
#     for _, row in data.iterrows():
#         query = create_query(TABLE_NAME, row)
#         url = get_url_formatter.format(protocol, host, port, query)
#         success = False
#         while not success:
#             res = req.get(url)
#             status = 'Success' if res.status_code == 200 else 'Failure'
#             print('[{}] {}'.format(status, url))

# Script to read records from a csv file and submit GET requests to the kdb+ API

import pandas as pd
import requests as req
import random as rd
import datetime as dt

def create_query(tabname):
    "Create a query to insert the synthetic data into table tab"
    date = dt.datetime.now().strftime("%Y.%m.%d")
    timespan = dt.datetime.now().strftime("%H:%M:%S.0000000")
    ticker = f"{rd.randint(0, 999999):06}.{['SZ', 'SH', 'HK'][rd.randint(0, 2)]}"
    middle = 5 * (1 + 199 * rd.random())
    interval = 0.1 * middle
    lowerbound = middle - interval
    upperbound = middle + interval
    prices = sorted([rd.random() * (upperbound - lowerbound) + lowerbound for i in range(4)])
    lp, hp = prices[0], prices[-1]
    op_idx = rd.randint(1, 2)
    cp_idx = 3 - op_idx
    op, cp = prices[op_idx], prices[cp_idx]
    avg_price = sum(prices) / len(prices)
    volume = rd.randint(10000, 10000000)
    amount = avg_price * volume
    query = "`{} insert ({} ; {} ; `{} ; {:.2f} ; {:.2f} ; {:.2f} ; {:.2f} ; {} ; {})".format(
        tabname, date, timespan, ticker, op, cp, hp, lp, volume, amount)
    return query

if __name__ == '__main__':
    protocol = "http"
    host = 'localhost'
    port = 5000
    get_url_formatter = "{}://{}:{}/?{}"
    table_name = 'trades'

    num_records = 0

    while num_records < 10000:
        if rd.randint(0, 1) == 0:
            continue
        query = create_query(table_name)
        url = get_url_formatter.format(protocol, host, port, query)
        success = False
        attempt = 0
        while not success and attempt < 5:
            res = req.get(url)
            if res.status_code == 200:
                status = 'Success'
                num_records += 1
                success = True
            else:
                status = 'Failure'
            print('[{}] {}'.format(status, url))
            attempt += 1