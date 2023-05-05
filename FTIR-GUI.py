import os
import tkinter as tk
import matplotlib.pyplot as plt
from matplotlib.backend_bases import PickEvent
from matplotlib.figure import Figure
from pandas import read_csv
from matplotlib.widgets import Cursor
from tkinter import filedialog

# Create the main window
window = tk.Tk()
window.title("FTIR DATA PLOTER")
filepaths_str = tk.StringVar()


def open_file_dialog(filenames_txtbox: tk.Text, filepaths_str: tk.StringVar) -> None:
    """open file picker and set the texts in text box"""

    filepaths = filedialog.askopenfilenames(initialdir=".", title="Select files",
                                            filetypes=[("Text files", "*.csv")], multiple=True)  # type: ignore

    filepaths_str.set(",".join(filepaths))  # save the path of all selected data files.
    # format data file names to display in text box
    txtbox_str = ",".join(map(lambda x: x.split(os.sep)[-1], filepaths))

    filenames_txtbox.configure(state=tk.NORMAL)
    filenames_txtbox.delete('1.0', tk.END)
    filenames_txtbox.insert(tk.END, txtbox_str)
    filenames_txtbox.configure(state=tk.DISABLED)


def on_pick(event: PickEvent, graphs: dict, fig: Figure) -> None:
    """function for show-hide feature"""

    legend = event.artist
    isVisible = legend.get_visible()

    graphs[legend].set_visible(not isVisible)
    legend.set_visible(not isVisible)

    fig.canvas.draw()


def display_graphs(filepaths_str: tk.StringVar, filenames_txtbox: tk.Text) -> None:
    """displaying plots and other features activates after click on 'Display Graphs(s)'"""

    file_paths = filepaths_str.get().split(",")
    dataframes = [read_csv(filename, skiprows=1).dropna() for filename in file_paths]
    txtbox_str = filenames_txtbox.get("1.0", "end")
    datafile_names = tuple(map(lambda x: x.split('.')[0], txtbox_str.strip().split(',')))

    # create a plot which displays all selected dataframes
    fig, ax = plt.subplots()
    fig.set_size_inches(w=10, h=6)
    fig.set_tight_layout(True)
    lines = []
    for dataframe in dataframes:
        lines.append(ax.plot(dataframe["cm-1"], dataframe["%T"], '-')[0])
    ax.set_xlabel("cm-1")
    ax.set_ylabel("%T")
    ax.grid()
    ax.set_title(f"Transmition vs wave number of {', '.join(datafile_names)}")

    # config plot for show-hide feature
    legends = ax.legend(datafile_names, loc="lower right")
    for legend in legends.get_lines():
        legend.set_picker(True)
        legend.set_pickradius(5)
    graphs = dict(zip(legends.get_lines(), lines))

    cursor = Cursor(ax, color='k', linewidth=1)
    plt.connect('pick_event', lambda event: on_pick(event, graphs, fig))  # connect mouse click event
    plt.show()


# defining the elements in the window
textbox = tk.Text(window, height=1, width=30, state="disabled")
btn1 = tk.Button(window, text="Select Data file(s)", command=lambda: open_file_dialog(textbox, filepaths_str))
button1 = tk.Button(window, text="Display Graph(s)", command=lambda: display_graphs(filepaths_str, textbox))
button3 = tk.Button(window, text="Close", command=window.destroy)

# display the label, textbox, and buttons on the window
textbox.grid(row=0, column=0, columnspan=3)
btn1.grid(row=1, column=0)
button1.grid(row=1, column=1)
button3.grid(row=1, column=2)

window.mainloop()
