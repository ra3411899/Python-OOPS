# Python Object Oriented Programming by Joe Marini course example
# Using class-level and static methods


class Book:
    # TODO: Properties defined at the class level are shared by all instances
    BOOK_TYPES = ('HARDCOVER', 'PAPERBACK', 'EBOOK')
    # TODO: double-underscore properties are hidden from other classes
    __booklist = None

    # TODO: create a class method
    @classmethod
    def getBookTypes(cls):
        return cls.BOOK_TYPES
    # TODO: create a static method
    @staticmethod
    def getBookList():
        if Book.__booklist == None:
            Book.__booklist = []
        return Book.__booklist

    # instance methods receive a specific object instance as an argument
    # and operate on data specific to that object instance
    def setTitle(self, newtitle):
        self.title = newtitle
        

    def __init__(self, title, booktype):
        self.title = title
        if booktype not in Book.BOOK_TYPES:
            raise ValueError('{} is not a Valid Book Type'.format(booktype))
        else:
            self.booktype = booktype


# TODO: access the class attribute
print('Book Types are {}'.format(Book.getBookTypes()))

# TODO: Create some book instances
b1 = Book("Title 1", 'hardcover'.upper())
b2 = Book("Title 2", 'ebook'.upper())

# TODO: Use the static method to access a singleton object
thebookList = Book.getBookList()
thebookList.append(b1)
thebookList.append(b2)
print(thebookList)

