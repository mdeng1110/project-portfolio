from models import Book
from library import Library

library = Library()

book1 = Book("978-0135166307", "Effective Python", "Brett Slatkin")
book2 = Book("978-0135166307", "Effective Python", "Brett Slatkin")  # duplicate ISBN

library.add_book(book1)
library.add_book(book2)
