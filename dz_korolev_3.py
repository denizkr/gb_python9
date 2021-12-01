class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._incom = {'profit': wage, "bonus": bonus}


class Position(Worker):
    def get_full_name(self):
        return f"{self.name} {self.surname}"

    def get_full_profit(self):
        return f"{sum(self._incom.values())}"


manager = Position("Jim", 'Carrey', "Actor", 500000, 125000)
print(manager.get_full_name())
print(manager.position)
print(manager.get_full_profit())

print('Хороший человек :)')