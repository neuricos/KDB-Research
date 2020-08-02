import argparse
import random

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-c", "--randcols", help="Number of columns with random data", type=int)
    parser.add_argument("-r", "--rowcnt", help="Number of fake records", type=int)
    parser.add_argument("-f", "--file", help="Name of output file", type=str)
    args = parser.parse_args()

    with open(args.file, 'w') as f:
        # Write the column names
        f.write("date,hour,minute,ticker,op,hp,lp,cp,volume,amount")
        for col in range(0, args.randcols):
            f.write(",random{}".format(col))
        f.write("\n")

        # Write the data
        for _ in range(args.rowcnt):
            # Randomly if the transaction happens in the morning or afternoon
            morning = random.randint(0, 1)
            if morning == 0:  # Afternoon, time period = [13:01, 15:00]
                hour = random.randint(13, 15)
                if hour == 13:
                    minute = random.randint(1, 59)
                elif hour == 14:
                    minute = random.randint(0, 59)
                else:
                    minute = 0
            else:  # Morning, time period = [9:31, 11:30]
                hour = random.randint(9, 11)
                if hour == 9:
                    minute = random.randint(31, 59)
                elif hour == 10:
                    minute = random.randint(0, 59)
                else:
                    minute = random.randint(0, 30)
            
            # ticker is a 6-digit code
            # from Shenzheng (SZ), Shanghai (SH), Hong Kong(HK)
            ticker_number = random.randint(0, 999999)
            ticker_index = random.randint(0, 2)
            ticker = "{:06d}.{}".format(ticker_number, ["SZ", "SH", "HK"][ticker_index])

            # Let lowest price and highest price be within [10, 90]
            prices = [random.uniform(10, 90) for _ in range(2)]
            hp = max(prices)
            lp = min(prices)
            op = random.uniform(lp, hp)
            cp = random.uniform(lp, hp)
            volume = random.randint(1000000, 10000000)
            amount = volume * random.uniform(lp, hp)

            # Write the values into the csv file
            f.write("20190603,{},{},{},{},{},{},{},{},{}".format(hour, minute, ticker, op, hp, lp, cp, volume, amount))
            # Randomly generate floats
            for _ in range(args.randcols):
                value = random.randint(10000, 1000000)
                f.write(",{}".format(value))
            f.write("\n")
    f.close()
    print("Done.")