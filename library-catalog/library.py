from models import Book
import csv
import os

class TrieNode:
    def __init__(self):
        self.children = {}
        self.books = []
        self.is_end = False

class Library:
    def __init__(self):
        """
        Initialize the library with an empty ISBN index.
        """
        self.isbn_index = {}

    def add_book(self, book):
        if book.isbn in self.isbn_index:
            return False

        # ISBN index
        self.isbn_index[book.isbn] = book

        # Author index
        if book.author not in self.author_index:
            self.author_index[book.author] = []
        self.author_index[book.author].append(book)

        # Title Trie
        self._insert_title(book.title, book)

        return True
    
    def _insert_title(self, title, book):
        """
        Insert a title into the Trie, handling spaces and special characters.
        """
        node = self.title_trie

        # Normalize for consistent searching
        normalized_title = title.lower()

        for char in normalized_title:
            # char may be a letter, space, number, or punctuation
            if char not in node.children:
                node.children[char] = TrieNode()

            node = node.children[char]

        node.is_end = True
        node.books.append(book)
    
    def update_book(self, isbn, title=None, author=None):
        """
        Update an existing book's title and or author.
        
        :param isbn: str - ISBN of the book to update
        :param title: str | None
        :param author: str | None
        :return: bool - True if updated, False if not found
        """
        try:
            book = self.isbn_index[isbn]

            if title is not None:
                book.title = title

            if author is not None:
                book.author = author

            return True
        
        except KeyError:
            print(f"Update failed: ISBN 'isbn' not found.")
            return False
    
    def delete_book(self, isbn):
        """
        Delete a book from the library by ISBN
        
        :param isbn: str
        :return: bool - True if deleted, False if not found
        """
        try:
            del self.isbn_index[isbn]
            return True
        
        except KeyError:
            print(f"Delete failed: ISBN '{isbn}' not found.")
            return False
    
    def load_books_from_csv(self, file_path):
        """
        Load books from a CSV file and add them to the library.
        
        :param file_path: str - path to CSV file
        :return: int - number of books successfully added
        """
        added_count = 0

        with open(file_path, newline="", encoding="utf-8") as csvfile:
            reader = csv.DictReader(csvfile)

            for row in reader:
                try:
                    isbn = row["ISBN"].strip()
                    title = row["Book-Title"].strip()
                    author = row["Book-Author"].strip()

                    book = Book(isbn, title, author)

                    if self.add_book(book):
                        added_count += 1

                except KeyError as e:
                    print(f"Skipping row due to missing/malformed field: {e}")

        return added_count