import customtkinter as ctk


class Analysis:
    def __init__(self, master: ctk.CTkFrame) -> None:
        self.master = master

        ctk.CTkLabel(self.master, text="Select the data file which \n wants to find local minimum").grid(
            row=0, column=0
        )
        self.filemin_txt = ctk.CTkEntry(self.master, state=ctk.DISABLED)
        self.filemin_btn = ctk.CTkButton(self.master, text="Select Data file")
        ctk.CTkLabel(self.master, text="Enter the lower bound").grid(row=1, column=0)
        self.lower_bound_txt = ctk.CTkEntry(self.master)
        ctk.CTkLabel(self.master, text="Enter the upper bound").grid(row=2, column=0)
        self.upper_bound_txt = ctk.CTkEntry(self.master)
        ctk.CTkLabel(self.master, text="Minimum data point").grid(row=3, column=0)
        self.minimum_txt = ctk.CTkEntry(self.master, state=ctk.DISABLED)
        self.minimum_btn = ctk.CTkButton(self.master, text="Find Minimum")

        self.filemin_txt.grid(row=0, column=1)
        self.filemin_btn.grid(row=0, column=2)
        self.lower_bound_txt.grid(row=1, column=1)
        self.upper_bound_txt.grid(row=2, column=1)
        self.minimum_txt.grid(row=3, column=1)
        self.minimum_btn.grid(row=4, column=0)
