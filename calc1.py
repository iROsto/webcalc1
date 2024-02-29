import sys


def make_int(n):
    try:
        return int(n)
    except ValueError:
        print(0)
        quit()

data = sys.argv[1:]
data = list(map(lambda x: make_int(x), data))
if len(data) != 2:
    print(0)
else:
    print(sum(data))
