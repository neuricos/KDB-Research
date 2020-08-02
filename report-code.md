# Appendix

## Generate CSV File with Random Data

### random.h

```cpp
#ifndef _RANDOM_H_
#define _RANDOM_H_

/* Generate a random integer within range [low, high] */
int randint(int low, int high);
/* Generate a random double within range [low, high] */
double randdouble(double low, double high);
/* Generat a random boolean value */
bool randbool();

#endif  // _RANDOM_H_
```

### random.cc

```cpp
#include <random>
#include <ctime>
#include <cassert>
#include "random.h"

using namespace std;

const int primes[] = {2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43,
47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127,
131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199,
211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283,
293, 307, 311, 313, 317, 331, 337, 347, 349, 353, 359, 367, 373, 379, 383,
389, 397, 401, 409, 419, 421, 431, 433, 439, 443, 449, 457, 461, 463, 467,
479, 487, 491, 499, 503, 509, 521, 523, 541, 547, 557, 563, 569, 571, 577,
587, 593, 599, 601, 607, 613, 617, 619, 631, 641, 643, 647, 653, 659, 661,
673, 677, 683, 691, 701, 709, 719, 727, 733, 739, 743, 751, 757, 761, 769,
773, 787, 797, 809, 811, 821, 823, 827, 829, 839, 853, 857, 859, 863, 877,
881, 883, 887, 907, 911, 919, 929, 937, 941, 947, 953, 967, 971, 977, 983,
991, 997};
const int numPrimes = 168;

default_random_engine getEngine() {
    static int primeIndex = 0;
    primeIndex = primeIndex % ::numPrimes;
    default_random_engine e(time(0) + primes[primeIndex]);
    e.seed(time(0) * primeIndex);
    primeIndex++;
    return e;
}

int randint(int low, int high) {
    assert(high >= low);
    default_random_engine e = getEngine();
    return e() % (high - low + 1) + low;
}

double randdouble(double low, double high) {
    assert(high >= low);
    default_random_engine e = getEngine();
    uniform_real_distribution<double> u(low, high);
    return u(e);
}

bool randbool() {
    int rval = randint(0, 1);
    return rval == 0? false : true;
}
```

### main.cc

```cpp
#include <iostream>
#include <fstream>
#include <cassert>
#include <vector>
#include <algorithm>
#include "random.h"

using namespace std;

void usage(char *program);
int getHour(void);
int getMinute(int hour);
string getTicker(void);
vector<double> getPrices(double low, double high, int n);

int main(int argc, char *argv[]) {
    if (argc != 4) {  // Check the number of arguments
        usage(argv[0]);
        return 1;
    }

    int numCols = atoi(argv[1]);
    int numRows = atoi(argv[2]);
    string outFileName(argv[3]);
    assert(numCols >= 0);
    assert(numRows >= 0);

    // Create a output file stream
    ofstream csvfile;
    csvfile.open(outFileName);

    // Print the first row -- column names
    csvfile << "date,hour,minute,ticker,op,hp,lp,cp,volume,amount";
    for (int i = 0; i < numCols; i++) {
        csvfile << ", random" << i;
    }
    csvfile << endl;

    int hour, minute;
    double op, hp, lp, cp, volume, amount;
    string ticker;
    vector<double> prices;

    for (int numRecords = 0; numRecords < numRows; numRecords++) {
        // Generate random data
        hour = getHour();
        minute = getMinute(hour);
        ticker = getTicker();
        prices = getPrices(10.0, 99.0, 2);
        hp = *max_element(prices.begin(), prices.end());
        lp = *min_element(prices.begin(), prices.end());
        op = randdouble(lp, hp);
        cp = randdouble(lp, hp);
        volume = double(randint(1000000, 10000000));
        amount = volume * randdouble(lp, hp);

        // Write to the csv file
        csvfile << "20190603"
            << "," << hour
            << "," << minute
            << "," << ticker
            << "," << op
            << "," << hp
            << "," << lp
            << "," << cp
            << "," << volume
            << "," << amount;
        // Write random data
        for (int i = 0; i < numCols; i++) {
            csvfile << "," << randdouble(10000, 1000000);
        }
        csvfile << endl;
    }
    csvfile.close();
    return 0;
}

void usage(char *program) {
    cout << "usage: "
    << program
    << " <number of extra columns> <number of records> <output file name>"
    << endl;
}

int getHour(void) {
    return randbool()? randint(9, 11) : randint(13, 15);
}

int getMinute(int hour) {
    assert((hour >= 9 && hour <= 11) || (hour >= 13 && hour <= 15));
    switch(hour) {
        case 9:
            return randint(31, 59);
        case 11:
            return randint(0, 30);
        case 13:
            return randint(1, 59);
        case 15:
            return 0;
        default:
            return randint(0, 59);
    }
}

string getTicker(void) {
    const string tickerOptions[] = {"SZ", "SH", "HK"};
    int tickerNumber = randint(1, 999999);
    int tickerIndex = randint(0,
        (sizeof(tickerOptions) / sizeof(string)) - 1);
    string ticker = to_string(tickerNumber);
    int tickerLength = ticker.length();
    for (int i = 0; i < 6 - tickerLength; i++) {
        ticker = "0" + ticker;
    }
    ticker = ticker + "." + tickerOptions[tickerIndex];
    return ticker;
}

vector<double> getPrices(double low, double high, int n) {
    assert(high >= low);
    assert(n > 0);
    vector<double> retVec;
    for (int i = 0; i < n; i++) {
        retVec.push_back(randdouble(low, high));
    }
    sort(retVec.begin(), retVec.end());
    return retVec;
}
```

