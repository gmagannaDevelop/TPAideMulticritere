import math


class Ride (object):
    def __init__(self, earlieststart, latestfinish, start, end, number):
        self.earlieststart = earlieststart
        self.latestfinish = latestfinish
        self.start = start
        self. end = end
        self.number = number

    @property
    def earlieststart(self):
        return self.__earlieststart

    @earlieststart.setter
    def earlieststart(self, earlieststart):
        self.__earlieststart = earlieststart

    @property
    def latestfinish(self):
        return self.__latestfinish

    @latestfinish.setter
    def latestfinish(self, latestfinish):
        self.__latestfinish = latestfinish

    @property
    def start(self):
        return self.__start

    @start.setter
    def start(self, start):
        self.__start = start

    @property
    def end(self):
        return self.__end

    @end.setter
    def end(self, end):
        self.__end = end

    @property
    def number(self):
        return self.__number

    @number.setter
    def number(self, number):
        self.__number = number

    def distanceto(self, vehicle):
        X=0
        Y=1
        distance = math.sqrt((vehicle.position[X]-self.start[X])**2 +
                             (vehicle.position[Y]-self.start[Y])**2)
        return distance

    def __repr__(self):
        return '[ride#{}: ({}, {}); ({}, {}); {}; {}]'.format(
            self.number, self.start[0], self.start[1], self.end[0], self.end[1],
            self.earlieststart, self.latestfinish
            )
