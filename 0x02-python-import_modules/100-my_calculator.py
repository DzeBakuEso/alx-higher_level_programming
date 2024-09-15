#!/usr/bin/python3


from calculator_1 import add, sub, mul, div
import sys


if __name__ != "__main__":
    exit()

if len(sys.argv) != 4:
    print("Usage: ./100-my_calculator.py <a> <operator> <b>")
    exit(1)

a = int(sys.argv[1])
operator = sys.argv[2]
b = int(sys.argv[3])

operations = {
    "+": add,
    "-": sub,
    "*": mul,
    "/": div
}

if operator not in operations:
    print("Unknown operator. Available operators: +, -, * and /")
    exit(1)

result = operations[operator](a, b)
print(f"{a} {operator} {b} = {result}")
