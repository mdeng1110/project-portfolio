from library import Library

library = Library()

count = library.load_books_from_csv("data/Books.csv")
print(f"{count} books loaded into the library.")
print(f"Total books in library: {len(library.isbn_index)}")
