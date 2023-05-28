import customtkinter as ctk
from Graphs import Graphs
from Analysis import Analysis

ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")

# Create the main window
window = ctk.CTk()
window.geometry("550x275")
window.title("FTIR DATA PLOTER")

# Add tabview to the main window and nameing
tab_view = ctk.CTkTabview(window)
tab_1 = tab_view.add("Graphs")
tab_2 = tab_view.add("Analysis")

# Defining the elements in each tab
graphs = Graphs(tab_1)
analysis = Analysis(tab_2)

# UI configurations
fontconfig = ctk.CTkFont(size=13)

for widget in tab_1.winfo_children():
    widget_type = type(widget)
    if widget_type == ctk.CTkEntry:
        widget.grid_configure(pady=5)
    widget.configure(font=fontconfig)

for widget in tab_2.winfo_children():
    widget_type = type(widget)
    if widget_type == ctk.CTkLabel:
        widget.grid_configure(sticky=ctk.W, padx=15)
    if widget_type == ctk.CTkEntry:
        widget.grid_configure(padx=10, pady=3)
        widget.configure(width=300)
    if widget_type == ctk.CTkButton:
        if widget.winfo_name() == "!ctkbutton2":
            widget.grid_configure(sticky=ctk.E, padx=10)
        widget.grid_configure(pady=3)
    widget.configure(font=fontconfig)

tab_view.pack()
tab_view.pack()
window.mainloop()
