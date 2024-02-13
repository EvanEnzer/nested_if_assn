# Part One

place = input("Choose a place: forest or cave?")

if place == "forest":
    action = input("climb a tree or cross a river?")
    if action == "climb a tree":
        print("You found a bird's nest!")
    elif action == "cross a river":
        print("You found a boat!")
    else:
        pass
elif place == "cave":
    action = input("Do you want to light a torch or continue in the dark?")
    if action == "light a torch":
        print("You find a hidden treasure!")
    elif action == "continue in the dark":
        print("You gain a stealth boost.")
    else: 
        pass
else: 
    pass

# Part Two

attendees = int(input("Enter number of attendees: "))
diet = input("Would you like the vegetarian option? (yes/no)")
venue = "large hall" if attendees > 100 else "conference room"
print(venue)
print("we prefer renting the DX5000 audio system for large halls") if venue == "large hall" else print("amplification not needed")
print("we prefer Veggie Delight Caterers") if diet == "yes" else print("we prefer Gourmet Meals Caterers")

# Part Three

try:
    number = float(input("enter a number"))
    x = number / 0
except ZeroDivisionError:
    pass
except ValueError:
    print("please  enter a numerical value")

import os

try:
    input_one = input("enter the filename")
    open (input_one)
except FileNotFoundError:
    pass

# Part Four

weather = input("Enter the weather: sunny, rainy, or cold: ")
if weather == "sunny": 
    clothing = "sunglasses" 
    shirt = ("short sleaves")
    accessory = ("scuba goggles")
elif weather == "rainy": 
    clothing = "umbrella"
    shirt = ("long sleaves")
    accessory = ("wet suit")
else:
   clothing = "sweater"
   shirt = ("undershirt")
   accessory = ("AirPods")
print(clothing)
print(shirt)
print(accessory)

# Part Five

import random

cpu_usage = random.randint(0, 100)
if cpu_usage > 90:
    print("High CPU usage!")
elif cpu_usage > 80 and cpu_usage <= 90:
    pass
memory_usage = random.randint(0, 100)
if memory_usage > 90:
    print("High RAM usage!")
elif memory_usage <= 90 and memory_usage >= 70:
    pass
disk_space = random.randint(0, 100)
if disk_space > 90:
    print("Low disk space!")
elif disk_space <= 90 and disk_space >= 70:
    pass