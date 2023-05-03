import pandas as pd


def import_data(directory: str, locations: tuple, num_test_per_sample: int) -> tuple:
    """Function to import raw readings from csv files"""

    samples = ()
    for location in locations:
        s = ()
        for i in range(1, num_test_per_sample+1):
            s += (pd.read_csv(f"{directory}/{location}{i}.csv",
                  skiprows=1).dropna(), )
        samples += (s, )
    return samples


locations = ('A', 'D', 'K', 'M', 'N', 'S', 'W')
A, D, K, M, N, S, W = import_data('.', locations, 3)


def get_minimum(sample: tuple, range: tuple):
    data1, data2, data3 = sample

    data1 = data1[(data1["cm-1"] > range[0]) & (data1["cm-1"] < range[1])]
    data2 = data2[(data2["cm-1"] > range[0]) & (data2["cm-1"] < range[1])]
    data3 = data3[(data3["cm-1"] > range[0]) & (data3["cm-1"] < range[1])]

    min_data1 = data1[data1["%T"] == data1["%T"].min()]
    min_data2 = data2[data2["%T"] == data2["%T"].min()]
    min_data3 = data3[data3["%T"] == data3["%T"].min()]

    return min_data1, min_data2, min_data3


mins = get_minimum(D, (485.01, 490.11))
print(mins[0])
print(mins[1])
print(mins[2])
