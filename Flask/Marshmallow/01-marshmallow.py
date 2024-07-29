# https://medium.com/@HeCanThink/marshmallow-a-sweet-python-library-for-object-serialization-and-deserialization-3001438b4708

from marshmallow import Schema, fields, post_load
class Book:
    def __init__(self, title, author, year_published):
        self.title = title
        self.author = author
        self.year_published = year_published

class BookSchema(Schema):
    title = fields.Str()
    author = fields.Str()
    year_published = fields.Int()

# Serializing a Book object to JSON:
book = Book(title="Sample Book", author="John Doe", year_published=2022)
book_schema = BookSchema()
serialized_book = book_schema.dump(book)
print(serialized_book)
print(type(serialized_book))

# Deserializing JSON data into a Book object:
json_data = {"title": "Another Book", "author": "Jane Smith", "year_published": 2021}       # dict
# json_data = '{"title": "Another Book", "author": "Jane Smith", "year_published": 2021}'   # error
book_schema = BookSchema()
deserialized_book = book_schema.load(json_data)
print(deserialized_book)
print(type(deserialized_book))
