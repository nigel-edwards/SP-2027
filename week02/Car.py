

class Car:

    def __init__(self, colour, speed):
        self._colour = colour
        self._speed = speed

    @property
    def colour(self):
        return self._colour

    @property
    def speed(self):
        return self._speed

    def accelerate(self, increase_speed=10):
        self._speed += increase_speed

    def brake(self, decrease_speed=10):
        self._speed -= decrease_speed
        if self._speed < 0:
            self._speed = 0

    def __str__(self):
        return f"{self.colour} {self.speed}"


def main():
    car1 = Car("red", 100)
    car2 = Car("blue", 200)
    print (car1.colour)
    print (car2.colour)
    print (f"Car 1 speed before: {car1.speed}")
    car1.accelerate()
    print (f"Car 1 speed after : {car1.speed}")
    print (f"Car 2 Speed before: {car2.speed}")
    car2.accelerate(50)
    print (f"Car 2 speed after : {car2.speed}")
    car1.brake()
    car2.brake(2000)
    print (car1)
    print (car2)

if __name__ == "__main__":
    main()