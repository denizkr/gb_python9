class Cars:

    def __init__(self, name, color, speed, is_police=False):
        self.name = name
        self.color = color
        self.speed = speed
        self.is_police = is_police
        print(f"Автомобилы: {self.name} (Цвет {self.color}) {self.is_police}")

    def go(self):
        print(f"{self.name}: Машина начала движение")

    def turn(self):
        print(f"{self.name}: Машина повернула 'налево'")

    def show_speed(self):
        print(f"{self.name}: Скорость автомобиля {self.speed} км/час")

    def stop(self):
        print(f"{self.name}: Машина остановилась")





class WorkCar(Cars):

    def show_speed(self):
        return f"{self.name}: Скорость автомобиля - {self.speed} - ПРЕВЕШЕНИЕ СКОРОСТИ!!!" \
            if self.speed > 40 else f"{self.name}: Скорость автомобиля - {self.speed}"


class SportCar(Cars):
    def __init__(self, name, color, speed, SportCar=True):
        super().__init__(name, color, speed, SportCar)
        print(f"{self.name}: Скорость автомобиля - {self.speed} - ПРЕВЕШЕНИЕ СКОРОСТИ!!!" \
            if self.speed > 40 else f"{self.name}: Скорость автомобиля - {self.speed}")


class PoliceCar(Cars):
    def __init__(self, name, color, speed, is_police=True):
        super().__init__(name, color, speed, is_police)
        print(f"{self.name}: Скорость автомобиля - {self.speed} - ПРЕВЕШЕНИЕ СКОРОСТИ!!!" \
            if self.speed > 70 else f"{self.name}: Скорость автомобиля - {self.speed}")


police_car = PoliceCar('Полиция', 'Белый', 70)
police_car.go(), police_car.turn(), police_car.stop()
sportCar = SportCar('Запарожец', 'Красный', 170)
sportCar.go(),  sportCar.turn(), sportCar.stop()
