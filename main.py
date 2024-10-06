import tkinter
import customtkinter
import pygame
import os
import numpy
import pandas
from obspy import read
from datetime import datetime, timedelta
# !!DO NOT REMOVE THIS TRY STATMENT UNDER ANY CIRCUMSTANCE
try:
    from ctypes import windll, byref, sizeof, c_int
except:
    pass


# Global variable to store the file path
csv_file_path = None

#TODO make graph outa csv
def print_csv_values():
    global csv_file_path
    if not csv_file_path:
        print("No file selected. Please import a CSV file first.")
        return

    if not os.path.exists(csv_file_path):
        print("The selected file does not exist.")
        return

    data = pandas.read_csv(csv_file_path)
    numeric_columns = data.select_dtypes(include=['number']).columns

    if len(numeric_columns) < 2:
        print("Not enough numeric columns in the selected CSV file")
        return

    for x, y in zip(data[numeric_columns[0]], data[numeric_columns[1]]):
        print(f"x: {x}, y: {y}")
        
    #pygame.mixer.Sound("audio/zoom.wav").play()

#TODO make it import csv, run c++ file and use the spat out csv
def import_csv_values():
    global csv_file_path
    csv_file_path = tkinter.filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])
    if not csv_file_path:
        print("No file selected")
        return

    print(f"File selected: {csv_file_path}")

def main():
    # window initialization
    root = tkinter.Tk()
    root.title("NASA Space App")
    root.iconbitmap("images/nasa.ico")
    root.geometry("960x540")
    root.resizable(0, 0)  # disable resizing

    color_pallet = ["#FFFFFF", "#121212", "#171717", "#1C1C1C", "#252525", "#383838"]

    # Initialize Background Sound
    pygame.mixer.init()
    pygame.mixer.music.load("audio/background.wav") 
    pygame.mixer.music.set_volume(0.1)
    pygame.mixer.music.play(-1) 

    # !!AND THIS ONE TO, YEAH DON'T REMOVE IT
    try:
        # get current window
        HWND = windll.user32.GetParent(root.winfo_id())  # get window handle from current open window (root)
        # https://learn.microsoft.com/en-us/windows/win32/api/dwmapi/ne-dwmapi-dwmwindowattribute
        windll.dwmapi.DwmSetWindowAttribute(HWND, 35, byref(c_int(0x00171717)), sizeof(c_int))
    except:
        pass

    root.configure(bg=color_pallet[1])

    # Title text
    title_text = tkinter.Label(master=root, text="Seismic Detection-inator", font=("Nasalization RG", 40), foreground=color_pallet[0], background=color_pallet[1])
    title_text.grid(row=0, column=0, columnspan=3, pady=(20), sticky="n")  

    # Configure grid weights for proper alignment
    root.grid_rowconfigure(0, weight=1)
    root.grid_columnconfigure(0, weight=1)
    root.grid_columnconfigure(1, weight=2)
    root.grid_columnconfigure(2, weight=1)

    # Add Import CSV button
    import_button = customtkinter.CTkButton(root, text="IMPORT CSV", command=import_csv_values, width=100, height=50)
    import_button.configure(corner_radius=12, fg_color=color_pallet[3], hover_color=color_pallet[4], text_color=color_pallet[0], font=("Nasalization RG", 24))
    import_button.grid(row=1, column=0, padx=20, pady=5, sticky="ew") 

    # Add Analyze button
    browse_button = customtkinter.CTkButton(root, text="ANALYZE", command=print_csv_values, width=100, height=50) 
    browse_button.configure(corner_radius=12, fg_color=color_pallet[3], hover_color=color_pallet[4], text_color=color_pallet[0], font=("Nasalization RG", 24))
    browse_button.grid(row=1, column=2, padx=20, pady=5, sticky="ew") 

    # Status label
    status_label = tkinter.Label(root, text="", fg="white", bg=color_pallet[1])
    status_label.grid(row=2, column=0, columnspan=3, pady=(5, 10), sticky="nsew")

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