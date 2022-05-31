#!/usr/bin/python3
import random
number = random.randint(-10, 10)
str = f"{number} is negative" if number < 0 else f"{number} is positive" if number > 0 else "0 is zero"
print(str)
