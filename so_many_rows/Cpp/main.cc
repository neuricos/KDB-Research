#include <iostream>
#include <fstream>
#include <cassert>
#include <vector>
#include <algorithm>
#include <iomanip>
#include "random.h"

using namespace std;

void usage(char *program);
int getHour(void);
int getMinute(int hour);
string getTicker(void);
vector<double> getPrices(double low, double high, int n);

int main(int argc, char *argv[]) {
    if (argc != 4) {  // Check the number of arguments
        cout << argc << endl;
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
        csvfile << ",random" << i;
    }
    csvfile << endl;

    int hour, minute;
    double op, hp, lp, cp, mp, volume, amount;
    string ticker;

    for (int numRecords = 0; numRecords < numRows; numRecords++) {
        hour = getHour();
        minute = getMinute(hour);
        ticker = getTicker();
        mp = randdouble(0.0, 1200.0);
        lp = mp - randdouble(0.0, 0.2 * mp);
        hp = mp + randdouble(0.0, 0.2 * mp);
        op = randdouble(lp, hp);
        cp = randdouble(lp, hp);
        volume = randint(0, 300000000);
        amount = volume * randdouble(12, 13);

        csvfile.unsetf(ios::floatfield);
        csvfile << "20190603"
            << "," << hour
            << "," << minute
            << "," << ticker;
        csvfile << fixed << setprecision(14)
            << "," << op
            << "," << hp
            << "," << lp
            << "," << cp;
        csvfile.unsetf(ios::floatfield);
        csvfile << "," << volume;
        csvfile << fixed << setprecision(14)
            << "," << amount;

        for (int i = 0; i < numCols; i++) {
            csvfile << "," << randdouble(0.0, 2000000000.0);
        }
        csvfile << endl;
    }
    csvfile.close();

    return 0;
}

void usage(char *program) {
    cout << "usage: "
        << program
        << " <number of extra columns> <number of records> <output filename>"
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
    int tickerIndex = randint(0, (sizeof(tickerOptions) / sizeof(string)) - 1);
    string ticker = to_string(tickerNumber);
    int tickerLength = ticker.length();
    for (int i = 0; i < 6 - tickerLength; i++) {
        ticker = "0" + ticker;
    }
    ticker = ticker + "." + tickerOptions[tickerIndex];
    return ticker;
}
