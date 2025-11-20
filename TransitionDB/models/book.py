from models.writable import Writable


class Book(Writable):

    def __init__(self, author, title, pages, time_to_read, cost):
        super().__init__(author, title, pages, time_to_read)
        self.author = author
        self.title = title
        self.pages = pages
        self.time_to_read = time_to_read
        self.cost = cost

    def __str__(self):
        return f'Автор: {self.author}\nЗаголовок: {self.title}\nКоличество страниц:\
{self.pages}\nВремя чтения: {self.time_to_read}\nСтоимость: {self.cost}'

