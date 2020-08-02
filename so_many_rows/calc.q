tstart: .z.t
trades:("DIISFFFFFFF";enlist ",") 0:`:converted.csv
tend: .z.t
dt: tstart - tend
show "Import: ", string(dt)

tstart: .z.t
tmp: select date, hour, minute, ticker, total: random0 from trades
tmp: select date, hour, minute, ticker, average: total % 1 from tmp
tend: .z.t
dt: tstart - tend
show "Calculation: ", string(dt)

tstart: .z.t
`:/Users/mikoto/Desktop/kdbDemoEx/so_many_rows/hdb` dsave enlist `trades
tend: .z.t
dt: tstart - tend
show "Export: ", string(dt)
\\

