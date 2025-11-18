# Superclass Vehicle
class Vehicle:
    def __init__(self, vehicle_type):
        self.vehicle_type = vehicle_type


# Subclass Automobile
class Automobile(Vehicle):
    def __init__(self, vehicle_type, year, make, model, doors, roof):
        super().__init__(vehicle_type)
        self.year = year
        self.make = make
        self.model = model
        self.doors = doors
        self.roof = roof


# Main app
def main():
    print("Enter the details for the car:\n")

    vehicle_type = "car"
    year = input("Enter year: ")
    make = input("Enter make: ")
    model = input("Enter model: ")
    doors = input("Enter number of doors (2 or 4): ")
    roof = input("Enter type of roof (solid or sun roof): ")

    # Automobile object
    car = Automobile(vehicle_type, year, make, model, doors, roof)

    print("\nHere is the car information:\n")
    print(f"  Vehicle type: {car.vehicle_type}")
    print(f"  Year: {car.year}")
    print(f"  Make: {car.make}")
    print(f"  Model: {car.model}")
    print(f"  Number of doors: {car.doors}")
    print(f"  Type of roof: {car.roof}")



if __name__ == "__main__":
    main()
