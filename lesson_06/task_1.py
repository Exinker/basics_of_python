
from time import sleep

class TrafficLight():

    colors = ['red', 'yellow', 'green']
    delays = [7, 2, 7]

    def __init__(self):
        self.__color = None

    def running(self):
        for color, delay in zip(TrafficLight.colors, TrafficLight.delays):
            self.__color = color
            print(self.__color)
            sleep(delay)


test = TrafficLight()
test.running()
