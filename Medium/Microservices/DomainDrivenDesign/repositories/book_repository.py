# repositories/book_repository.py
class BookRepository:
    def __init__(self):
        self.books = {}

    def add(self, book):
        self.books[book.isbn] = book

    def find_by_isbn(self, isbn):
        return self.books.get(isbn)

# repositories/loan_repository.py
class LoanRepository:
    def __init__(self):
        self.loans = {}

    def add(self, loan):
        self.loans[loan.loan_id] = loan

    def find_by_id(self, loan_id):
        return self.loans.get(loan_id)