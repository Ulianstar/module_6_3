# Horse - класс описывающий Лошадь.
class Horse:
    def __init__(self, *args):
        self.x_distance = 0
        self.sound = 'Frrr'
        super().__init__(*args)

    # Метод run(self, dx) увеличивает x_distance на dx.
    def run(self, dx):
        self.x_distance += dx


# Eagle - класс описывающий Орла.
class Eagle:
    def __init__(self, *args):
        self.y_distance = 0
        self.sound = 'I train, eat, sleep, and repeat'
        super().__init__(*args)

    # Метод fly(self, dy) увеличивает y_distance на dy.
    def fly(self, dy):
        self.y_distance += dy


# Pegasus - класс описывающий пегаса. Наследуется от Horse и Eagle в том же порядке.
class Pegasus(Horse, Eagle):
    def __init__(self, *args):
        super().__init__(*args)

    # Метод move(self, dx, dy) - где dx и dy изменения дистанции.
    # Этот метод запускает наследованные методы run и fly соответственно.
    def move(self, dx, dy):
        self.run(dx)
        self.fly(dy)

    # Метод get_pos(self) возвращает текущее положение пегаса в виде кортежа -
    # (x_distance, y_distance) в том же порядке.
    def get_pos(self):
        return self.x_distance, self.y_distance

    # Метод voice - печатает значение унаследованного атрибута sound.
    def voice(self):
        print(self.sound)


# Вывод перемещения Пегаса.
p1 = Pegasus()

print(p1.get_pos())
p1.move(10, 15)
print(p1.get_pos())
p1.move(-5, 20)
print(p1.get_pos())

# Вывод: 'I train, eat, sleep, and repeat'
p1.voice()