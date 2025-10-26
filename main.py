book_data = {
    1: {"title" : "1984", "author": "George Orwell", "ISBN" : 9780140817744, "price" : 20, "stock" : 13},
    2: {"title" : "Animal Far", "author": "George Orwell", "ISBN" : 9780194267533, "price" : 15, "stock" : 4},
    3: {"title" : "Three Comrades", "author" : "Erich Maria Remarque", "ISBN" : 9780449912423, "price" : 15, "stock" : 8},
    4: {"title" : "The Chamber", "author" : "Josh Grisham", "ISBN" : 12, "price" : 15, "stock" : 8}
}
"""
def add_book(book_data):
    new_id = max(book_data.keys()) + 1

    title = input("Enter the book's title: ")
    author = input("Enter the book's author: ")

    ISBN_checker = [book["ISBN"] for book in book_data.values()]
    while True:
        try:
            ISBN = int(input("Enter ISBN number: "))
            if ISBN in ISBN_checker:
                print("This ISBN already exists, enter a unique one.")
                continue
            break
        except ValueError:
            print("Please enter a valid number for ISBN.")

    while True:
        try:
            price = float(input("Enter price: $"))
            break
        except ValueError:
            print("Use a '.', not a ','")
    stock = int(input("Enter quantity/stock: "))

    book_data[new_id] = {
        "title": title,
        "author": author,
        "ISBN": ISBN,
        "price": price,
        "stock": stock
    }

    print("\nNew book and information added!")

add_book(book_data)

"""
