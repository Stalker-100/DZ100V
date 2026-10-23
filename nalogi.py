class Property:      # класс РОДИТЕЛЬ
    """базовое имущество"""

    def __init__(self, worth):
        """сохраняет стоимость имущества."""
        self.__worth = worth

    @property
    def worth(self):
        """возвращает сумму"""
        return self.__worth

    @worth.setter
    def worth(self, value):
        """устанавливает стоимость, проверяя на отрицательность."""
        if value < 0:
            raise ValueError("Стоимость не может быть отрицательной")
        self.__worth = value

    def tax(self):
        """считает налог и переопределяется наследникам"""
        raise NotImplementedError("метод tax() должен быть переопределён")


class Apartment(Property):
    """Квартира. Налог = 1/1000."""

    def __init__(self, worth):
        super().__init__(worth)

    def tax(self):
        return self.worth / 1000


class Car(Property):
    """Машина. Налог = 1/200."""

    def __init__(self, worth):
        super().__init__(worth)

    def tax(self):
        return self.worth / 200


class CountryHouse(Property):
    """Дача. Налог = 1/500."""

    def __init__(self, worth):
        super().__init__(worth)

    def tax(self):
        return self.worth / 500


def create_property(kind, worth):
    """возвращает объект имущества по номеру типа 1/2/3"""
    classes = {1: Apartment, 2: Car, 3: CountryHouse}
    if kind not in classes:
        raise ValueError("Неизвестное имущество")
    return classes[kind](worth)


def main():
    """спрашивает данные, считает налог и выводит результат."""
    print("Тип имущества: 1 — квартира, 2 — машина, 3 — дача")
    kind = int(input("Введите номер типа имущества: "))
    worth = float(input("Введите стоимость имущества: "))
    money = float(input("Введите количество ваших денег: "))

    prop = create_property(kind, worth)
    tax = prop.tax()

    print(f"\nСтоимость имущества: {prop.worth}")
    print(f"Налог: {tax:.2f}")

    if money >= tax:
        print(f"Денег хватает. Остаток: {money - tax:.2f}")
    else:
        print(f"Не хватает: {tax - money:.2f}")


if __name__ == "__main__":
    main()