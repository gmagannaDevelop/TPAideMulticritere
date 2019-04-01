class Vehicle(object):
    def __init__(self, position):
        self.position = position
        self.__rides = None

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, position):
        self.__position = position

    def add_ride(self, ride):
        if self.__rides:
            self.__rides = [ride]
        else:
            self.__rides.append(ride)

    def show_rides_list(self):
        return self.__rides
