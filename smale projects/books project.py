
books = [
    {"title": "lol", "name": "jore", "copies": 2},
    {"title": "rose", "name": "mame", "copies": 4},
    {"title": "rams", "name": "soso", "copies": 5},
    {"title": "rageing", "name": "kaka", "copies": 5},
    {"title": "masterbating", "name": "norah", "copies": 1}
]

def list_books():
    for b in books:
        print(f"{b['title']} - {b['name']} - copies: {b['copies']}")

def add_book(title, name, copies=1):
    if copies > 5:
        print("you can't add more than 5 copies")
        return

    exists = any(
        b["title"] == title and b["name"] == name
        for b in books
    )
    if exists:
        print("the book is already in the library")
        return

    books.append({"title": title, "name": name, "copies": copies})
    print("book added successfully")

def remove_book(title, name, copies=None):
    for b in books:
        if b["title"] == title and b["name"] == name:
            if copies is None or b["copies"] == copies:
                books.remove(b)
                print("book removed")
                return
            else:
                print("book found but copies number does not match")
                return
    print("the book does not exist")

a = int(input("1-show books ?\n2-add books ?\n3-remove books ?\n"))
if a == 1:
    list_books()
elif a == 2:
    x = input("title ?\n")
    y = input("name ?\n")
    z = int(input("copies ?\n"))
    add_book(x, y, z)
elif a == 3:
    o = input("title ?\n")
    oo = input("name ?\n")
    
    copies_input = input("copies ? (press enter to ignore)\n")
    if copies_input.strip() == "":
        remove_book(o, oo)
    else:
        remove_book(o, oo, int(copies_input))
else:
    print("error")