import tkinter as tk
from time import strftime
def update_time():
    """Updates the time displayed on the clock label."""
    string_time = strftime('%H:%M:%S %p')  
    lbl.config(text=string_time)
    lbl.after(1000, update_time)  
root = tk.Tk()
root.title("Digital Clock")
lbl = tk.Label(root, font=('calibri', 40, 'bold'), background='black', foreground='white')
lbl.pack(anchor='center')
update_time()
root.mainloop()
