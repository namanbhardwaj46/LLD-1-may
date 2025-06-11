from time import sleep

from design_pattrens.Observer.observerObjects.AppObserver import AppObserver
from design_pattrens.Observer.observerObjects.TvObserver import TvObserver
from design_pattrens.Observer.weatherStation import WeatherStation

if __name__=="__main__":
    ws = WeatherStation()

    tv1 = TvObserver()
    tv2 = TvObserver()

    ws.register_observer(tv1)
    ws.register_observer(tv2)

    App1 = AppObserver()
    App2 = AppObserver()

    ws.register_observer(App1)
    ws.register_observer(App2)

    sleep(30)
    ws.set_measurements(25, 60)

    sleep(10)
    print(" ---------  --------- ")

    ws.set_measurements(30, 70)

    sleep(15)

    ws.unregister_observer(tv1)

    print(" --------- Unregistering tv1 --------- ")

    ws.set_measurements(35, 80)

