class Book:
    def __init__(self, name, author):
        self._name = name
        self._author = author
    @property
    def name(self):
        return self._name
    @property
    def author(self):
        return self._author

    def __str__(self):
        return f"Название: {self.name}, Автор: {self.author}"

    def __repr__(self):
        return f"Book(name='{self.name}', author='{self.author}')"


class PaperBook(Book):
    def __init__(self, name, author, pages):
        super().__init__(name, author)
        self.pages = pages  # Используем сеттер pages
    @property
    def pages(self):
        return self._pages
    @page.setter
    def pages(self, value):
        if not isinstance(value, int):
            raise TypeError("Количество страниц должно быть целым числом")
        if value <= 0:
            raise ValueError("Количество страниц должно быть положительным числом")
        self._pages = value

    def __str__(self):
        return f"{super().__str__()}, Страницы: {self.pages}"

    def __repr__(self):
        return f"PaperBook(name='{self.name}', author='{self.author}', pages={self.pages})"


class AudioBook(Book):
    def __init__(self, name, author, duration):
        super().__init__(name, author)
        self.duration = duration  # Используем сеттер duration
    @property
    def duration(self):
        return self._duration
    @duration.setter
    def duration(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError("Продолжительность должна быть числом")
        if value <= 0:
            raise ValueError("Продолжительность должна быть положительной")
        self._duration = value

    def __str__(self):
        return f"{super().__str__()}, Продолжительность: {self.duration:.2f}"

    def __repr__(self):
        return f"AudioBook(name='{self.name}', author='{self.author}', duration={self.duration})"

# Пример использования
try:
    book = Book("Автостопом по галактике", "Дуглас Адамс")
    paper_book = PaperBook("1984", "Джордж Оруэлл", 328)
    audio_book = AudioBook("Властелин Колец", "Дж. Р. Р. Толкин", 54.5)

    print(book)
    print(repr(book))
    print(paper_book)
    print(repr(paper_book))
    print(audio_book)
    print(repr(audio_book))

    # Попытка изменить name (вызовет AttributeError)
    # book.name = "New Name"

    # Попытка присвоить неверное значение pages (вызовет исключение)
    # paper_book.pages = "abc"
    # paper_book.pages = -10

except (TypeError, ValueError) as e:
    print(f"Ошибка: {e}")
except AttributeError as e:
    print(f"Ошибка атрибута: {e}")