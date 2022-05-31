#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last_digit = int(str(number)[-1])
str = f"Last digit of {number:d} is {last_digit:d} and {'is 0' if last_digit == 0 else 'is greater than 5' if last_digit > 5 else 'is less than 6 and not 0'}"
print(str)
