"""
   In this program we can compare speed of vehicles
                                                   """


class Vehicle:
    """
       This class is created for represent and compare vehicles
                                                               """
    def __init__(self, name, brand, worth, speed):
        """
           We use this method for represent our variables
                                                         """
        self.name = name
        self.brand = brand
        self.worth = worth
        self.speed = speed

    def __gt__(self, other):
        """
           We use this method for compare speed of vehicles
                                                           """
        return self.speed > other.speed


vehicles = [
            Vehicle("car", "Toyota",  "30000$", 250),
            Vehicle("car", "Mercedes",  "45000$", 280),
            Vehicle("car", "BMW", "40000$", 300),
            Vehicle("bicycle", "Ardis",  "1200$", 45)
            ]

sorted_vehicles = sorted(vehicles, reverse=True)

for vehicle in sorted_vehicles:
    print(f"vehicle name - {vehicle.name}, vehicle brand - {vehicle.brand}, "
          f"vehicle worth - {vehicle.worth}, vehicle speed - {vehicle.speed}\n")
