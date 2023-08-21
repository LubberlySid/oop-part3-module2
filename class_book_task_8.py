"""
   In this program we represent a list of books
                                               """


class Book:
    year = 2023
    
    def __init__(self, title, author, pages_number, year):
        self.title = title
        self.author = author
        self.pages_number = pages_number
        self.year = year

    @staticmethod
    def count_book_publ_in_this_year(books, target_year):
        count = 0
        for book in books:
            if book.year == target_year:
                count += 1

        return count


books = [
        Book("Harry Potter", "J.K. Rowling", 900,  2007),
        Book("The MIDNIGHT LIBRARY", "Matt Haig", 300, 2020)
]

target_year = int(input("Введіть рік: "))

count = Book.count_book_publ_in_this_year(books, target_year)
print(f"Кількість книжок, опублікованих у {target_year} році: {count}")

