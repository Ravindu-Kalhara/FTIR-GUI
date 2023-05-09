import customtkinter as ctk
import matplotlib.pyplot as plt
from matplotlib.backend_bases import PickEvent
from matplotlib.figure import Figure
from matplotlib.widgets import Cursor
from os import sep
from customtkinter import filedialog
from pandas import read_csv


class Graphs:
    def __init__(self, master: ctk.CTkFrame) -> None:
        self.master = master
        self.filepaths_str = ctk.StringVar()

        self.filenames_entry = ctk.CTkEntry(self.master, width=400, state="disabled")
        self.filesselect_btn = ctk.CTkButton(self.master, text="Select Data file(s)", command=self.__open_file_dialog)
        self.display_graphs_btn = ctk.CTkButton(
            self.master,
            text="Display Graph(s)",
            command=self.__display_graphs,
        )

        self.filenames_entry.grid(row=0, column=0, columnspan=3)
        self.filesselect_btn.grid(row=1, column=0)
        self.display_graphs_btn.grid(row=1, column=1)

    def __open_file_dialog(self) -> None:
        """open file picker and set the texts in filenames entry box"""

        filepaths = filedialog.askopenfilenames(
            initialdir=".", title="Select files", filetypes=[("Text files", "*.csv")], multiple=True  # type: ignore
        )

        self.filepaths_str.set(",".join(filepaths))  # save the path of all selected data files.
        # format data file names to display in text box
        txtbox_str = ",".join(map(lambda x: x.split(sep)[-1], filepaths))

        self.filenames_entry.configure(state=ctk.NORMAL)
        self.filenames_entry.delete(0, ctk.END)
        self.filenames_entry.insert(ctk.END, txtbox_str)
        self.filenames_entry.configure(state=ctk.DISABLED)

    def __on_pick(self, event: PickEvent, graphs: dict, fig: Figure) -> None:
        """function for show-hide feature"""

        legend = event.artist
        isVisible = legend.get_visible()
        graphs[legend].set_visible(not isVisible)
        legend.set_visible(not isVisible)
        fig.canvas.draw()

    def __display_graphs(self) -> None:
        """displaying plots and other features activates after click on 'Display Graphs(s)'"""

        file_paths = self.filepaths_str.get().split(",")
        dataframes = [read_csv(filename, skiprows=1).dropna() for filename in file_paths]
        txtbox_str = self.filenames_entry.get()
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
        plt.connect("pick_event", lambda event: self.__on_pick(event, graphs, fig))  # connect mouse click event
        plt.show()
