# Carpark
# Car
# Sensor
# Display
class CarPark:
    """
    Consolidates cars within a defined parking area (aka. carpark)
    """
    def __init__(self,
                 name,
                 location,
                 max_bays,
                 occupied = 0,
                 displays = None,
                 bays = None,
                 cars = None):
        self.temperature = self.update_temperature()
        self._car_count = 0 # TODO: read from config
        self._max_bays = 42 # ditto...
        # that's a lot of attributes!

    def update_temperature(self):
        '''Updates the temperature'''
        # TODO: implement
        return 42
    def get_car_park_status(self):
        print("providing status...")
        # TODO: provide status info

    def add_car(self, car):
        '''Adds a car to the carpark'''
        self._car_count += 1
        # self.car_count = self.car_count + 1
        # TODO: maybe I should build a list of cars...

    def remove_car(self, car):
        assert self._car_count > 0, "There should be cars for a car to be removed"
        self._car_count -= 1

    @property
    def is_full(self):
        return self._car_count >= self._max_bays


