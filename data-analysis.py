import matplotlib.pyplot as plt
import pandas as pd
from matplotlib.widgets import Cursor


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


def make_plt(subplt: tuple, data: tuple, location: str, visibility: tuple):
    global X
    ax = plt.subplot2grid(*subplt[:2], rowspan=subplt[2], colspan=subplt[3])
    s1, = ax.plot(data[0]["cm-1"], data[0]["%T"],
                  '-r', label=1, antialiased=True)
    s2, = ax.plot(data[1]["cm-1"], data[1]["%T"],
                  '-g', label=2, antialiased=True)
    s3, = ax.plot(data[2]["cm-1"], data[2]["%T"],
                  '-b', label=3, antialiased=True)
    s4, = ax.plot(X["cm-1"], X["%T"], '-m', label='X', antialiased=True)
    s1.set_visible(visibility[0])
    s2.set_visible(visibility[1])
    s3.set_visible(visibility[2])
    s4.set_visible(True)
    ax.set_xlabel("cm-1")
    ax.set_ylabel("%T")
    ax.set_title(f"Transmition vs wave number ({location})")
    ax.legend(loc="lower right")
    ax.grid()
    plt.tight_layout()
    return ax


locations = ('A', 'D', 'K', 'M', 'N', 'S', 'W')
A, D, K, M, N, S, W = import_data('.', locations, 3)

X = pd.read_csv("./XX.txt", skiprows=10, header=None).dropna()
X[1] = 100 - 100*X[1]
X.columns = ["cm-1", "%T"]
X["cm-1"] = pd.to_numeric(X["cm-1"])

plt.figure(1, figsize=(10, 6))
ax1 = make_plt(((1, 1), (0, 0), 1, 1), A, "Attipola", (1, 1, 1))  # Done
# ax1 = make_plt(((1, 1), (0, 0), 1, 1), D, "Dutuwewa", (1, 1, 1))
# ax1 = make_plt(((1, 1), (0, 0), 1, 1), K, "Kiridigalla", (1, 1, 1))
# ax1 = make_plt(((2, 2), (1, 1), 1, 1), M, "Moragahakanda", (1, 1, 1))

# plt.figure(2, figsize=(10, 6))
# ax1 = make_plt(((2, 2), (0, 0), 1, 1), N, "Nawula", (1, 1, 1))
# ax1 = make_plt(((2, 2), (0, 1), 1, 1), S, "Synthetic", (1, 1, 1))
# ax1 = make_plt(((2, 2), (1, 0), 1, 1), W, "Warapitiya", (1, 1, 1))

cursor = Cursor(ax1, color='k', linewidth=1)
plt.show()
