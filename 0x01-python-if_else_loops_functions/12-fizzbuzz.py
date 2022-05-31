#!/usr/bin/python3
def fizzbuzz():
    print(' '.join(['FizzBuzz' if a % 3 == 0 and a %
                    5 == 0 else 'Fizz' if a % 3 == 0 else 'Buzz' if a %
                    5 == 0 else str(a) for a in range(1, 101)]), end=' ')
