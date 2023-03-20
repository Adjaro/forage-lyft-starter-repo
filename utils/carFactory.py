from model.battery.nubbin import Nubbin
from model.battery.spindler import Spindler
from car import Car
from model.engine.capulet  import Capulet
from model.engine.sternman import Sternman
from model.engine.willoughby  import Willoughby
from model.tires.carrigan  import Carrigan
from model.tires.octoprime  import Octoprime

class CarFactory:
    @staticmethod
    def create_calliope(current_date, last_service_date, current_mileage, last_service_mileage, tire_wear):
        engine = Capulet (current_mileage, last_service_mileage)
        battery = Spindler(current_date, last_service_date)
        tires = Carrigan(tire_wear)
        car = Car(engine, battery, tires)
        return car

    @staticmethod
    def create_glissade(current_date, last_service_date, current_mileage, last_service_mileage, tire_wear):
        engine = Willoughby (current_mileage, last_service_mileage)
        battery = Spindler (current_date, last_service_date)
        tires = Octoprime (tire_wear)
        car = Car(engine, battery, tires)
        return car

    @staticmethod
    def create_palindrome(current_date, last_service_date, warning_light_is_on, tire_wear):
        engine = Sternman (warning_light_is_on)
        battery = Spindler (current_date, last_service_date)
        tires = Carrigan (tire_wear)
        car = Car(engine, battery, tires)
        return car

    @staticmethod
    def create_rorschach(current_date, last_service_date, current_mileage, last_service_mileage, tire_wear):
        engine = Willoughby (current_mileage, last_service_mileage)
        battery = Nubbin (current_date, last_service_date)
        tires = Octoprime (tire_wear)
        car = Car(engine, battery, tires)
        return car

    @staticmethod
    def create_thovex(current_date, last_service_date, current_mileage, last_service_mileage, tire_wear):
        engine = Capulet (current_mileage, last_service_mileage)
        battery = Nubbin (current_date, last_service_date)
        tires = Carrigan (tire_wear)
        car = Car(engine, battery, tires)
        return car