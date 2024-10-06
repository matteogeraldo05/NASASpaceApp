import tkinter as tk


def main():
   

    root = tk.Tk()
    root.title("Basic GUI Window")
    root.geometry("1920x1080")  # Move 2 pixels to the left
    root.configure(bg="#252526")

    
    #run
    root.mainloop()

if __name__ == "__main__":
    main()