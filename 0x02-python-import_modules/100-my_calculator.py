#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    import calculator_1 as calc

    if len(sys.argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    else:
        a = sys.argv[1]
        b = sys.argv[3]
        c = sys.argv[2]
        operators = ["+", "-", "*", "/"]
        if c not in operators:
            print("Unknown operator. Available operators: +, -, * and /")
            exit(1)
        if c == operators[0]:
            print("{} + {} = {}".format(a, b, calc.add(int(a), int(b))))
        elif c == operators[1]:
            print("{} - {} = {}".format(a, b, calc.sub(int(a), int(b))))
        elif c == operators[2]:
            print("{} * {} = {}".format(a, b, calc.mul(int(a), int(b))))
        elif c == operators[3]:
            print("{} / {} = {}".format(a, b, calc.div(int(a), int(b))))
