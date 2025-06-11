from design_pattrens.Observer.observerObjects.ObserverInterface import ObserverInterface


class TvObserver(ObserverInterface):

    def update(self, temp, humidity):
        print(f"TvObserver: Temperature is {temp}°C and Humidity is {humidity}%")