# TODO Написать 3 класса с документацией и аннотацией типов

import doctest


class Pet:
    def __init__(self, fluffy: bool, active: bool, cute: bool):
        """
        Создание и подготовка к работе объекта "Питомец"

        :param fluffy: пушистый ли питомец.
        :param active: активный ли питомец.
        :param cute: милый ли питомец.

        Примеры:
        >>> pet = Pet(True, True, False)  # инициализация экземпляра класса
        """

        if (not fluffy) and cute:
            raise ValueError("Не хочу не пушистых и не милых!")
        self.fluffy = fluffy
        self.active = active
        self.cute = cute

    def is_cute_boyfriend(self) -> bool:
        """
        Функция которая проверяет является ли питомец пушистым

        :return: Является ли питомец пушистым

        Пример:
        >>> pet = Pet(True, True, False)
        >>> pet.is_cute_boyfriend()
        """
        ...

    def cute_pet(self) -> None:
        """
        Делает питомца милым независимо от чужого мнения.)

        Примеры:
        >>> pet = Pet(True, False, False)
        >>> pet.cute_pet()
        """
        ...

    def is_pet_a_cat(self) -> bool:
        """
        Функция которая проверяет не котик ли питомец
        :return: Является ли питомец котиком

        Примеры:
        >>> pet = Pet(True, True, True)
        >>> pet.is_pet_a_cat()
        """
        ...


class Store:
    def __init__(self, number_of_shelves: int, number_of_goods: int):
        """
        Создание и подготовка к работе объекта "Магазин"
        :param number_of_shelves: Количество полок
        :param number_of_goods: Количество товаров
        Пример:
        >>> store = Store(200, 1500)  # инициализация экземпляра класса
        """
        if not isinstance(number_of_shelves, int):
            raise TypeError("Количество полок должно быть типом int")
        if number_of_shelves <= 0:
            raise ValueError("Количество полок должно быть положительным числом")
        self.number_of_shelves = number_of_shelves

        if not isinstance(number_of_goods, int):
            raise TypeError("Количество товаров должно быть типом int")
        if number_of_goods < 0:
            raise ValueError("Количество товаров не может быть отрицательным")
        self.number_of_goods = number_of_goods

    def is_empty_store(self) -> bool:
        """
        Функция которая проверяет есть ли в магазине товары

        :return: есть ли в магазине товары

        Пример:
        >>> store = Store(100, 0)
        >>> store.is_empty_store()
        """
        ...

    def add_goods_to_store(self, goods: int) -> None:
        """
        Завоз новых товаров в магазин.
        :param goods: Количество поступивших товаров

        Пример:
        >>> store = Store(100, 0)
        >>> store.add_goods_to_store(200)
        """
        if not isinstance(goods, int):
            raise TypeError("Количество товаров должно быть типом int")
        if goods < 0:
            raise ValueError("Количество поступивших товаров должно быть положительным")
        ...

    def writeoff_goods_from_store(self, number_of_writtenoff: int) -> None:
        """
        Списывание товаров.

        :param number_of_writtenoff: Количество списанных товаров
        :raise ValueError: Если количество списанных больше количества имеющихся в магазине
        товаров, то возвращается ошибка.

        Пример:
        >>> store = Store(100, 500)
        >>> store.writeoff_goods_from_store(200)
        """
        if not isinstance(number_of_writtenoff, int):
            raise TypeError("Количество товаров должно быть типом int")
        if number_of_writtenoff < 0:
            raise ValueError("Количество списанных товаров должно быть положительным")

        ...


class School:
    def __init__(self, number_of_subjects: int, number_of_classes: int):
        """
        Создание и подготовка к работе объекта "Школа"

        :param number_of_subjects: Количество предметов
        :param number_of_classes: Количество классов

        Пример:
        >>> school = School(10, 50)  # инициализация экземпляра класса
        """
        if not isinstance(number_of_subjects, int):
            raise TypeError("Количество предметов должно быть типа int")
        if number_of_subjects < 0:
            raise ValueError("Количество предметов не может быть отрицательным числом")
        self.number_of_subjects = number_of_subjects

        if not isinstance(number_of_classes, int):
            raise TypeError("Количество классов должно быть типа int")
        if number_of_classes < 0:
            raise ValueError("Количество классов не может быть отрицательным числом")
        self.number_of_classes = number_of_classes

    def add_subjects_to_schedule(self, subjects: int) -> None:
        """
        Появление новых предметов в расписании школы.
        :param subjects: Количество новых предметов

        Пример:
        >>> school = School(10, 50)
        >>> school.add_subjects_to_schedule(5)
        """
        if not isinstance(subjects, int):
            raise TypeError("Количество предметов должно быть типа int")
        if subjects < 0:
            raise ValueError("Количество новых предметов должно быть положительным числом")
        ...

    def add_new_class(self) -> None:
        """
        Функция, которая увеличивает количество классов на один

        Пример:
        >>> school = School(10, 50)
        >>> school.add_new_class()
        """
        ...


if __name__ == "__main__":
    doctest.testmod()  # тестирование примеров, которые находятся в документации

