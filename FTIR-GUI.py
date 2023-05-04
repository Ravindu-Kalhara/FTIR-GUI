import os
import tkinter as tk
import pandas as pd
import matplotlib.pyplot as plt
from tkinter import filedialog
from Essentials import Essentials

# Create the main window
window = tk.Tk()
window.title("FTIR DATA PLOTER")
filepaths_str = tk.StringVar()

Ess = Essentials()

def open_file_dialog(filenames_txtbox: tk.Text, filepaths_str: tk.StringVar) -> None:
    filepaths = filedialog.askopenfilenames(initialdir=".", title="Select files",
                                            filetypes=[("Text files", "*.csv")], multiple=True)  # type: ignore

    filepaths_str.set(",".join(filepaths))  # save the path of all selected data files.
    # format data file names to display in text box
    txtbox_str = ",".join(map(lambda x: x.split(os.sep)[-1], filepaths))

    filenames_txtbox.configure(state=tk.NORMAL)
    filenames_txtbox.delete('1.0', tk.END)
    filenames_txtbox.insert(tk.END, txtbox_str)
    filenames_txtbox.configure(state=tk.DISABLED)


def run_code(filepaths_str: tk.StringVar, filenames_txtbox: tk.Text) -> None:
    # Get the filenames from the textbox
    file_paths = filepaths_str.get().split(",")

    # Load the csv files into pandas dataframes
    dataframes = [pd.read_csv(filename, skiprows=1) for filename in file_paths]

    # Defining plots
    fig, ax = plt.subplots()
    for dataframe in dataframes:
        dataframe.plot("cm-1", ax=ax)  # type: ignore

    # Set the axis labels and title
    ax.set_xlabel("cm-1")
    ax.set_ylabel("%T")
    ax.set_title("Transmition vs wave number")
    ax.legend()
    plt.show()

    # clear the text box containing data file names.
    filenames_txtbox.configure(state=tk.NORMAL)
    filenames_txtbox.delete('1.0', tk.END)
    filenames_txtbox.configure(state=tk.DISABLED)


# defining the elements in the window
textbox = tk.Text(window, height=1, width=30, state="disabled")
btn1 = tk.Button(window, text="Select Data file(s)", command=lambda: open_file_dialog(textbox, filepaths_str))
button1 = tk.Button(window, text="Display Graph(s)", command=lambda: run_code(filepaths_str, textbox))
button3 = tk.Button(window, text="Close", command=window.destroy)

# Pack the label, textbox, and buttons in the window
textbox.grid(row=0, column=0, columnspan=3)
btn1.grid(row=1, column=0)
button1.grid(row=1, column=1)
button3.grid(row=1, column=2)

window.mainloop()
