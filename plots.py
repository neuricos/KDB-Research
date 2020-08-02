#author: Wanqing Wang

import matplotlib.pyplot as plt

#### plot for columns vs file size
x = [10 * i for i in range(2, 22)]
y = [150.4, 221.5, 292, 363.3, 433.9, 504.8, 575, 646.2, 716.6, 787.7, 858.5, 928.9, 1024,
     1095.68, 1167.36, 1239.04, 1310.72, 1382.4, 1464.32, 1536]
plt.xlabel("Total Columns", fontsize=16)
plt.ylabel("CSV File Size (MB)", fontsize=16)
plt.title("Total Columns vs. CSV File Size", fontsize=24, fontweight='bold')
plt.plot(x, y)
plt.show()

#### plot for import time
z = [1.557, 2.501, 3.08, 3.822, 4.646, 5.049, 6.1117, 6.9863, 8.0247, 8.4553, 9.5173,
     10.3110, 11.0363, 11.6240, 12.4060, 13.2590, 13.9237, 14.6887, 15.2073, 16.2473]
plt.xlabel("Total Columns", fontsize=16)
plt.ylabel("CSV Import Time (s)", fontsize=16)
plt.title("Total Columns vs. CSV Import Time", fontsize=24, fontweight='bold')
plt.plot(x, z)
plt.show()

#### plot for calculation time
a = [0.017, 0.033, 0.05267, 0.0637, 0.0793, 0.0987, 0.1117, 0.1387, 0.1663, 0.1723,
     0.1873, 0.1933, 0.2227, 0.2380, 0.2353, 0.2647, 0.2487, 0.3047, 0.2913, 0.3203]
plt.xlabel("Total Columns", fontsize=16)
plt.ylabel("Calculation Time (s)", fontsize=16)
plt.title("Total Columns vs. Calculation Time", fontsize=24, fontweight='bold')
plt.plot(x, a)
plt.show()

#### plot for HDB export time
b = [0.139, 0.1526, 0.323, 0.3927, 0.479, 0.5057, 0.6090, 0.6903, 0.7617, 0.8283,
     0.9573, 0.9787, 1.1020, 1.1457, 1.1347, 1.4430, 1.3777,  1.5803, 1.5780, 1.6297]
plt.xlabel("Total Columns", fontsize=16)
plt.ylabel("HDB Export Time (s)", fontsize=16)
plt.title("Total Columns vs. HDB Export Time", fontsize=24, fontweight='bold')
plt.plot(x, b)
plt.show()

#### plot for HDB import time
c = [0.0003, 0.0006, 0.0006, 0.001, 0.001, 0.001, 0.0013, 0.0013, 0.0003, 0.0013,
     0.0017, 0.001, 0.0017, 0.002, 0.001, 0.0023, 0.0017, 0.0023, 0.0027, 0.0030]
plt.xlabel("Total Columns", fontsize=16)
plt.ylabel("HDB Import Time (s)", fontsize=16)
plt.title("Total Columns vs. HDB Import Time", fontsize=24, fontweight='bold')
plt.plot(x, c)
plt.show()