import tkinter as tk
import main

book_inventory = tk.Tk()
book_inventory.title("Book Inventory")
book_inventory.geometry("640x580")
book_inventory.configure(bg="#E6E6E6", cursor="star")

book_entry_frame = tk.Frame(book_inventory, bg="#E6E6E6")
book_entry_frame.pack(pady=20)

book_display_frame = tk.Frame(book_inventory, bg="#E6E6E6")
book_display_frame.pack()

books_per_row = 3

def display_books(book_data):
    row = 0
    col = 0

    for key, book in book_data.items():
        book_frame = tk.Frame(
            book_display_frame,
            borderwidth=2,
            relief="ridge",
            bg="white",
            padx=10,
            pady=10
        )
        book_frame.grid(row=row, column=col, padx=10, pady=10, sticky="n")

        tk.Label(book_frame, text=book["title"], font=("Comic Sans MS", 12, "bold"), fg="black", bg="white").pack(anchor="w")
        tk.Label(book_frame, text=f"Author: {book['author']}", font=("Comic Sans MS", 10),  fg="black", bg="white").pack(anchor="w")
        tk.Label(book_frame, text=f"ISBN: {book['ISBN']}", font=("Comic Sans MS", 9),  fg="black", bg="white").pack(anchor="w")
        tk.Label(book_frame, text=f"Price: ${book['price']}", font=("Comic Sans MS", 10, "bold"),  fg="black", bg="white").pack(anchor="w")
        tk.Label(book_frame, text=f"Stock: {book['stock']}", font=("Comic Sans MS", 10),  fg="black", bg="white").pack(anchor="w")

        col += 1
        if col >= books_per_row:
            col = 0
            row += 1

display_books(main.book_data)

book_inventory.mainloop()
