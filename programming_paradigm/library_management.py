class Book:
    def __init__(self, title, author):
        self.title = title          # Public attribute
        self.author = author        # Public attribute
        self._is_checked_out = False  # Private attribute (_ indicates "internal use")

    def check_out(self):
        """Mark the book as checked out if it's available."""
        if not self._is_checked_out:
            self._is_checked_out = True
            return True
        return False

    def return_book(self):
        """Return the book to the library."""
        if self._is_checked_out:
            self._is_checked_out = False
            return True
        return False

    def is_available(self):
        """Check if the book is available."""
        return not self._is_checked_out


class Library:
    def __init__(self):
        self._books = []  # Private list to store Book instances

    def add_book(self, book):
        """Add a Book instance to the library."""
        if isinstance(book, Book):
            self._books.append(book)
            return True
        return False

    def check_out_book(self, title):
        """Check out a book by title if available."""
        for book in self._books:
            if book.title == title and book.is_available():
                book.check_out()
                return f"'{title}' has been checked out."
        return f"'{title}' is not available."

    def return_book(self, title):
        """Return a book by title."""
        for book in self._books:
            if book.title == title and not book.is_available():
                book.return_book()
                return f"'{title}' has been returned."
        return f"'{title}' was not checked out or does not exist."

    def list_available_books(self):
        """Return a list of titles of available books."""
        return [book.title for book in self._books if book.is_available()]


# Example Usage
if __name__ == "__main__":
    # Create books
    book1 = Book("1984", "George Orwell")
    book2 = Book("To Kill a Mockingbird", "Harper Lee")
    book3 = Book("Python 101", "Michael Driscoll")

    # Create library
    library = Library()
    library.add_book(book1)
    library.add_book(book2)
    library.add_book(book3)

    # Check available books
    print("Available books:", library.list_available_books())

    # Check out a book
    print(library.check_out_book("1984"))

    # Check available books after checkout
    print("Available books:", library.list_available_books())

    # Return a book
    print(library.return_book("1984"))

    # Check available books after returning
    print("Available books:", library.list_available_books())
