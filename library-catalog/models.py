class Book:
    def __init__(self, title, author, isbn):
        """
        Initialize a Book object.
        
        :param self: Book object
        :param title: Title of the book
        :param author: Author of the book
        :param isbn: International Standard Book Number
        """
        self.title = title
        self.author = author
        self.isbn = isbn

    def __str__(self):
        """
        Return a human-readable string representation of the book.
        """

        return f"ISBN: {self.isbn} | Title: {self.title} | Author: {self.author}"
        
    

    
