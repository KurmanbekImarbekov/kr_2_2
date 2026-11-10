class Animal:
    def __init__(self, name, age):
        self._name = name
        self._age = age

    @property
    def name(self):
        return self._name

    @property
    def age(self):
        return self._age

    @name.setter
    def name(self, new_name):
        if not new_name.strip():
            raise ValueError("Имя не может быть пустым!")

        self._name = new_name

    @age.setter
    def age(self, new_age):
        if new_age < 0:
            raise ValueError("Возраст не может быть отрицательным!")

        self._age = new_age

    def make_sound(self):
        pass


class Dog(Animal):
    def make_sound(self):
        return f"Собака: Гау!"

    def info(self):
        return f"Кличка: {self.name}\nВозраст: {self.age}"


class Cat(Animal):
    def make_sound(self):
        return f"Кошка: Мяу!"

    def info(self):
        return f"Кличка: {self.name}\nВозраст: {self.age}"


lessi = Dog("Lessi", 3)
mursik = Cat("Mursik", 5)

print(lessi.make_sound())
print(mursik.make_sound())

print(lessi.info())
print(mursik.info())


lessi.name = "Bobik"
mursik.age = 2
print(lessi.info())
print(mursik.info())