### Makefile

```makefile
COMPILER=g++
FLAGS=-Wall -g -std=c++11

all: main

main: main.o random.o
	${COMPILER} ${FLAGS} $^ -o $@

main.o: main.cc random.h
	${COMPILER} ${FLAGS} -c $< -o $@

random.o: random.cc random.h
	${COMPILER} ${FLAGS} -c $< -o $@
```

## Code to Generate Random CSV File in Python

**Same functionality, just slower**

### gen_fake_data.py

```python
import argparse
import random

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-c", "--randcols",
        help="Number of columns with random data", type=int)
    parser.add_argument("-r", "--rowcnt",
        help="Number of fake records", type=int)
    parser.add_argument("-f", "--file",
        help="Name of output file", type=str)
    args = parser.parse_args()

    with open(args.file, 'w') as f:
        # Write the column names
        f.write("date,hour,minute,ticker,op,hp,lp,cp,volume,amount")
        for col in range(0, args.randcols):
            f.write(",random{}".format(col))
        f.write("\n")

        # Write the data
        for _ in range(args.rowcnt):
            # Randomly if the transaction happens in the morning
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
            ticker = "{:06d}.{}".format(ticker_number,
                ["SZ", "SH", "HK"][ticker_index])

            # Let lowest price and highest price be within [10, 90]
            prices = [random.uniform(10, 90) for _ in range(2)]
            hp = max(prices)
            lp = min(prices)
            op = random.uniform(lp, hp)
            cp = random.uniform(lp, hp)
            volume = random.randint(1000000, 10000000)
            amount = volume * random.uniform(lp, hp)

            # Write the values into the csv file
            f.write("20190603,{},{},{},{},{},{},{},{},{}".\
              format(hour, minute, ticker, op, hp, lp, cp, volume, amount))
            # Randomly generate floats
            for _ in range(args.randcols):
                value = random.uniform(10000, 1000000)
                f.write(", {}".format(value))
            f.write("\n")
    f.close()
    print("Done.")
```

## Generate q Code to Do CSV Import, Calculation, and Export

