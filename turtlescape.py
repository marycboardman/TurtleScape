# -*- coding: utf-8 -*-
"""
Created on Sun Feb 25 13:10:41 2018

@author: marycboardman
"""
import random


class turtle:
    """Creates a turtle object with turtle attributes and eats"""

    def __init__(self, wealth=0, metab=1, vision=1, age=0, maxage=10):
        self.wealth = wealth
        self.metab = metab
        self.age = age
        self.maxage = maxage
        self.vision = vision

    # Turtles eat sugar, add to wealth, then metabolize it
    def eat(self):
        sugar = random.randint(1, 4)
        sugar = self.vision * sugar
        self.wealth += sugar
        self.wealth -= self.metab

    # Turtles age 1 step for each model tick
    def grow_age(self):
        self.age += 1

    def print_wealth(self):
        print("Turtle wealth is ", self.wealth)

    def print_age(self):
        print("Turtle age is ", self.age)


class turtle_scape(turtle):
    """Creates a list of turtles and runs the model"""

    def __init__(self, turtles=[], turtle_wealth=[], wealth=0, metab=1,
                 vision=1, numturtle=1, age=0, maxage=10, birth=1,
                 maxruns=500):
        self.turtles = []
        self.turtle_wealth = []
        self.birth = birth
        self.maxruns = maxruns
        for t in range(numturtle):
            t = turtle(wealth, metab, vision, age, maxage)
            self.turtles.append(t)

    # Represents each tick of the model. Has each turtle eat, get older, and
    # kills off the ones with no wealth and/or too old through appending a
    # survivor list
    def tick(self):
        survivors = []
        for t in self.turtles:
            t.eat()
            t.grow_age()
            if (t.wealth > 0) and (t.age < t.maxage):
                survivors.append(t)
        for t in range(self.birth):
            t = turtle()
            survivors.append(t)
        self.turtles = survivors

    # Runs the model, feeds, ages, and kills the turtles. Then adds turtles
    # to the model according to birth. It then prints the output.
    def model(self):
        for i in range(self.maxruns):
            count = 0
            count += 1
            turtle_scape.tick(self)
        print("There are", len(self.turtles), "turtles")
        if len(self.turtles) == 0:
            print("Oh no! Your turtles are all dead!")
            print("They didn't even make it ", count, "runs!")
            print("Look at your dead turtle!")
            print("\|     |/")
            print("---------O")
            print("\______/")
            pass
        else:
            turtle_wealth = [t.wealth for t in self.turtles]
            w = sum(turtle_wealth)
            print("Total turtle wealth is", w)
            a = (w/len(self.turtles))
            print("Average turtle wealth is", a, "units of sugar per turtle.")


