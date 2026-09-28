# The Book Class Module

class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn

    def __str__(self):
        return f"{self.title} by {self.author}, ISBN: {self.isbn}"

    def get_details(self):
        return (
            f"Title: {self.title}, "
            f"Author: {self.author}, "
            f"ISBN: {self.isbn}"
        )


sample_book = Book(
    "Harry Potter and the Sorcerer's Stone",
    "J.K. Rowling",
    "978-0439708180",
)

print(sample_book.get_details())