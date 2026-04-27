class Car:
    def __init__(self, brand: str, speed=0, fuel=100):
        self.brand = brand
        self.speed = speed
        self.fuel = fuel

    def accelerate(amount: int):
        Car.speed += amount

    def brake(amount: int):
        Car.speed -= amount
        if Car.speed < 0:
            Car.speed = 0
    
    def drive():
        if Car.speed > 0 and Car.fuel > 0:
            print("Car is driving")
            Car.fuel -= 10
        else:
            print("Car can't drive")


class Elevator:
    def __init__(self, current_floor=0, max_floor=10, working=True):
        self.current_floor = current_floor
        self.max_floor = max_floor
        self.working = working

    def go_up():
        if Elevator.current_floor < Elevator.max_floor:
            Elevator.current_floor += 1
    
    def go_down():
        if Elevator.current_floor > 0:
            Elevator.current_floor -= 1

    def use():
        if Elevator.working:
            print("that the elevator is working")
        else:
            print("that the elevator is out of service")


class Phone:
    def __init__(self, brand, battery=100, turned_on=False):
        self.brand = brand
        self.battery = battery
        self.turned_on = turned_on

    def turn_on():
        if Phone.battery > 0:
            Phone.turned_on = True

    def use_phone():
        if Phone.turned_on:
            Phone.battery -= 15
            print("that the phone is being used")
        else:
            print("that the phone is off")

    def charge():
        Phone.battery = 100


class Train:
    def __init__(self, name, speed=0, passengers=0):
        self.name = name
        self.speed = speed
        self.passengers = passengers

    def add_passengers(number):
        Train.passengers += number
    
    def start():
        if Train.passengers > 0:
            Train.speed = 50
            print("that the train started moving")
        else:
            print("that the train cannot start without passengers")

    def stop():
        Train.speed = 0


class Boat:
    def __init__(self, name, speed=0, fuel=50):
        self.name = name
        self.speed = speed
        self.fuel = fuel

    def add_fuel(amount):
        Boat.fuel += amount

    def sail():
        if Boat.fuel > 0 and Boat.speed > 0:
            print("that the boat is sailing")
            Boat.fuel -= 5
        else:
            print("that the boat cannot sail")

    def accelerate():
        Boat.speed += 10


car1 = Car("Audi")
car2 = Car("Mercedes", 40, 30)

car1.accelerate(5)
car1.brake(5)
car1.drive()

car2.accelerate(5)
car2.brake(5)
car2.drive()



elevator1 = Elevator(0, 5, False)
elevator2 = Elevator()

elevator1.go_down()
elevator1.go_up()
elevator1.use()

elevator2.go_down()
elevator2.go_up()
elevator2.use()


phone1 = Phone("apple", 50, True)
phone2 = Phone("samsung")

phone1.charge()
phone1.turn_on()
phone1.use_phone()

phone2.charge()
phone2.turn_on()
phone2.use_phone()


train1 = Train("Train A", 50, 20)
train2 = Train("Train B")

train1.add_passengers(5)
train1.start()
train1.stop()

train2.add_passengers(5)
train2.start()
train2.stop()


boat1 = Boat("Boat A", 30)
boat2 = Boat("Boat B", 0, 0)

boat1.accelerate(5)
boat1.add_fuel(5)
boat1.sail

boat2.accelerate(5)
boat2.add_fuel(5)
boat2.sail