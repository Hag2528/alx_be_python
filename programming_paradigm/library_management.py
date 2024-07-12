class Book:
  def __init__(self, title, author):
    self.title = title
    self.author = author
    self._is_checked_out = False  # Private attribute for availability
  def check_out(self):
       self._is_checked_out = True

  def return_book(self):
      self._is_checked_out = False
  def is_available(self):
      return not self._is_checked_out
  def __str__(self):
      return f"{self.title} by {self.author}"

class Library:

  def __init__(self): 
   
    self._books = []

  def add_book(self, book):
   
    self._books.append(book)

  def check_out_book(self, title):
  
    for book in self._books:
      if book.title == title and book.is_available():
        book.check_out()
        print(f"{title} has been checked out.")
        return
    print(f"Sorry, '{title}' is not available or does not exist.")

  def return_book(self, title):
  
    for book in self._books:
      if book.title == title:
        book.return_book()
        print(f"{title} has been returned.")
        return
    print(f"Sorry, '{title}' is not checked out or does not exist.")

  def list_available_books(self):
     print("Available books:")
     for book in self._books:
      if book.is_available():
        print(book)