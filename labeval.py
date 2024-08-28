class Library:
    def __init__(self):
        self.books = {}

    def add_book(self, title, author, isbn, genre, available=True):
        if isbn in self.books:
            print(f"Book with ISBN {isbn} already exists.")
            return
        self.books[isbn] = {
            'title': title,
            'author': author,
            'genre': genre,
            'available': available
        }

    def update_book_details(self, isbn, title=None, author=None, genre=None, available=None):
        if isbn not in self.books:
            print(f"Book with ISBN {isbn} not found.")
            return
        if title:
            self.books[isbn]['title'] = title
        if author:
            self.books[isbn]['author'] = author
        if genre:
            self.books[isbn]['genre'] = genre
        if available is not None:
            self.books[isbn]['available'] = available

    def search_by_isbn(self, isbn):
        return self.books.get(isbn, "Book not found.")

    def generate_genre_report(self):
        report = {}
        for book in self.books.values():
            if book['available']:
                genre = book['genre']
                if genre not in report:
                    report[genre] = []
                report[genre].append(book)
        return report

library = Library()
library.add_book("The Great Gatsby", "F. Scott Fitzgerald", "9780743273565", "Fiction")
library.add_book("1984", "George Orwell", "9780451524935", "Dystopian")
library.add_book("To Kill a Mockingbird", "Harper Lee", "9780061120084", "Fiction")

library.update_book_details("9780451524935", available=False)

print(library.search_by_isbn("9780743273565"))

print(library.generate_genre_report())
