import tkinter as tk
import tkinter.messagebox
import main

book_inventory = tk.Tk()
book_inventory.title("Book Inventory")
book_inventory.geometry("640x580")
book_inventory.configure(bg="#E6E6E6", cursor="star")

book_entry_frame = tk.Frame(book_inventory, bg="#E6E6E6")
book_entry_frame.pack(pady=10)

book_display_frame = tk.Frame(book_inventory, bg="#E6E6E6")
book_display_frame.pack()

books_per_row = 3

def delete_book(book_key):
    if book_key in main.book_data:
        del main.book_data[book_key]
        display_books(main.book_data)

        tkinter.messagebox.showinfo("Alert!", "Book successfully deleted")


def display_books(book_data):
    for widget in book_display_frame.winfo_children():
        widget.destroy()

    row, col = 0, 0
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
        tk.Label(book_frame, text=f"Author: {book['author']}", font=("Comic Sans MS", 10), fg="black", bg="white").pack(anchor="w")
        tk.Label(book_frame, text=f"ISBN: {book['ISBN']}", font=("Comic Sans MS", 9), fg="black", bg="white").pack(anchor="w")
        tk.Label(book_frame, text=f"Price: ${book['price']}", font=("Comic Sans MS", 10, "bold"), fg="black", bg="white").pack(anchor="w")
        tk.Label(book_frame, text=f"Stock: {book['stock']}", font=("Comic Sans MS", 10), bg="white").pack(anchor="w")
        delete = tk.Button(book_frame, text = "Delete Book", font=("Comic Sans MS", 8), bg="#FFCCCC", command=lambda k=key: delete_book(k)).pack(anchor="w")

        col += 1
        if col >= books_per_row:
            col = 0
            row += 1


def search_books():
    query = search_entry.get().strip().lower()
    if not query:
        display_books(main.book_data)
        return

    filtered_books = {
        key: book for key, book in main.book_data.items()
        if query in book["title"].lower()
    }

    display_books(filtered_books)


tk.Label(book_entry_frame, text="Search Book Title:", fg="black", bg="#E6E6E6", font=("Comic Sans MS", 11, "bold")).pack(side="left", padx=(0, 5))

search_entry = tk.Entry(book_entry_frame, width=30)
search_entry.pack(side="left", padx=(0, 10))

search_button = tk.Button(book_entry_frame, text="Search", command=search_books,bg="#CCCCCC")
search_button.pack(side="left")

reset_button = tk.Button(book_entry_frame,text="Reset", command=lambda: display_books(main.book_data), bg="#CCCCCC")
reset_button.pack(side="left", padx=(5, 0))

display_books(main.book_data)

book_inventory.mainloop()
