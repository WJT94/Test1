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

while True:
    author_input = input("\nPlease enter an author's name: ")
    author_input = author_input.strip().lower()  # strip extra white space and convert the input to lowercase

    found_author = False
    for author, titles in books.items():  # Iterate on each author & title pair in the dict
        if author_input == author.strip().lower():  # if the author input is the same as the dict author
            found_author = True  # establish that the author was found.
            author_input = author  # edit the input to be an exact copy of how it's spelled in the dictionary
            break

    if found_author:
        book_list = books[author_input].copy()  # Creates a copy of the author's book list
        book_list.sort()  # Sorts the list in alphabetical order
        book_string = ", ".join(book_list)  # Conjoins the items of the list into a string
        print(f"The following books are by {author_input}:  {book_string}")
        break
    else:
        print(f"We do not have any books by {author_input}. Did you enter the name correctly?")