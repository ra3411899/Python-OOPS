# Python Object Oriented Programming by Joe Marini course example
# Using composition to build complex objects


class Book:
    def __init__(self, title, price, auth):
        self.title = title
        self.price = price

        self.auth = auth

        self.chapters = []

    def addchapter(self, chapters):
        self.chapters.append((chapters))

    def getPagesCount(self):
        result = 0
        for ch in self.chapters:
            result += ch.pages
        return result

class Author:
    def __init__(self, fname,  lname):
        self.fname = fname
        self.lname = lname

    def __str__(self) -> str:
        return f"{self.fname} {self.lname}"

class Chapters:
    def __init__(self, chapter_name, pages):
        self.chapter_name = chapter_name
        self.pages = pages



auth = Author("Leo", "Tolstoy")

b1 = Book("War and Peace", 39.0, auth)

b1.addchapter(Chapters("Chapter 1", 125))
b1.addchapter(Chapters("Chapter 2", 97))
b1.addchapter(Chapters("Chapter 3", 143))

print(b1.auth)
print(b1.getPagesCount())