```python
import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-c", "--randcols",
        help="Number of columns with random data", type=int)
    parser.add_argument("-f", "--file",
        help="Name of output file", type=str)
    args = parser.parse_args()

    import_string = 'trades:("DIISFFFFFF{}";enlist ",") 0:`:{}'.\
            format("F" * args.randcols, args.file)
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
""".format(import_string, cal_string, args.randcols,
    '/Users/mikoto/Desktop/kdb_demo_ex/so_many_rows/hdb')
    print(file_string)
```

## Re-import Data into KDB from History Database

```kdb+
t1: .z.t
\l hdb
t2: .z.t
dt: t2 - t1
show dt
```

## Analyze the Data and Generate Formulas

```
#!/usr/bin/ruby

def avg(arr)
    arr.inject{ |sum, el| sum + el }.to_f / arr.size
end

import_times = []
calc_times = []
export_times = []
reimport_times = []

f = File.open('output.txt', 'r')
f.each_line do |line|
    line.chomp!
    m = line.match /\"(?<name>.*): -?(\d*:)+(?<time>.*)\"/
    if m.nil? then next end

    if m[:name] == 'Import'
        import_times.push(m[:time].to_f)
    elsif m[:name] == 'Calculation'
        calc_times.push(m[:time].to_f)
    elsif m[:name] == 'Export'
        export_times.push(m[:time].to_f)
    elsif m[:name] == 'Reimport'
        reimport_times.push(m[:time].to_f)
    else
        next
    end
end
f.close

puts "     Import: (#{import_times.join('+')})/#{import_times.size}="
puts "%.4f" % avg(import_times)
puts "Calculation: (#{calc_times.join('+')})/#{calc_times.size}="
puts "%.4f" % avg(calc_times)
puts "     Export: (#{export_times.join('+')})/#{export_times.size}="
puts "%.4f" % avg(export_times)
puts "   Reimport: (#{reimport_times.join('+')})/#{reimport_times.size}="
puts "%.4f" % avg(reimport_times)
```

## To Make It All Work

```bash
#!/bin/bash

usage() { echo "Usage: $0 [-c] [-f]" 1>&2; exit 1; }

while getopts ":c:f:" o; do
    case "${o}" in
        c)
            cols=${OPTARG}
            ;;
        f)
            file=${OPTARG}
            ;;
        *)
            usage
            ;;
    esac
done
shift $((OPTIND - 1))

if [ -z "${cols}" ] || [ -z "$file" ] ; then
    usage
fi

rm -rf output.txt
for i in {1..3} ; do
    python3 gen_q_script.py -c ${cols} -f ${file} > calc.q
    rlwrap q calc.q 2>/dev/null 1>>output.txt
    rm -rf hdb/.DS_Store
    rlwrap q reimport.q 2>/dev/null 1>>output.txt
    echo "" >>output.txt
    # Clean up
    rm -rf hdb
    mkdir hdb
done

./analyze.rb
```

## Experiment Records

![experiment records](./horizontal-result.png)

## Plot the Graphs

**Help from Sophia Wang**

```python
#author: Wanqing Wang

import matplotlib.pyplot as plt

#### plot for columns vs file size
x = [10 * i for i in range(2, 22)]
y = [150.4, 221.5, 292, 363.3, 433.9, 504.8, 575, 646.2, 716.6, 787.7,
    858.5, 928.9, 1024, 1095.68, 1167.36, 1239.04, 1310.72, 1382.4,
    1464.32, 1536]
plt.xlabel("Total Columns")
plt.ylabel("CSV File Size (MB)")
plt.title("Total Columns v.s. CSV File Size",
    fontsize=14, fontweight='bold')
plt.plot(x, y)
plt.show()

#### plot for import time
z = [1.557, 2.501, 3.08, 3.822, 4.646, 5.049, 6.1117, 6.9863, 8.0247,
    8.4553, 9.5173, 10.3110, 11.0363, 11.6240, 12.4060, 13.2590,
    13.9237, 14.6887, 15.2073, 16.2473]
plt.xlabel("Total Columns")
plt.ylabel("CSV Import Time (s)")
plt.title("Total Columns v.s. CSV Import Time",
    fontsize=14, fontweight='bold')
plt.plot(x, z)
plt.show()

#### plot for calculation time
a = [0.017, 0.033, 0.05267, 0.0637, 0.0793, 0.0987, 0.1117, 0.1387,
    0.1663, 0.1723, 0.1873, 0.1933, 0.2227, 0.2380, 0.2353, 0.2647,
    0.2487, 0.3047, 0.2913, 0.3203]
plt.xlabel("Total Columns")
plt.ylabel("Calculation Time (s)")
plt.title("Total Columns v.s. Calculation Time",
    fontsize=14, fontweight='bold')
plt.plot(x, a)
plt.show()

#### plot for HDB export time
b = [0.139, 0.1526, 0.323, 0.3927, 0.479, 0.5057, 0.6090, 0.6903,
    0.7617, 0.8283, 0.9573, 0.9787, 1.1020, 1.1457, 1.1347, 1.4430, 1.3777,
    1.5803, 1.5780, 1.6297]
plt.xlabel("Total Columns")
plt.ylabel("HDB Export Time (s)")
plt.title("Total Columns v.s. HDB Export Time",
    fontsize=14, fontweight='bold')
plt.plot(x, b)
plt.show()

#### plot for HDB import time
c = [0.0003, 0.0006, 0.0006, 0.001, 0.001, 0.001, 0.0013, 0.0013,
    0.0003, 0.0013, 0.0017, 0.001, 0.0017, 0.002, 0.001, 0.0023, 0.0017,
    0.0023, 0.0027, 0.0030]
plt.xlabel("Total Columns")
plt.ylabel("HDB Import Time (s)")
plt.title("Total Columns v.s. HDB Import Time",
    fontsize=14, fontweight='bold')
plt.plot(x, c)
plt.show()
```