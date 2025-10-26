import tkinter as tk
import tkinter.messagebox
import main

book_inventory = tk.Tk()
book_inventory.title("Book Inventory")
book_inventory.geometry("740x580")
book_inventory.configure(bg="#E6E6E6", cursor="star")

book_entry_frame = tk.Frame(book_inventory, bg="#E6E6E6")
book_entry_frame.pack(pady=10)

book_entry_frame2 = tk.Frame(book_inventory, bg="#E6E6E6")
book_entry_frame2.pack(pady=10)

book_add_frame = tk.Frame(book_inventory, bg="#E6E6E6")
book_add_frame.pack(pady=10)

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

def show_title_search():
    def search_by_title():
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

    search_button = tk.Button(book_entry_frame, text="Search", command=search_by_title, bg="#CCCCCC")
    search_button.pack(side="left")

    reset_button = tk.Button(book_entry_frame,text="Reset", command=lambda: display_books(main.book_data), bg="#CCCCCC")
    reset_button.pack(side="left", padx=(5, 0))

def show_author_search():
    def search_by_author():
        query = search_entry.get().strip().lower()
        if not query:
            display_books(main.book_data)
            return

        filtered_books = {
            key: book for key, book in main.book_data.items()
            if query in book["author"].lower()
        }

        display_books(filtered_books)

    tk.Label(book_entry_frame2, text="Search Book Author:", fg="black", bg="#E6E6E6", font=("Comic Sans MS", 11, "bold")).pack(side="left", padx=(0, 5))

    search_entry = tk.Entry(book_entry_frame2, width=30)
    search_entry.pack(side="left", padx=(0, 10))

    search_button = tk.Button(book_entry_frame2, text="Search", command=search_by_author,bg="#CCCCCC")
    search_button.pack(side="left")

    reset_button = tk.Button(book_entry_frame2,text="Reset", command=lambda: display_books(main.book_data), bg="#CCCCCC")
    reset_button.pack(side="left", padx=(5, 0))

def show_add_button():
    add_button = tk.Button(book_add_frame, text="Add New Book", command=lambda: build_book_addition_screen(), bg="#B3E6B3")
    add_button.pack(side="left", padx=(10, 0))

def build_book_addition_screen():
    for widget in book_inventory.winfo_children():
        widget.destroy()

    add_frame=tk.Frame(book_inventory, bg="#E6E6E6")
    add_frame.pack(pady=20)

    tk.Label(add_frame, text = "Add a new book", bg="#E6E6E6", fg="black", font=("Comic Sans MS", 24, "bold")).grid(row=0, column=0, columnspan=2, pady=20)

    labels = ["title: ", "author: ", "ISBN: ", "Price: ", "Stock: "]
    entries = {}

    for i, field in enumerate(labels):
        tk.Label(add_frame, text=field, fg="black", bg="#E6E6E6", font=("Comic Sans MS", 10)).grid(row=i+1, column=0, sticky="e", pady=5, padx=5)
        entry = tk.Entry(add_frame, width=30, bg="#E6E6E6", fg="black")
        entry.grid(row=i+1, column=1, padx=10, pady=10)
        entries[field.replace(":", "").strip().lower()] = entry

    tk.Button(add_frame, text="Save Book", bg="#B3E6B3",
              command=lambda: save_new_book(entries)).grid(row=7, column=0, columnspan=2, pady=15)
    tk.Button(add_frame, text="Back", bg="#CCCCCC",
              command=lambda: back_button()).grid(row=8, column=0, columnspan=2, pady=5)

def save_new_book(entries):
    title = entries["title"].get().strip()
    author = entries["author"].get().strip()
    isbn = entries["isbn"].get().strip()
    price = entries["price"].get().strip()
    stock = entries["stock"].get().strip()

    if not all([title, author, isbn, price, stock]):
        tkinter.messagebox.showerror("Missing Field(s)", "Please fill out all of the fields")
        return
    
    try:
        isbn = int(isbn)
    except ValueError:
        tkinter.messagebox.showerror("Invalid ISBN", "ISBN must be a number")

    existing_isbn = [book["ISBN"] for book in main.book_data.values()]
    if isbn in existing_isbn:
        tkinter.messagebox.showerror("Duplicate ISBN", "This ISBN number already exists")
        return

    try:
        price = float(price)
        stock = int(stock)
    except ValueError:
        tkinter.messagebox.showerror("Invalid Input", "Price must be a number; Stock must be an integer.")
        return
    
    new_id = max(main.book_data.keys(), default=0) + 1
    main.book_data[new_id] = {
        "title": title,
        "author": author,
        "ISBN": isbn,
        "price": price,
        "stock": stock
    }

    tkinter.messagebox.showinfo("Successful entry", f"The book '{title}' has been successfully added to the library")

    for widget in book_inventory.winfo_children():
        widget.destroy()

    global book_entry_frame, book_display_frame
    book_entry_frame = tk.Frame(book_inventory, bg="#E6E6E6")
    book_entry_frame.pack(pady=10)

    global book_entry_frame2, book_display_frame
    book_entry_frame2 = tk.Frame(book_inventory, bg="#E6E6E6")
    book_entry_frame2.pack(pady=10)

    global book_add_frame, book_display_frame
    book_add_frame = tk.Frame(book_inventory, bg="#E6E6E6")
    book_add_frame.pack(pady=10)

    book_display_frame = tk.Frame(book_inventory, bg="#E6E6E6")
    book_display_frame.pack()

    display_books(main.book_data)
    show_title_search()
    show_author_search()
    show_add_button()

def back_button():
    for widget in book_inventory.winfo_children():
        widget.destroy()

    global book_entry_frame, book_display_frame
    book_entry_frame = tk.Frame(book_inventory, bg="#E6E6E6")
    book_entry_frame.pack(pady=10)

    global book_entry_frame2, book_display_frame
    book_entry_frame2 = tk.Frame(book_inventory, bg="#E6E6E6")
    book_entry_frame2.pack(pady=10)

    global book_add_frame, book_display_frame
    book_add_frame = tk.Frame(book_inventory, bg="#E6E6E6")
    book_add_frame.pack(pady=10)

    book_display_frame = tk.Frame(book_inventory, bg="#E6E6E6")
    book_display_frame.pack()

    display_books(main.book_data)
    show_title_search()
    show_author_search()
    show_add_button()

display_books(main.book_data)
show_title_search()
show_author_search()
show_add_button()
book_inventory.mainloop()
