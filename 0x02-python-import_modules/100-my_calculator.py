#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    from calculator_1 import add, sub, mul, div
    args = sys.argv[1:]

    if len(args) != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    elif args[1] not in '+-/*':
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
    else:
        a, operator, b = args
        a = int(a)
        b = int(b)

        if operator == "+":
            print('{:d} + {:d} = {:d}'.format(a, b, add(a, b)))
        elif operator == "-":
            print('{:d} - {:d} = {:d}'.format(a, b, sub(a, b)))
        elif operator == "*":
            print('{:d} * {:d} = {:d}'.format(a, b, mul(a, b)))
        elif operator == "/":
            print('{:d} / {:d} = {:d}'.format(a, b, div(a, b)))
        exit(0)
