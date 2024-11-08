# entities/book.py
class Book:
    def __init__(self, isbn, title, author):
        self.isbn = isbn
        self.title = title
        self.author = author
        self.available = True

    def mark_unavailable(self):
        self.available = False

    def mark_available(self):
        self.available = True

# entities/member.py
class Member:
    def __init__(self, member_id, name):
        self.member_id = member_id
        self.name = name

# aggregates/loan.py
from datetime import datetime, timedelta

class Loan:
    def __init__(self, loan_id, book, member):
        self.loan_id = loan_id
        self.book = book
        self.member = member
        self.due_date = datetime.now() + timedelta(days=14)  # 2-week loan period

    def return_book(self):
        self.book.mark_available()