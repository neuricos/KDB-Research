from matplotlib import pyplot

if __name__ == "__main__":
    colnums = [20, 30, 60, 110, 160, 210]
    filesizes = [315.4, 507, 1105.92, 2088.96, 3072, 4055.04]
    importtimes = [
        (5.588, 5.569, 5.944),
        (8.803, 9.023, 9.184),
        (19.606, 23.281, 20.184),
        (33.866, 34.413, 34.144),
        (50.256, 55.537, 52.658),
        (71.527, 65.956, 64.976, 77.178)
    ]
    exporttimes = [
        (0.229, 0.227, 0.232),
        (0.305, 0.284, 0.290),
        (0.500, 0.502, 0.505),
        (0.847, 0.843, 0.834),
        (1.211, 1.284, 1.092),
        (2.401, 1.622, 1.638, 0.285)
    ]
    calculationtimes = [
        (0.016, 0.017, 0.021),
        (0.032, 0.039, 0.039),
        (0.079, 0.099, 0.088),
        (0.126, 0.142, 0.143),
        (0.205, 0.233, 0.216),
        (1.332, 0.250, 0.263, 1.620)
    ]
    reimporttimes = [
        (0.0, 0.0, 0.0),
        (0.0, 0.0, 0.0),
        (0.0, 0.0, 0.0),
        (0.0, 0.0, 0.0),
        (0.308, 0.326, 0.340),
        (0.636, 0.396, 0.316, 0.380)
    ]

    importtimes = [sum(importtime) / len(importtime) for importtime in importtimes]
    exporttimes = [sum(exporttime) / len(exporttime) for exporttime in exporttimes]
    calculationtimes = [sum(calculationtime) / len(calculationtime) for calculationtime in calculationtimes]
    reimporttimes = [sum(reimporttime) / len(reimporttime) for reimporttime in reimporttimes]

    # File size
    pyplot.plot(colnums, filesizes)
    pyplot.title('File Size vs. Number of Columns', fontsize=16, fontweight='bold')
    pyplot.xlabel('Number of Columns')
    pyplot.ylabel('Size (MB)')
    pyplot.show()

    # CSV import
    pyplot.plot(colnums, importtimes)
    pyplot.title('Time to Import CSV vs. Number of Columns', fontsize=16, fontweight='bold')
    pyplot.xlabel('Number of Columns')
    pyplot.ylabel('Time (s)')
    pyplot.show()

    # HDB export
    pyplot.plot(colnums, exporttimes)
    pyplot.title('Time to Export HDB vs. Number of Columns', fontsize=16, fontweight='bold')
    pyplot.xlabel('Number of Columns')
    pyplot.ylabel('Time (s)')
    pyplot.show()

    # Calculation
    pyplot.plot(colnums, calculationtimes)
    pyplot.title('Calculation vs. Number of Columns', fontsize=16, fontweight='bold')
    pyplot.xlabel('Number of Columns')
    pyplot.ylabel('Time (s)')
    pyplot.show()

    pyplot.plot(colnums, reimporttimes)
    pyplot.title('Time to Import HDB vs. Number of Columns', fontsize=16, fontweight='bold')
    pyplot.xlabel('Number of Columns')
    pyplot.ylabel('Time (s)')
    pyplot.show()