import sys

from lost_cities.lost_cities import fib

if __name__ == "__main__":
    n = int(sys.argv[1])
    print(fib(n))
