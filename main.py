#test
import tkinter as tk
import subprocess

def main():
    def upload_to_git():
        subprocess.run(["git", "add", "/c:/Users/thoma/Testing/gui.py"])
        subprocess.run(["git", "commit", "-m", "Add GUI script"])
        subprocess.run(["git", "push"])

    upload_to_git()
    root = tk.Tk()
    root.title("Basic GUI Window")
    root.geometry("1920x1080")  # Move 2 pixels to the left
    root.configure(bg="#252526")

    root.mainloop()

if __name__ == "__main__":
    main()

  