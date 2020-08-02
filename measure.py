import datetime
import os

if __name__ == '__main__':
    num_runs = 10
    total = datetime.timedelta(0)

    for i in range(num_runs):
        start = datetime.datetime.now()
        os.system('~/q/m64/q script.q &>/dev/null')
        end = datetime.datetime.now()
        total += end - start
        print("round #{}: {}s".format(i + 1, (end - start).seconds))

    avg = total / num_runs
    print()
    print("Avg time: {}s".format(avg.seconds))