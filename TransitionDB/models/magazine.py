from typing import override

from models.writable import Writable


class Magazine(Writable):

    def __init__(self, author: str, title: str, pages: int, time_to_read: int) -> object:
        super().__init__(author, title, pages, time_to_read)
        self.author = author
        self.title = title
        self.pages = pages
        self.time_to_read = time_to_read
