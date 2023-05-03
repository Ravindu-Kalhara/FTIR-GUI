import tkinter as tk
import pandas as pd
import matplotlib.pyplot as plt

# Create the main window
window = tk.Tk()

# Set the window title
window.title("CSV PLOTER")

# Create the label
label = tk.Label(window, text="Enter your filenames here (comma-separated):")

# Create the textbox
textbox = tk.Text(window, height=1, width=30)

# Create the buttons
def run_code():
    # Get the filenames from the textbox
    filenames = textbox.get("1.0", "end").strip().split(",")
    
    # Load the csv files into pandas dataframes
    dataframes = [pd.read_csv(filename.strip() + ".csv", skiprows=1) for filename in filenames]
    
    # Create a plot of the "cm-1" column of the first dataframe
    fig, ax = plt.subplots()
    dataframes[0].plot('cm-1', ax=ax)

    # Add the "cm-1" column of the other dataframes to the plot
    for dataframe in dataframes[1:]:
        dataframe.plot("cm-1", ax=ax)

    # Set the axis labels and title
    ax.set_xlabel("cm-1")
    ax.set_ylabel("%T")
    ax.set_title("CSV Files Combined Plot")

    # Add a legend
    ax.legend()

    # Display the plot
    plt.show()

button1 = tk.Button(window, text="Run Code", command=run_code)
button2 = tk.Button(window, text="Clear", command=lambda: textbox.delete('1.0', 'end'))
button3 = tk.Button(window, text="Close", command=window.destroy)

# Pack the label, textbox, and buttons in the window
label.pack()
textbox.pack()
button1.pack()
button2.pack()
button3.pack()

# Start the main loop
window.mainloop()
