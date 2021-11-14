import datetime
import operator


class Book:
    items = []
    def __init__(self, title, published, author):
        self.title = title
        self.author = author
        self.published = published
        Book.items.append(self)

    def __str__(self):
        return f'{self.author}\'s {self.title}'

    @staticmethod
    def find_by_title(title):
        find_book = []
        for book in Book.items:
            if book.title.lower() == title.lower():
                find_book.append(book)
        return find_book

    @staticmethod
    def find_by_author(author):
        list_dook = []
        for book in Book.items:
            if author in book.author.split(' '):
                list_dook.append(book)
        return list_dook


    def __eq__(self, other):
        return self.title == other.title and self.author == other.author

    def __hash__(self):
        return hash((self.title, self.author))

    @staticmethod
    def published_after(year):
        list_book = []
        for book in Book.items:
            if book.published.year >= year:
                list_book.append(book)
        return list_book


class Movie:

    items = []
    def __init__(self, name, release_day, directed_by, based_on=None):
        self.name = name
        self.release_day = release_day
        self.directed_by = directed_by
        self.based_on = based_on
        Movie.items.append(self)

    def __str__(self):
        return f'{self.release_day}'

    @staticmethod
    def bubble_sort(array, field):
        n = len(array)
        for i in range(n - 1):
            for j in range(0, n - i - 1):
                if getattr(array[j], field) > \
                        getattr(array[j + 1], field):
                    array[j], array[j + 1] = array[j + 1], array[j]

    @staticmethod
    def sort_items():
        sort_items = Movie.items
        Movie.bubble_sort(Movie.items, 'release_day')
        return sort_items

    @staticmethod
    def for_book(books):
        list_mov = []
        for mov in Movie.items:
            if books in mov.based_on.title:
                list_mov.append(mov.based_on)
        return list_mov

    @property
    def recommendations(self):
        empty_list = []
        for movie in Movie.items:
            if self.based_on.title == movie.based_on.title:
                if movie != self:
                    empty_list.append(movie)
        return empty_list








#
# if __name__ == '__main__':

    # first_book = Book('Dune', datetime.date(1965, 8, 1), 'Frank Herbert')
    # first_movie = Movie('Dune', datetime.date(2021, 9, 3), 'Denis Villeneuve', first_book)
    # other_movie = Movie('Dune', datetime.date(1984, 12, 3), 'Raffaella De Laurentiis', first_book)
    # second_book = Book('The Lord of the Rings', datetime.date(1954, 7, 29), 'J. R. R. Tolkien')
    # second_movie = Movie('The Lord of the Rings', datetime.date(2001, 12, 10),
    #                      'Peter Jackson', second_book)
    # # print(first_book.published)
    # print(Movie.sort_items())
    # for i in Movie.sort_items():
    #     print(i)