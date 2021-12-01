class Stationery:

    def __init__(self, title="Что нибудь!"):
        self.title = title

    def draw(self):
        print(f"Просто рисуй! {self.title}")


class Pen(Stationery):
    def draw(self):
        print(f"Рисуй с руской! {self.title}")


class Pencil(Stationery):
    def draw(self):
        print(f"Рисуй с карандашом! {self.title}")


class Handle(Stationery):
    def draw(self):
        print(f"Рисуй с маркером! {self.title}")


stat = Stationery()
stat.draw()


mark = Handle()
peni = Pencil()
pen = Pen()


mark.draw()
peni.draw()
pen.draw()