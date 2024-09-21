import tkinter as tk
from tkinter import Menu

root = tk.Tk()
root.title("menu")
root.geometry("400x300")

menu_bar = Menu(root) # adds the menu bar

file_menu = Menu(menu_bar, tearoff=0) # adds the menu
file_menu.add_command(label="Exit", command=sys.exit) # adds the Exit option to the Options option (wth did i just write)

menu_bar.add_cascade(label="Options", menu=file_menu) # adds the "Options" option.

root.config(menu=menu_bar) # makes the menu bar work

root.mainloop()
