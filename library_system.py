class Book:
    def __init__(self ,title ,author):
        self.title=title
        self.author=author
    def __str__(self):
        return f"Book:{self.title}{self.author}"
class EBook(Book):
    def __init__(self, title,author,file_size):
        super().__init__(title, author)
        self.file_size=file_size
    def __str__(self):
         return f"EBook:{self.title}{self.author}{self.file_size}"
class PrintBook(Book):
    def __init__(self,title,author,page_count):
        super().__init__(title,author)
        self.page_count=page_count
    def __str__(self):
        return f"PrintBook:{self.title}{self.author}{self.page_count}"
class Library: 
       def __init__(self): 
           self.books = [] 
       def add_book(self, book):
           if isinstance(book, Book): 
            self.books.append(book) 
           else: print("Invalid book type. Only Book, EBook, or PrintBook allowed.") 
       def list_books(self):
         for book in self.books: 
              print(book)
            #   : {book.title}, Author: {book.author}")
        #  if isinstance(book, EBook): 
        #       print(f"File Size: {book.file_size} MB") 
        #  elif isinstance(book, PrintBook): 
        #       print(f"Page Count: {book.page_count}")
