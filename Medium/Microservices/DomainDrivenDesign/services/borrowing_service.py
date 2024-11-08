from entities.book import Loan

# services/borrowing_service.py
class BorrowingService:
    def __init__(self, book_repository, loan_repository):
        self.book_repository = book_repository
        self.loan_repository = loan_repository

    def borrow_book(self, isbn, member):
        book = self.book_repository.find_by_isbn(isbn)
        if book and book.available:
            book.mark_unavailable()
            loan = Loan(loan_id=1, book=book, member=member)  # loan_id should be generated
            self.loan_repository.add(loan)
            return loan
        else:
            raise Exception("Book is not available for loan")