class Gadget:
    """
    Базовый класс для всех мобильных устройств.

    Attributes:
        make (str): Производитель мобильного устройства.
        year (int): Год выпуска мобильного устройства.
        model (str): Модель мобильного устройства.
    """

    def __init__(self, make: str, model: str, year: int) -> None:
        """
        Инициализирует объект Gadget.

        Args:
            make (str): Производитель мобильного устройства.
            year (int): Год выпуска мобильного устройства.
            model (str): Модель мобильного устройства.
        """
        self.make = make
        self.year = year
        self.model = model

    def __str__(self) -> str:
        """Возвращает строковое представление мобильного устройства."""
        return f"{self.year} {self.make} {self.model}"

    def __repr__(self) -> str:
        """Возвращает формальное строковое представление мобильного устройства."""
        return f"Vehicle(make='{self.make}', model='{self.model}', year={self.year})"


class Phone(Gadget):
    """
    Класс для смартфонов, наследуется от Gadget.

    Attributes:
        num_cores (int): Количество ядер смартфона.
    """

    def __init__(self, make: str, model: str, year: int, num_cores: int) -> None:
        """
        Инициализирует объект Phone, расширяя конструктор Gadget.

        Args:
            make (str): Производитель смартфона.
            model (str): Модель смартфона.
            year (int): Год выпуска смартфона.
            num_cores (int): Количество ядер смартфона.
        """
        super().__init__(make, model, year)
        self.num_cores = num_cores

    def __str__(self) -> str:
        """Возвращает строковое представление смартфона."""
        return f"{super().__str__()} with {self.num_cores} doors"

    def __repr__(self) -> str:
        """Возвращает формальное строковое представление смартфона."""
        return f"Car(make='{self.make}', model='{self.model}', year={self.year}, num_doors={self.num_cores})"

    def on(self) -> str:
        """
        Симулирует работу устройство.

        Returns:
            str: Сообщение о том, что устройство работает.
        """
        return f"{self.make} {self.model} is on."


class Tablet(Gadget):
    """
    Класс для планшетов, наследуется от Gadget.

    Attributes:
        load_capacity (float): Объем памяти планшета в гигабайтах.
    """
def __init__(self, make: str, model: str, year: int, load_capacity: float) -> None:
    """
    Инициализирует объект Tablet, расширяя конструктор Gadget.

    Args:
        make (str): Производитель планшета.
        model (str): Модель планшета.
        year (int): Год выпуска планшета.
        load_capacity (float): Объем памяти планшета в гигабайтах.
    """
    super().__init__(make, model, year)
    self._load_capacity = load_capacity  # Инкапсуляция атрибута, чтобы предотвратить его изменение извне.


def __str__(self) -> str:
    """Возвращает строковое представление планшета."""
    return f"{super().__str__()} with a load capacity of {self._load_capacity} gbytes"


def __repr__(self) -> str:
    """Возвращает формальное строковое представление планшета."""
    return f"Truck(make='{self.make}', model='{self.model}', year={self.year}, load_capacity={self._load_capacity})"


def load(self, weight: float) -> str:
    """
    Загружает файл на планшет, если вес меньше объема памяти.

    Args:
        weight (float): Вес файла.

    Returns:
        str: Сообщение о результате загрузки.

    Raises:
        ValueError: Если вес файла превышает объем памяти.
    """
    if weight > self._load_capacity:
        raise ValueError(f"Cannot load {weight} gbytes. Exceeds capacity of {self._load_capacity} gbytes.")
    return f"Loaded {weight} gbytes on the tablet."


if __name__ == "__main__":
    # Пример использования классов
    phone = Phone("Honor", "X9c", 2025, 8)
    print(phone)
    print(phone.on())

    tablet = Tablet("Xiaomi Redmi Pad", "SE", 2023, 128.0)
    print(tablet)
    print(tablet.load(15.0))
