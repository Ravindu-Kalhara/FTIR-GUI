import os
import customtkinter as ctk
import matplotlib.pyplot as plt
from matplotlib.backend_bases import PickEvent
from matplotlib.figure import Figure
from pandas import read_csv
from matplotlib.widgets import Cursor
from customtkinter import filedialog

ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")

# Create the main window
window = ctk.CTk()
window.title("FTIR DATA PLOTER")
filepaths_str = ctk.StringVar()


def open_file_dialog(filenames_txtbox: ctk.CTkEntry, filepaths_str: ctk.StringVar) -> None:
    """open file picker and set the texts in filenames entry box"""

    filepaths = filedialog.askopenfilenames(
        initialdir=".", title="Select files", filetypes=[("Text files", "*.csv")], multiple=True  # type: ignore
    )

    filepaths_str.set(",".join(filepaths))  # save the path of all selected data files.
    # format data file names to display in text box
    txtbox_str = ",".join(map(lambda x: x.split(os.sep)[-1], filepaths))

    filenames_txtbox.configure(state=ctk.NORMAL)
    filenames_txtbox.delete(0, ctk.END)
    filenames_txtbox.insert(ctk.END, txtbox_str)
    filenames_txtbox.configure(state=ctk.DISABLED)


def on_pick(event: PickEvent, graphs: dict, fig: Figure) -> None:
    """function for show-hide feature"""

    legend = event.artist
    isVisible = legend.get_visible()

    graphs[legend].set_visible(not isVisible)
    legend.set_visible(not isVisible)

    fig.canvas.draw()


def display_graphs(filepaths_str: ctk.StringVar, filenames_txtbox: ctk.CTkEntry) -> None:
    """displaying plots and other features activates after click on 'Display Graphs(s)'"""

    file_paths = filepaths_str.get().split(",")
    dataframes = [read_csv(filename, skiprows=1).dropna() for filename in file_paths]
    txtbox_str = filenames_txtbox.get()
    datafile_names = tuple(map(lambda x: x.split(".")[0], txtbox_str.strip().split(",")))

    # create a plot which displays all selected dataframes
    fig, ax = plt.subplots()
    fig.set_size_inches(w=10, h=6)
    fig.set_tight_layout(True)
    lines = []
    for dataframe in dataframes:
        lines.append(ax.plot(dataframe["cm-1"], dataframe["%T"], "-")[0])
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

    cursor = Cursor(ax, color="k", linewidth=1)  # noqa: F841
    plt.connect("pick_event", lambda event: on_pick(event, graphs, fig))  # connect mouse click event
    plt.show()


# defining the elements in the window
frame_1 = ctk.CTkFrame(window)
filenames = ctk.CTkEntry(frame_1, width=400, state="disabled")
btn1 = ctk.CTkButton(frame_1, text="Select Data file(s)", command=lambda: open_file_dialog(filenames, filepaths_str))
button1 = ctk.CTkButton(frame_1, text="Display Graph(s)", command=lambda: display_graphs(filepaths_str, filenames))

frame_2 = ctk.CTkFrame(window)
filemin_lbl = ctk.CTkLabel(frame_2, text="Select the data file which \n wants to find local minimum")
filemin_txt = ctk.CTkEntry(frame_2, state=ctk.DISABLED)
filemin_btn = ctk.CTkButton(frame_2, text="Select Data file")
lower_bound_lbl = ctk.CTkLabel(frame_2, text="Enter the lower bound")
lower_bound_txt = ctk.CTkEntry(frame_2)
upper_bound_lbl = ctk.CTkLabel(frame_2, text="Enter the upper bound")
upper_bound_txt = ctk.CTkEntry(frame_2)
minimum_lbl = ctk.CTkLabel(frame_2, text="Minimum data point")
minimum_txt = ctk.CTkEntry(frame_2, state=ctk.DISABLED)
minimum_btn = ctk.CTkButton(frame_2, text="Find Minimum")
button3 = ctk.CTkButton(frame_2, text="Close", command=window.destroy)

# display the label, filenames, and buttons on the window
frame_1.pack()
filenames.grid(row=0, column=0, columnspan=3)
btn1.grid(row=1, column=0)
button1.grid(row=1, column=1)

frame_2.pack()
filemin_lbl.grid(row=0, column=0)
filemin_txt.grid(row=0, column=1)
filemin_btn.grid(row=0, column=2)
lower_bound_lbl.grid(row=1, column=0)
lower_bound_txt.grid(row=1, column=1)
upper_bound_lbl.grid(row=2, column=0)
upper_bound_txt.grid(row=2, column=1)
minimum_lbl.grid(row=3, column=0)
minimum_txt.grid(row=3, column=1)
minimum_btn.grid(row=4, column=0)
button3.grid(row=4, column=1)

window.mainloop()
