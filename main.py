import numpy as np
import tkinter as tk
import tkinter.filedialog as filedialog
import customtkinter
import pyglet
import pandas as pd
import os
from obspy import read
from datetime import datetime, timedelta
# this will crash on macOS / linux if try except is removed
try:
    from ctypes import windll, byref, sizeof, c_int
except:
    pass


# Global variable to store the file path
csv_file_path = None

def print_csv_values():
    global csv_file_path
    if not csv_file_path:
        print("No file selected. Please import a CSV file first.")
        return

    if not os.path.exists(csv_file_path):
        print("The selected file does not exist.")
        return

    data = pd.read_csv(csv_file_path)
    numeric_columns = data.select_dtypes(include=['number']).columns

    if len(numeric_columns) < 2:
        print("Not enough numeric columns in the selected CSV file")
        return

    for x, y in zip(data[numeric_columns[0]], data[numeric_columns[1]]):
        print(f"x: {x}, y: {y}")

def import_csv_values():
    global csv_file_path
    csv_file_path = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])
    if not csv_file_path:
        print("No file selected")
        return

    print(f"File selected: {csv_file_path}")

def main():
    # window initialization
    root = tk.Tk()
    root.title("NASA Space App")
    root.iconbitmap("images/nasa.ico")
    root.geometry("960x540")
    root.resizable(0, 0)  # disable resizing

    color_pallet = ["#FFFFFF", "#121212", "#171717", "#1C1C1C", "#252525", "#383838"]
    root.tk.call("font", "create", "Nasalization RG", "-family", "Nasalization RG")
    pyglet.font.add_file("fonts/nasalization-rg.otf")

    try:
        # get current window
        HWND = windll.user32.GetParent(root.winfo_id())  # get window handle from current open window (root)
        # https://learn.microsoft.com/en-us/windows/win32/api/dwmapi/ne-dwmapi-dwmwindowattribute
        windll.dwmapi.DwmSetWindowAttribute(HWND, 35, byref(c_int(0x00171717)), sizeof(c_int))
    except:
        pass

    root.configure(bg=color_pallet[1])

    # Title text
    title_text = tk.Label(master=root, text="Seismic Detection-inator", font=("Nasalization RG", 40), foreground=color_pallet[0], background=color_pallet[1])
    title_text.grid(row=0, column=0, columnspan=2, pady=(5, 5), sticky="nsew")

    # Configure grid weights for proper alignment
    root.grid_rowconfigure(0, weight=1)
    root.grid_columnconfigure(0, weight=1)
    root.grid_columnconfigure(1, weight=1)

    # Add Import CSV button
    import_button = customtkinter.CTkButton(root, text="IMPORT CSV", command=import_csv_values, width=100)
    import_button.configure(corner_radius=5, fg_color=color_pallet[3], hover_color=color_pallet[2], text_color=color_pallet[0], font=("Nasalization RG", 16))
    import_button.grid(row=1, column=0, padx=20, pady=5, sticky="ew") 

    # Add Analyze button
    browse_button = customtkinter.CTkButton(root, text="ANALYZE", command=print_csv_values, width=100) 
    browse_button.configure(corner_radius=5, fg_color=color_pallet[3], hover_color=color_pallet[2], text_color=color_pallet[0], font=("Nasalization RG", 16))
    browse_button.grid(row=1, column=1, padx=20, pady=5, sticky="ew")

    # Status label
    status_label = tk.Label(root, text="", fg="white", bg=color_pallet[1])
    status_label.grid(row=2, column=0, columnspan=2, pady=(5, 10), sticky="nsew") 

    def update_status_label():
        if not csv_file_path:
            status_label.config(text="No file selected. Please import a CSV file first.")
        else:
            status_label.config(text=f"File selected: {csv_file_path}")

    import_button.configure(command=lambda: [import_csv_values(), update_status_label()])
    browse_button.configure(command=lambda: [print_csv_values(), update_status_label()])


    # run
    root.mainloop()

if __name__ == "__main__":
    main()
