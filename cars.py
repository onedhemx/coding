class Vehicle:
    def __init__(self, brand: str, model: str, year: int, mileage: float = 0):
        self.brand = brand
        self.model = model
        self.year = year
        self.mileage = mileage

    def drive(self, distance: float) -> None:
        if distance > 0:
            self.mileage += distance
        else:
            print("расстояние положительное число")

    def display_info(self) -> None:
        print(f"Марка: {self.brand}")
        print(f"Модель: {self.model}")
        print(f"Год выпуска: {self.year}")
        print(f"Пробег: {self.mileage} км")


class Car(Vehicle):
    def __init__(self, brand: str, model: str, year: int, fuel_type: str, mileage: float = 0):
        super().__init__(brand, model, year, mileage)
        self.fuel_type = fuel_type

    def display_info(self) -> None:
        super().display_info()
        print(f"тп топлива: {self.fuel_type}")


class Truck(Vehicle):
    def __init__(self, brand: str, model: str, year: int, max_load: float, mileage: float = 0, current_load: float = 0):
        super().__init__(brand, model, year, mileage)
        self.max_load = max_load
        self.current_load = current_load

    def load_cargo(self, weight: float) -> None:
        if weight <= 0:
            print("Весдолжен положительным")
            return
        if self.current_load + weight > self.max_load:
            print(f"максимум: {self.max_load} т.")
        else:
            self.current_load += weight
            print(f"груз загружен. Текущий груз: {self.current_load} т")

    def unload_cargo(self, weight: float) -> None:
        if weight <= 0:
            print("Вес должен положительным")
            return
        if self.current_load - weight < 0:
            print("Нельзя больше")
        else:
            self.current_load -= weight
            print(f"Груз разгружен. Текущий груз: {self.current_load} т")

    def display_info(self) -> None:
        super().display_info()
        print(f"Максимальная грузоподъемность: {self.max_load} т")
        print(f"Текущий груз: {self.current_load} т")
