# Python Object Oriented Programming by Joe Marini course example
# Using the __str__ and __repr__ magic methods


class Book:
    def __init__(self, title, author, price):
        super().__init__()
        self.title = title
        self.author = author
        self.price = price

    # TODO: the __eq__ method checks for equality between two objects
    def __eq__(self, object) -> bool:
        if not isinstance(object, Book):
            raise ValueError('Cannot Compare')
        return (self.title == object.title and self.price == object.price and self.author == object.author)

    # TODO: the __ge__ establishes >= relationship with another obj

    def __ge__(self, object):
        if not isinstance(object, Book):
            raise ValueError('Cannot Compare')

        return (self.price >= object.price)

    # TODO: the __lt__ establishes < relationship with another obj
    def __lt__(self, object):
        if not isinstance(object, Book):
            raise ValueError('Cannot Compare')
        return (self.price <= object.price)


b1 = Book("War and Peace", "Leo Tolstoy", 39.95)
b2 = Book("The Catcher in the Rye", "JD Salinger", 29.95)
b3 = Book("War and Peace", "Leo Tolstoy", 39.95)
b4 = Book("To Kill a Mockingbird", "Harper Lee", 24.95)

# TODO: Check for equality
# print(b1 == b2)
# print(b1 == b3)

# TODO: Check for greater and lesser value
print(b1 >= b2)
print(b1 < b2)

# TODO: Now we can sort them too

books = [b4, b2, b1, b3]
sorted(books)
print([_.title for _ in books ]) 