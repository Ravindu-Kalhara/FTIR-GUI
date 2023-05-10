import customtkinter as ctk


class Analysis:
    def __init__(self, master: ctk.CTkFrame) -> None:
        """Class which defined for FTIR data analysis and to define all UI elements which are releated
        to FTIR data analysis.

        :param master: the master container widget for other UI elements are defined in Analysis class
        :type master: ctk.CTkFrame
        """

        self.master = master

        # Define all UI elements used in Analysis class. They are defined explicitly because with that, UI customization
        # become much eassy.
        self.filemin_lbl = ctk.CTkLabel(self.master, text="Select the data file which \n wants to find local minimum")
        self.filemin_txt = ctk.CTkEntry(self.master, state=ctk.DISABLED)
        self.filemin_btn = ctk.CTkButton(self.master, text="Select Data file")
        self.lower_bound_lbl = ctk.CTkLabel(self.master, text="Enter the lower bound")
        self.lower_bound_txt = ctk.CTkEntry(self.master)
        self.upper_bound_lbl = ctk.CTkLabel(self.master, text="Enter the upper bound")
        self.upper_bound_txt = ctk.CTkEntry(self.master)
        self.minimum_lbl = ctk.CTkLabel(self.master, text="Minimum data point")
        self.minimum_txt = ctk.CTkEntry(self.master, state=ctk.DISABLED)
        self.minimum_btn = ctk.CTkButton(self.master, text="Find Minimum")

        self.filemin_lbl.grid(row=0, column=0)
        self.filemin_txt.grid(row=0, column=1)
        self.filemin_btn.grid(row=0, column=2)
        self.lower_bound_lbl.grid(row=1, column=0)
        self.lower_bound_txt.grid(row=1, column=1)
        self.upper_bound_lbl.grid(row=2, column=0)
        self.upper_bound_txt.grid(row=2, column=1)
        self.minimum_lbl.grid(row=3, column=0)
        self.minimum_txt.grid(row=3, column=1)
        self.minimum_btn.grid(row=4, column=0)
