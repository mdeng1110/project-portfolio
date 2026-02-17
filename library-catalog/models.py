class Book:
    def __init__(self, title, author, ISBN):
        """
        Initialize a Book object.
        
        :param self: self
        :param title: Title of the book
        :param author: Author of the book
        :param ISBN: International Standard Book Number
        """
        self.title = title
        self.author = author
        self.isbn = ibsn

    def __str__(self):
        """
        Return a human-readable string representation of the book.
        """

        return f"ISBN: {self.isbn} | Title: {self.title} | Author: {self.author}"
        
    

    
