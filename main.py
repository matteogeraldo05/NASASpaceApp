import numpy as np
import tkinter as tk
import tkinter.filedialog as filedialog
import pyglet

# will crash on macOS / linux if try except is removed
try:
    from ctypes import windll, byref, sizeof, c_int
except:
    pass
import pandas as pd
import os

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

    # title text
    title_text = tk.Label(master=root, text="Seismic Detection-inator", font=("Nasalization RG", 40), foreground=color_pallet[0], background=color_pallet[1])
    title_text.pack()

     # Add Import CSV button
    import_button = tk.Button(root, text="Import CSV", command=import_csv_values)
    import_button.pack(pady=20)
    
    # Add Browse Files button
    browse_button = tk.Button(root, text="Analyze", command=print_csv_values)
    browse_button.pack(pady=20)


    # run
    root.mainloop()

if __name__ == "__main__":
    main()
