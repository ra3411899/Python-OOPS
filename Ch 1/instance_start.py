# Python Object Oriented Programming by Joe Marini course example
# Using instance methods and attributes


class Book:
    # the "init" function is called when the instance is
    # created and ready to be initialized
    def __init__(self, title, author, pages, price):
        self.title = title
        # TODO: add properties
        self.author = author
        self.pages = pages
        self.price = price # instance Attribute - each to each instance that created
        self.__secret = 'This is the Secret'

    # TODO: create instance methods
    def getPrice(self):
        if hasattr(self, '_discount'):
            return self.price - (self.price * self._discount)
        else:
            return self.price

    def setDiscount(self, amount):
        self._discount = amount
        print(b2.__secret) # here It Will work


# TODO: create some book instances
b1 = Book("War and Peace", 'Leo Tolstoy', 1233, 39.99)
b2 = Book("The Catcher in the Rye", 'JD Salinger', 154, 6.99)

# TODO: print the price of book1
print('Price Of {0} is ${1:.2f}'.format(b1.title,b1.getPrice()))

# TODO: try setting the discount
print('Price of {} before Discount is {}'.format(b2.title, b2.getPrice()))
b2.setDiscount(0.25)
print('Price of {} After Discount is {:.2f}'.format(b2.title, b2.getPrice()))


# TODO: properties with double underscores are hidden by the interpreter
# print(b1.__secret) # TODO: throws an exception, cannot be seen outside of the class
print(b1._Book__secret) # HERE: Its works
