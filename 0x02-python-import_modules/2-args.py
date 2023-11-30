#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    count = 0
    if len(sys.argv) == 1:
        print("{} arguments.".format(count))
    elif len(sys.argv) == 2:
        count = 1
        print("{} argument:".format(count))
        print("{}: {}".format(count, sys.argv[count]))
    else:
        count = len(sys.argv) - 1
        print("{} arguments:".format(count))
        j = 1
        while j < count + 1:
            print("{}: {}".format(j, sys.argv[j]))
            j += 1
