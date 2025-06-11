class WeatherStation:
    def __init__(self):
        self.__temp = 0
        self.__humidity = 0
        self.observers = []

    def register_observer(self, observer):
        if observer not in self.observers:
            self.observers.append(observer)



    def unregister_observer(self, observer):
        if observer in self.observers:
            self.observers.remove(observer)


    def notify_observers(self):
        for observer in self.observers:
            observer.update(self.__temp, self.__humidity)

    def set_measurements(self, temp, humidity):
        self.__temp = temp
        self.__humidity = humidity
        self.notify_observers()