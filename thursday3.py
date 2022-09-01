books = {
    "In Our Time": "Ernest Hemingway",
    "A Farewell to Arms": "Ernest Hemingway",
    "For Whom the Bell Tolls": "Ernest Hemingway",
    "The Catcher in the Rye": "J. D. Salinger",
    "The Great Gatsby": "F. Scott Fitzgerald",
    "To Kill a Mockingbird": "Harper Lee",
    "Jane Eyre": "Charlotte Bronte"
}


def get_books_by_author(author):
    book_list = []
    for k, v in books.items():  # For each book in the dictionary
        if author.lower() == v.lower():  # check if its value is the selected author
            book_list.append(k)  # if so, add that book to the returned list

    book_list.sort() # Alphabetically sorts the returned list

    if len(book_list) > 0:
        print(f"The following books are by {author}:  {', '.join(book_list)}")
    else:
        print(f"We do not have any books by {author}.")


prompt = input("Please enter an author's name: ")
get_books_by_author(prompt)
