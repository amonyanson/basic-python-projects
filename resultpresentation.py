import tkinter as tk

def show_results(result):
    window = tk.Tk()
    window.title("Results")
    label = tk.Label(window, text=result)
    label.pack()
    window.mainloop()