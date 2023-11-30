#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    sum = 0
    if len(sys.argv) == 1:
        print("0")
    elif len(sys.argv) > 1:
        j = 1
        while j < len(sys.argv):
            sum += int(sys.argv[j])
            j += 1
        print("{}".format(sum))
