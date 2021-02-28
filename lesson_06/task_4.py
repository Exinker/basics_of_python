
class Car():

    def __init__(self, speed, color, name, is_police=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def show_speed(self):
        print(f'speed: {self.speed}')

    def go(self):
        print('go')

    def stop(self):
        print('stop')

    def turn(self, direction):
        print(f'turn to {direction}')


class TownCar(Car):

    def show_speed(self):
        alert = '(reduce speed!)' if self.speed > 60 else ''
        print(f'speed: {self.speed} {alert}')


class WorkCar(Car):

    def show_speed(self):
        alert = '(reduce speed!)' if self.speed > 40 else ''
        print(f'speed: {self.speed} {alert}')


class PoliceCar(Car):

    def __init__(self, speed, color, name, is_police=True):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police


town_car = TownCar(60, 'black', 'town car')
town_car.turn('left')
town_car.show_speed()

work_car = WorkCar(43, 'yellow', 'hork car')
work_car.show_speed()

police_car = PoliceCar(143, 'blue', 'police car')
police_car.show_speed()
