
class Writable:

    def __init__(self, author: str, title: str, pages: int, time_to_read: int) -> set:
        self.author = author
        self.title = title
        self.pages = pages
        self.time_to_read = time_to_read

    def __str__(self):
        return f'Автор: {self.author}\nЗаголовок: {self.title}\nКоличество страниц:\
{self.pages}\nВремя чтения: {self.time_to_read}'

    def __getitem__(self, item):
        return self[item]

    def __iter__(self):
        return self

    def __getstate__(self):
        return [self.author, self.title, self.pages, self.time_to_read]




