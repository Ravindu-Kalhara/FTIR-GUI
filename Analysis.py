import customtkinter as ctk
from customtkinter import filedialog
from tkinter import messagebox
from os import sep
from pandas import read_csv


class Analysis:
    def __init__(self, master: ctk.CTkFrame) -> None:
        """Class which defined for FTIR data analysis and to define all UI elements which are releated
        to FTIR data analysis.

        :param master: the master container widget for other UI elements are defined in Analysis class
        :type master: ctk.CTkFrame
        """

        self.master = master
        self.filepath_str = ctk.StringVar()

        # Define all UI elements used in Analysis class. They are defined explicitly because with that, UI customization
        # become much eassy.
        self.filemin_lbl = ctk.CTkLabel(self.master, text="Select the data file which \n wants to find local minimum")
        self.filemin_entry = ctk.CTkEntry(self.master, state=ctk.DISABLED)
        self.filemin_btn = ctk.CTkButton(self.master, text="Select Data file", command=self.__open_file_dialog)
        self.lower_bound_lbl = ctk.CTkLabel(self.master, text="Enter the lower bound")
        self.lower_bound_entry = ctk.CTkEntry(self.master)
        self.upper_bound_lbl = ctk.CTkLabel(self.master, text="Enter the upper bound")
        self.upper_bound_entry = ctk.CTkEntry(self.master)
        self.minimum_lbl = ctk.CTkLabel(self.master, text="Minimum data point(s)")
        self.minimum_entry = ctk.CTkEntry(self.master, state=ctk.DISABLED)
        self.minimum_btn = ctk.CTkButton(self.master, text="Find Minimum", command=self.__get_minimum)

        self.filemin_lbl.grid(row=0, column=0)
        self.filemin_entry.grid(row=0, column=1)
        self.filemin_btn.grid(row=0, column=2)
        self.lower_bound_lbl.grid(row=1, column=0)
        self.lower_bound_entry.grid(row=1, column=1)
        self.upper_bound_lbl.grid(row=2, column=0)
        self.upper_bound_entry.grid(row=2, column=1)
        self.minimum_lbl.grid(row=3, column=0)
        self.minimum_entry.grid(row=3, column=1)
        self.minimum_btn.grid(row=4, column=0)

    def __get_minimum(self) -> None:
        """Disply the wave numbers which has lowest relative transmistion in the given wave number range in
        self.minimum_entry entry box."""
        try:
            # Find the minimum(s)
            df = read_csv(self.filepath_str.get(), skiprows=1).dropna()
            lower_bound = float(self.lower_bound_entry.get().strip())
            upper_bound = float(self.upper_bound_entry.get().strip())
            selected_range = df.loc[(df["cm-1"] >= lower_bound) & (df["cm-1"] <= upper_bound)]
            mins = selected_range[selected_range["%T"] == selected_range["%T"].min()]["cm-1"]
            mins_str = ",".join(map(str, mins))

            # Display the minimum(s) in self.minimum_entry entry box
            self.minimum_entry.configure(state=ctk.NORMAL)
            self.minimum_entry.delete(0, ctk.END)
            self.minimum_entry.insert(ctk.END, mins_str)
            self.minimum_entry.configure(state=ctk.DISABLED)
        except FileNotFoundError as fnf:
            print(fnf)
            messagebox.showwarning("Warning", "Please select a valid FTIR data file.")
        except ValueError as ve:
            print(ve)
            messagebox.showwarning(
                "Warning", "Please check whether is lower and upper bound entry boxes are filled with valid entries."
            )
        except KeyError as ke:
            print(ke)
            messagebox.showwarning("Warning", "Please check whether is the selected file valid FTIR data file.")
        except Exception as exc:
            print(exc)
            messagebox.showerror("Warning", "Something went wrong. Try again.")

    def __open_file_dialog(self) -> None:
        """Open file picker and set the texts in filenames entry box"""

        filepath = filedialog.askopenfilename(
            initialdir=".", title="Select file", filetypes=[("Text files", "*.csv")]  # type: ignore
        )

        self.filepath_str.set(filepath)  # save the path of selected data file.
        # set data file name to display in text box
        txtbox_str = filepath.split(sep)[-1]

        self.filemin_entry.configure(state=ctk.NORMAL)
        self.filemin_entry.delete(0, ctk.END)
        self.filemin_entry.insert(ctk.END, txtbox_str)
        self.filemin_entry.configure(state=ctk.DISABLED)
