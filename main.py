import tkinter as tk
from tkinter import filedialog
#will crash on macOS / linux if try except is removed
try:
    from ctypes import windll, byref, sizeof, c_int
except:
    pass
import pandas as pd
import os

def print_csv_values():
    file_path = os.path.join(os.path.dirname(__file__), 'files', 'numbers.csv')
    if not os.path.exists(file_path):
        print("numbers.csv not found")
        return

    data = pd.read_csv(file_path)
    numeric_columns = data.select_dtypes(include=['number']).columns

    if len(numeric_columns) < 2:
        print("Not enough numeric columns in numbers.csv")
        return

    for x, y in zip(data[numeric_columns[0]], data[numeric_columns[1]]):
        print(f"x: {x}, y: {y}")

def main():
    #window initializeation
    root = tk.Tk()
    root.title("NASA Space App")
    root.iconbitmap("images/nasa.ico")
    root.geometry("960x540")
    root.resizable(0,0) #disable resizing
    
    color_pallet = ["#121212", "#171717", "#1C1C1C", "#252525", "#383838"]
    try:
        #get current window
        HWND = windll.user32.GetParent(root.winfo_id()) #get window handle from current open window (root)
        #https://learn.microsoft.com/en-us/windows/win32/api/dwmapi/ne-dwmapi-dwmwindowattribute
        windll.dwmapi.DwmSetWindowAttribute(HWND, 35, byref(c_int(0x00171717)), sizeof(c_int))
    except:
        pass
    
    root.configure(bg=color_pallet[0])

    #title text
    title_text = tk.Label(master=root, text="Seismic Detection-inator")
    title_text.pack()

    # Add Browse Files button
    browse_button = tk.Button(root, text="Analyze", command=print_csv_values)
    browse_button.pack(pady=20)

    #run
    root.mainloop()

if __name__ == "__main__":
    main()

    