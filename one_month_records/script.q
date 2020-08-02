// AUTHOR: Zetian Chen
// COMPANY: Caitong Fund, Ltd., Shanghai

// Find the top in_n tickers with the largest earning rate
f_top_n_earning_rate: {
    [in_tab; in_date; in_hour; in_minute; in_interval; in_n]
    
    start_min: in_minute;
    end_min: in_minute + in_interval;

    start_hr: in_hour;
    end_hr: in_hour;

    if [end_min > 59; end_hr: end_hr + 1; end_min: end_min mod 60];
    
    start_records: select ticker, start_cp: cp from in_tab where date = in_date, hour = start_hr, minute = start_min;
    end_records: select ticker, end_cp: cp from in_tab where date = in_date, hour = end_hr, minute = end_min;

    part_s: select by ticker from start_records where ticker in end_records[`ticker];
    part_e: select by ticker from end_records where ticker in start_records[`ticker];

    target: desc select earning_rate: end_cp % start_cp by ticker from (part_s lj part_e);

    select [in_n] from target}


// Entry Point
main: {
    // Read data from the csv file
    trades: ("DIISFFFFFF" ; enlist ",") 0:`:high_freq_201906.csv;

    trade_start_day: 2019.06.03;
    trade_end_day: 2019.06.28;

    // Time periods during which transactions can happen: [9:31, 11:30], [13:01, 15:00]
    trade_start_hr: 9;
    trade_start_min: 31;

    trade_midend_hr: 11;
    trade_midend_min: 30;

    trade_midstart_hr: 13;
    trade_midstart_min: 1;

    trade_end_hr: 15;
    trade_end_min: 0;

    interval: 10;  // 10-minute interval
    num_records: 100;

    // Initialize the current time point
    trade_curr_day: trade_start_day;
    trade_curr_hr: trade_start_hr;
    trade_curr_min: trade_start_min;

    // Check the earning rate with a time interval of 10 minutes
    // Each time, get the top 100 tickers with the largest earning_rate
    while [
        (trade_curr_day >= trade_start_day)
            and (trade_curr_day <= trade_end_day);

        // Query the DB
        result: f_top_n_earning_rate[trades; trade_curr_day; trade_curr_hr; trade_curr_min; interval; num_records];
        show (((("Top 100 Tickers: date=", string(trade_curr_day)), ", hour="), string(trade_curr_hr)), ", min="), string(trade_curr_min);
        show result;

        // Updates
        // Update minute
        trade_curr_min: trade_curr_min + 1;
        // Update hour
        if [trade_curr_min = 60; trade_curr_hr: trade_curr_hr + 1; trade_curr_min: 0];
        // Skip the time period during which transaction is closed
        if [(trade_curr_hr = trade_midend_hr) and (trade_curr_min > (trade_midend_min - interval)); trade_curr_hr: trade_midstart_hr; trade_curr_min: trade_midstart_min];
        // Update date
        if [(trade_curr_hr = (trade_end_hr - 1)) and (trade_curr_min > (60 - interval)); trade_curr_day: trade_curr_day + 1; trade_curr_hr: trade_start_hr; trade_curr_min: trade_start_min];
        // Skip weekends
        week_index: (trade_curr_day - trade_start_day) mod 7;
        // If it is Saturday, directly jump to the next week
        if [week_index = 5; trade_curr_day: trade_curr_day + 2]];

    // Done
    show "All Done."}

// Run the main program
main[]
\\