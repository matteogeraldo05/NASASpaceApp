import tkinter as tk
from ctypes import windll, byref, sizeof, c_int
import pandas

def main():
    #window initializeation
    root = tk.Tk()
    root.title("NASA Space App")
    root.iconbitmap("images/nasa.ico")
    root.geometry("960x540")
    root.resizable(0,0) #disable resizing
    
    color_pallet = ["#121212", "#171717", "#1C1C1C", "#252525", "#383838"]

    #get current window
    HWND = windll.user32.GetParent(root.winfo_id()) #get window handle from current open window (root)
    #https://learn.microsoft.com/en-us/windows/win32/api/dwmapi/ne-dwmapi-dwmwindowattribute
    windll.dwmapi.DwmSetWindowAttribute(HWND, 35, byref(c_int(0x00171717)), sizeof(c_int))
    root.configure(bg=color_pallet[0])

    
    #run
    root.mainloop()

if __name__ == "__main__":
    main()

  