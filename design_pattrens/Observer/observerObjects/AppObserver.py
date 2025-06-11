from design_pattrens.Observer.observerObjects.ObserverInterface import ObserverInterface


class AppObserver(ObserverInterface):

    def update(self, temp, humidity):
        print(f"AppObserver: Temperature is {temp}°C and Humidity is {humidity}%")