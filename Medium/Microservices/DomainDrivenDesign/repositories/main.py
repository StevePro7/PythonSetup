from entities.book import Book, Member
from repositories.book_repository import BookRepository
from repositories.book_repository import LoanRepository
from services.borrowing_service import BorrowingService

# Setup
book_repo = BookRepository()
loan_repo = LoanRepository()
borrowing_service = BorrowingService(book_repo, loan_repo)

# Add a book to the repository
book = Book(isbn="123456789", title="Domain-Driven Design", author="Eric Evans")
book_repo.add(book)

# Add a member
member = Member(member_id=1, name="Alice")

# Borrow the book
loan = borrowing_service.borrow_book(isbn="123456789", member=member)
print(f"Book '{loan.book.title}' borrowed by {loan.member.name} until {loan.due_date}")