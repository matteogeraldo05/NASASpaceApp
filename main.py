import tkinter as tk
from tkinter import ttk
import pandas as pd
import os
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.ticker import MultipleLocator

def main():
    def browse_file():
        file_path = os.path.join(os.path.dirname(__file__), 'numbers.csv')
        if file_path:
            df = pd.read_csv(file_path)
            text_widget.delete(1.0, tk.END)
            text_widget.insert(tk.END, df.to_string(index=False))
            plot_graph(df)

    def plot_graph(df):
        fig, ax = plt.subplots()
        df.plot(x='x', y='y', ax=ax)  # Use 'x' and 'y' as the column names
        ax.set_xlabel('x')  # Set x-axis label
        ax.set_ylabel('y')  # Set y-axis label
        ax.axhline(0, color='black', linewidth=0.5)  # Add horizontal line at y=0
        ax.axvline(0, color='black', linewidth=0.5)  # Add vertical line at x=0
        ax.xaxis.set_major_locator(MultipleLocator(10))  # Set x-axis ticks at intervals of 10
        ax.yaxis.set_major_locator(MultipleLocator(10))  # Set y-axis ticks at intervals of 10
        ax.set_xticks(df['x'])  # Set x-ticks to the values in the 'x' column
        ax.set_xticklabels(df['x'])  # Set x-tick labels to the values in the 'x' column
        canvas = FigureCanvasTkAgg(fig, master=root)
        canvas.draw()
        canvas.get_tk_widget().pack(expand=True, fill='both', pady=(0, 200))  # Add padding to move the graph up

    root = tk.Tk()
    style = ttk.Style()
    style.theme_use('clam')
    root.title("Basic GUI Window")
    root.geometry("1920x1080")
    root.configure(bg="#252526")

    browse_button = tk.Button(root, text="Browse Files", command=browse_file)
    browse_button.pack(pady=20)

    text_widget = tk.Text(root, wrap='none', bg="#1e1e1e", fg="white")
    text_widget.pack(expand=True, fill='both')

    root.mainloop()

if __name__ == "__main__":
    main()