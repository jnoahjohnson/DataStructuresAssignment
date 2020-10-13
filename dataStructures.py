# Thomas Fife, Nathan Sonnenberg, Zach Daniels, Noah Johnson
# Description :
# You are the owner of a very successful hamburger restaurant. Your faithful customers line up every day and eat dozens of burgers.
# You are writing a program to track exactly how many hamburgers each customer eats.

# Imports
import random
import collections

# Code to get started


def randomName():
    asCustomers = ["Jefe", "El Guapo", "Lucky Day", "Ned Nederlander",
                   "Dusty Bottoms", "Harry Flugleman", "Carmen", "Invisible Swordsman",
                   "Singing Bush"]

    iRandomNum = random.randint(0, 8)

    return asCustomers[iRandomNum]


def randomBurgers():
    return random.randint(1, 20)


# Queue
burgerQueue = []

# Create Queue from randomName()
for num in range(0, 100):
    burgerQueue.append(randomName())

# Customers
customers = {}

# Create Customers from Quere
for person in burgerQueue:
    if person not in customers:
        customers[person] = 0

print(customers)
