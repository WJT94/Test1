books = {
    "Ernest Hemingway": ["In Our Time", "A Farewell to Arms", "For Whom the Bell Tolls"],
    "J. D. Salinger": ["The Catcher in the Rye"],
    "F. Scott Fitzgerald": ["The Great Gatsby"],
    "Harper Lee": ["To Kill a Mockingbird"],
    "Charlotte Bronte": ["Jane Eyre"],
    "Margaret Atwood": ["The Handmaiden's Tale"],
    "J.R.R. Tolkien": ["The Hobbit"],
    "Roald Dahl": ["The Witches", "Charlie and the Chocolate Factory"]
}

author = input("\nPlease enter an author's name: ")
author.strip()

if author in books:
    book_list = books[author].copy()  # Creates a copy of the author's book list
    book_list.sort()  # Sorts the list in alphabetical order
    book_string = ", ".join(book_list)  # Conjoins the items of the list into a string
    print(f"The following books are by {author}:  {book_string}")
else:
    print(f"We do not have any books by {author}. Did you enter the name correctly?")
