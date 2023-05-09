import customtkinter as ctk
from Graphs import Graphs
from Analysis import Analysis

ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")

# Create the main window
window = ctk.CTk()
window.title("FTIR DATA PLOTER")

# Add tabview to the main window and nameing
tab_view = ctk.CTkTabview(window)
tab_1 = tab_view.add("Graphs")
tab_2 = tab_view.add("Analysis")

# Defining the elements in each tab
graphs = Graphs(tab_1)
analysis = Analysis(tab_2)

tab_view.pack()
window.mainloop()
