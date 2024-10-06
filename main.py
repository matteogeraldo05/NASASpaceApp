import tkinter as tk
import pandas

def main():
    #window initializeation
    root = tk.Tk()
    root.title("NASA Space App")
    root.iconbitmap("images/nasa.ico")
    root.state("zoomed") #start in windowed fullscreen
    root.resizable(0,0) #disable resizing
    root.configure(bg="#252526")

    #run
    root.mainloop()

if __name__ == "__main__":
    main()

  