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

# Customers (dictionary)
dictCustomers = {}

# Iterate through queue
for iCount in range(0, len(burgerQueue)):
    # Variable to store customer at front of queue
    customerName = burgerQueue[0]

    # Check if customer has already been added and initialize if not
    if customerName not in dictCustomers:
        dictCustomers[customerName] = 0

    # Add burger count to customer
    dictCustomers[customerName] += randomBurgers()

    # Get rid of customer from queue
    burgerQueue.pop(0)


listSortedCustomers = sorted(
    dictCustomers.items(), key=lambda x: x[1], reverse=True)

# Print final list

for customer in listSortedCustomers:
    print(f'{customer[0].ljust(20)}{customer[1]}')
