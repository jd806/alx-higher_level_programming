#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last_digit = int(str(number)[-1]) * (-1 if number < 0 else 1)
str = f"Last digit of {number:d} is {last_digit:d} and "
if last_digit == 0:
    str += 'is 0'
elif last_digit > 5:
    str += 'is greater than 5'
else:
    str += 'is less than 6 and not 0'
print(str)
