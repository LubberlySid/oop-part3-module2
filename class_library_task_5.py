"""
   In this program we represent books in our library
                                                    """


class Books:
    def __init__(self, name, author, year_of_publication):
        self.name = name
        self.author = author
        self.year_of_publication = year_of_publication

    def __str__(self):
        return f"Book: {self.name} by {self.author}, {self.year_of_publication} "


class Library:
    books = []
    """
       This class is created for represent our library
                                                      """

    def add_book(self, other):
        self.books.append(other)

    def __str__(self):
        book_list = "\n".join(str(book) for book in self.books)
        return f"Library books:\n{book_list}"


library = Library()

list_book = [
    Books("Harry Potter", "J.K. Rowling", "1997-2007"),
    Books("The MIDNIGHT LIBRARY", "Matt Haig", "13 August 2020"),
    Books("THE SILENT PATIENT", "Alex Michaelides", "5 February 2019")
]

for book in list_book:
    library.add_book(book)

print(library)
