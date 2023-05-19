class Country:
    def __init__(self, name: str, population: int, capital: str):
        self.name = name
        self.population = population
        self.capital = capital

    def increase_population(self, inc_number: int):
        self.population += inc_number

    def __str__(self):
        return f"{self.name} population is {self.population} and capital is {self.capital}"

    # Create add method to add two countries together
    def add(self, add_country):
        return Country(f"{self.name} {add_country.name}",
                       self.population + add_country.population,
                       self.capital)

    # Implementation previous task with magic method
    def __add__(self, add_country):
        return Country(f"{self.name} {add_country.name}",
                       self.population + add_country.population,
                       self.capital)


bosnia = Country('Bosnia', 10_000_000, "Sarajevo")
herzegovina = Country('Herzegovina', 5_000_000, "unknown")

bosnia_herzegovina = bosnia.add(herzegovina)
bosnia_herzegovina_magic = bosnia + herzegovina

assert str(bosnia_herzegovina) == str(bosnia_herzegovina_magic)


# Task 4 Create a Car class
class Car(object):
    def __init__(self, brand: str, model: str, year: int, speed: float):
        self.brand = brand
        self.model = model
        self.year = year
        self.speed = speed

    def accelerate(self):
        self.speed += 5

    def brake(self):
        self.speed -= 5


# Task 5 Create a robot class
class Robot:
    DIRECTIONS = ("North", "East", "South", "West")

    def __init__(self, orientation, position_x, position_y):
        self.orientation = orientation
        self.position_x = position_x
        self.position_y = position_y

    # Why in construction case I can't use tuple like self.DIRECTIONS[0]?
    def move(self, num_of_steps: int):
        match self.orientation:
            case "North":
                self.position_y += num_of_steps
            case "South":
                self.position_y -= num_of_steps
            case "East":
                self.position_x -= num_of_steps
            case "West":
                self.position_x += num_of_steps

    def turn(self, direction):
        current_direction_index = self.DIRECTIONS.index(self.orientation)
        if direction == "right":
            new_direction_index = (current_direction_index - 1) % len(self.DIRECTIONS)
        elif direction == "left":
            new_direction_index = (current_direction_index + 1) % len(self.DIRECTIONS)
        self.orientation = self.DIRECTIONS[new_direction_index]

    def display_position(self):
        print(f"x: {self.position_x}, y: {self.position_y}")


robot = Robot("North", 0, 0)
robot.move(3)
assert robot.position_x == 0 and robot.position_y == 3
robot.turn("right")
robot.move(2)
assert robot.position_x == 2 and robot.position_y == 3
robot.turn("left")
robot.move(1)
assert robot.position_x == 2 and robot.position_y == 4
