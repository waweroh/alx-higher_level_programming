#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    import sys

len = len(sys.argv) - 1

if len != 3:
    print("Usage: ./100-my_calculator.py <a> <operator> <b>")
    sys.exit(1)

oprnd = sys.argv[2]

if oprnd != "+" and oprnd != "-" and oprnd != "*" and oprnd != "/":
    print("Unknown operator. Available operators: +, -, * and /")
    sys.exit(1)

a = int(sys.argv[1])
b = int(sys.argv[3])

if oprnd == "+":
    print("{:d} + {:d} = {:d}".format(a, b, add(a, b)))
elif oprnd == "-":
    print("{:d} - {:d} = {:d}".format(a, b, sub(a, b)))
elif oprnd == "*":
    print("{:d} * {:d} = {:d}".format(a, b, mul(a, b)))
elif oprnd == "/":
    print("{:d} / {:d} = {:d}".format(a, b, div(a, b)))
