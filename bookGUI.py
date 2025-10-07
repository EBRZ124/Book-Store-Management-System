import tkinter as tk
import main

book_inventory = tk.Tk()

book_inventory.title("Book Inventory")
book_inventory.geometry("640x580")
book_inventory.configure( bg="#E6E6E6", cursor="star")

book_entry_frame = tk.Frame(book_inventory, bg="#E6E6E6")
book_entry_frame.pack()

book_inventory.mainloop()