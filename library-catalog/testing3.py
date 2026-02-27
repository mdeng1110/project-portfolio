from library import Library
libby = Library()
libby.load_books_from_csv("data/Books.csv")

books = libby.find_by_author("Brett Slatkin")
for book in books:
    print(book)