import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-c", "--randcols", help="Number of columns with random data", type=int)
    parser.add_argument("-f", "--file", help="Name of output file", type=str)
    args = parser.parse_args()

    import_string = 'trades:("DIISFFFFFF{}";enlist ",") 0:`:{}'.format("F" * args.randcols, args.file)
    s = ["random{}".format(i) for i in range(args.randcols)]
    cal_string = str.join('+', s)
    file_string = """tstart: .z.t
{}
tend: .z.t
dt: tstart - tend
show "Import: ", string(dt)

tstart: .z.t
tmp: select date, hour, minute, ticker, total: {} from trades
tmp: select date, hour, minute, ticker, average: total % {} from tmp
tend: .z.t
dt: tstart - tend
show "Calculation: ", string(dt)

tstart: .z.t
`:{}` dsave enlist `trades
tend: .z.t
dt: tstart - tend
show "Export: ", string(dt)
\\\\
""".format(import_string, cal_string, args.randcols, '/Users/mikoto/Desktop/kdbDemoEx/so_many_rows/hdb')
    print(file_string)