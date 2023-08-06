#!/usr/bin/python3
"""N Queens"""
import sys


if __name__ == "__main__":
    """print N values"""
    args = sys.argv
    if len(args) < 2:
        print("Usage: nqueens N")
        sys.exit(1)

    N = int(sys.argv[1])
    if type(N) is not int:
        print("N must be a number")
        sys.exit(1)

    if N < 4:
        print("N must be a at least 4")
        sys.exit(1)

    count = 0
    outer = []
    row_incr = 0
    counter = 2
    prev_col = None
    while count < N - 2:
        row_incr += count
        for row in range(0, N):
            inner = []
            inner.append(row)
            row_incr += row + 1
            for col in range(row_incr, row_incr + 1):

                if row == 0:
                    inner.append(col)
                else:
                    x = outer[-1]
                    col = x[1]
                    col += counter
                    val = col % (N + 1)
                    inner.append(val)

            outer.append(inner)
        print(outer)
        row_incr = 0
        outer.clear()
        counter += 1
        count += 1
