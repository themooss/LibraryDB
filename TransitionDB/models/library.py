from models.magazine import Magazine
from models.manga import Manga


class Library:

    def __init__(self,):
        self.books = []
        self.magazines = []
        self.manga = []

    def __len__(self):
        return len(self.books)

    def __str__(self):
        return f'Книги: {self.books}\nЖурналы: {self.magazines}\nМанга: {self.manga}'

    def __iter__(self):
        return self
    def add_book_content(self, content: set):
        self.books.append(content)

    def add_magazine_content(self, content: Magazine):
        self.magazines.append(content.__getstate__())

    def add_manga_content(self, content: Manga):
        self.manga.append(content.__getstate__())

    def show_book_content(self):
        print(f'Книги: {self.books}')

    def show_magazine_content(self):
        print(f'Журналы: {self.magazines}')

    def show_manga_content(self):
        print(f'Манга: {self.manga}')

    def add_content(self, param):
        self.books.append(param)
