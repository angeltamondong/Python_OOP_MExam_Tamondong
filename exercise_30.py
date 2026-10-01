class ReadingList:
    def __init__(self):
        self._books = []

    def add_book(self, title):
        if not title.strip():
            raise ValueError("Book title cannot be blank")
        self._books.append(title)

    def count(self):
        return len(self._books)

    def titles(self):
        return self._books.copy()


reading_list = ReadingList()
reading_list.add_book("Python Basics")
reading_list.add_book("OOP")

print(reading_list.count())

external = reading_list.titles()
external.pop()

print(len(external))