# Treats user input as global variables, then assigns them to the turtle,
# Turtle list, and model parameters
def user_input():
    # Minimum/maximum initial turtle wealth. This represents inheritance.
    global min_wealth
    global max_wealth
    global u_wealth
    # Minimum/maximum turtle metabolism. This represents the amount of sugar
    # consumed at each run of the model.
    global min_metab
    global max_metab
    global u_metab
    # Minimum/maximum turtle vision. This is a sugar multiplier, to simulate
    # the vision from original sugarscape. Instead of turtles looking around
    # for sugar, this gives a turtle a certain proportion (either less than
    # or greater than zero) of sugar at each run.
    global min_vision
    global max_vision
    global u_vision
    # Initial number of turtles in the model.
    global u_numturtle
    # Maximum age. Once a turtle reaches this, it dies.
    global u_maxage
    # Number of turtles added to the model at each tick.
    global u_birth
    # Maximum runs of a particular model run.
    global u_maxruns
    # Number of model runs in the simulation.
    global u_simulation
    # Input statements
    try:
        min_wealth = int(input("Enter minimum initial wealth: "))
        if min_wealth < 0:
            raise NegativeNumError("Max_wealth must be 0 or greater.")
            main()
        else:
            pass
    except IndexError:
        print("You need to enter in a value. Try again.")
        main()
    except ValueError:
            print("You need to inter the value as an integer. Try again.")
            main()
    try:
        max_wealth = int(input("Enter maximum initial wealth: "))
        if max_wealth < 0:
            raise NegativeNumError("Max_wealth must be 0 or greater.")
            main()
        else:
            pass
        if max_wealth < min_wealth:
            raise RangeError("Max_wealth must be at least min_wealth.")
            main()
        else:
            pass
    except IndexError:
            print("You need to enter in a value. Try again.")
            main()
    except ValueError:
            print("You need to inter the value as an integer. Try again.")
            main()
    try:
        min_metab = int(input("Enter minimum metabolism: "))
        if min_metab < 0:
            raise NegativeNumError("Min_metab must be 0 or greater.")
            main()
        else:
            pass
    except IndexError:
            print("You need to enter in a value. Try again.")
            main()
    except ValueError:
            print("You need to inter the value as an integer. Try again.")
            main()
    try:
        max_metab = int(input("Enter maximum metabolism: "))
        if max_metab < 1:
            raise PositiveNumError("Max_metab must be at least 1.")
            main()
        else:
            pass
        if max_metab < min_metab:
            raise RangeError("Max_wealth must be greater than min_wealth.")
            main()
        else:
            pass
    except IndexError:
            print("You need to enter in a value. Try again.")
            main()
    except ValueError:
            print("You need to inter the value as an integer. Try again.")
            main()
    try:
        min_vision = float(input("Enter minimum vision between 0 and 1: "))
        if min_vision < 0:
            raise NegativeNumError("Min_vision must be 0 or greater.")
            main()
        else:
            pass
        if min_vision >= 1:
            raise VisionError("Min_metab must be less than 1.")
            main()
        else:
            pass
    except IndexError:
            print("You need to enter in a value. Try again.")
            main()
    except ValueError:
            print("You need to inter the value as an float. Try again.")
            main()
    try:
        max_vision = float(input("Enter maximum vision between 1 and 2: "))
        if max_vision < 1:
            raise PositiveNumError("Max_vision must be at least 1.")
            main()
        else:
            pass
        if max_vision > 2:
            raise VisionError("Max_vision must be at least 1.")
            main()
        else:
            pass
    except IndexError:
            print("You need to enter in a value. Try again.")
            main()
    except ValueError:
            print("You need to inter the value as an float. Try again.")
            main()
    try:
        u_numturtle = int(input("Enter initial population: "))
        if u_numturtle < 1:
            raise PositiveNumError("U_numturtle must be at least 1.")
            main()
        else:
            pass
    except IndexError:
            print("You need to enter in a value. Try again.")
            main()
    except ValueError:
            print("You need to inter the value as an integer. Try again.")
            main()
    try:
        u_maxage = int(input("Enter turtle maximum age: "))
        if u_maxage < 1:
            raise PositiveNumError("U_maxage must be at least 1.")
            main()
        else:
            pass
    except IndexError:
            print("You need to enter in a value. Try again.")
            main()
    except ValueError:
            print("You need to inter the value as an integer. Try again.")
            main()
    try:
        u_birth = int(input("Enter turtle birth rate: "))
        if u_birth < 0:
            raise NegativeNumError("U_birth must be at least 0.")
            main()
        else:
            pass
    except IndexError:
            print("You need to enter in a value. Try again.")
            main()
    except ValueError:
            print("You need to inter the value as an integer. Try again.")
            main()
    try:
        u_maxruns = int(input("Enter maximum runs: "))
        if u_maxruns < 1:
            raise PositiveNumError("U_maxruns must be at least 1.")
            main()
        else:
            pass
    except IndexError:
            print("You need to enter in a value. Try again.")
            main()
    except ValueError:
            print("You need to inter the value as an integer. Try again.")
            main()
    try:
        u_simulation = int(input("Enter the number of simulations: "))
        if u_simulation < 1:
            raise PositiveNumError("U_simulation must be at least 1.")
            main()
        else:
            pass
    except IndexError:
            print("You need to enter in a value. Try again.")
            main()
    except ValueError:
            print("You need to inter the value as an integer. Try again.")
            main()


class RangeError(Exception):
    pass


class VisionError(Exception):
    pass


class NegativeNumError(Exception):
    pass


class PositiveNumError(Exception):
    pass


# Main method
def main():
    # Takes user input above, walks the user through inputting model
    # parameters
    user_input()
    # Takes the user input and creates a list of turtles with the following
    # model parameters
    # Wealth, metab, and vision is a random number between the min and max
    # provided by the user. This allows for turtles to have a uniformly
    # distributed set of attributes.
    turtworld = turtle_scape(wealth=random.randint(min_wealth, max_wealth),
                             metab=random.randint(min_metab, max_metab),
                             vision=random.uniform(min_vision, max_vision),
                             numturtle=u_numturtle,
                             maxage=u_maxage,
                             birth=u_birth,
                             maxruns=u_maxruns)
    # Runs the simulation for u_simulation number of times
    for s in range(u_simulation):
        turtworld.model()


# Initialization
if __name__ == "__main__":
    main()
else:
    print("This script is being used by another program")
