
class Shape:
    """
    Абстрактный класс для фигуры
    >>> class Circle(Shape):
    ...     def __init__(self, radius):
    ...         self.radius = radius
    ...
    ...     def area(self):
    ...         return 3.14 * self.radius ** 2
    ...     def side_length(self):
    ...         return 3.14 * self.radius * 2
    ...
    >>> c = Circle(3)
    >>> c.area()
    28.26
    """

    def area(self):
        ...

    def side_length(self):
        ...

class Animal:
    """
    Животное
    """

    def eat(self) -> None:
        """
        Симулирует поедание еды
        :return: None
        """
        ...

    def sleep(self, time: int) -> None:
        """
        Симулирует сон

        :param time: Длительность сна в часах
        :return: None

        >>> a = Animal()
        >>> a.sleep(8)
        """
        ...


class Phone:
    """
    Телефон
    """

    def call(self, number: str) -> None:
        """
        Звонок по номеру

        :param number: Номер телефона
        :return: None

        >>> p = Phone()
        >>> p.call("+123456789")
        """
        ...

    def turn_on(self) -> None:
        """
        Включение телефона

        :return: None

        >>> p = Phone()
        >>> p.turn_on()
        """
        ...

    def open_site(self, url: str) -> None:
        """
        Открыть сайт

        :param url: Адрес сайта
        :return: None

        >>> p = Phone()
        >>> p.open_site("https://www.example.com")
        """
        ...
if __name__ == "__main__":
    # TODO работоспособность экземпляров класса проверить с помощью doctest
    import doctest
    doctest.testmod()
    pass
