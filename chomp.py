"""
Python reference implementation of the 4×n Chomp solver.

Slower than the C++ version but readable. Used for early verification
and for cross-checking small cases against the C++ output.

A position is a tuple (a, b, c, d) with a ≥ b ≥ c ≥ d ≥ 0, where each
coordinate is the number of remaining squares in that row. The terminal
P-position is (1, 0, 0, 0).

Usage:
    python3 chomp.py [max_n]   (default: 100)
"""

import csv
import sys
import time


def moves(a, b, c, d):
    for col in range(d):
        yield (a, b, c, col)
    for col in range(c):
        yield (a, b, col, min(d, col))
    for col in range(b):
        yield (a, col, min(c, col), min(d, col))
    for col in range(1, a):
        yield (col, min(b, col), min(c, col), min(d, col))


def tabulate(max_n):
    p_set  = {(1, 0, 0, 0)}
    p_list = [(1, 0, 0, 0)]
    t0 = time.time()

    for a in range(1, max_n + 1):
        count = 0
        for b in range(a + 1):
            for c in range(b + 1):
                for d in range(c + 1):
                    state = (a, b, c, d)
                    if state == (1, 0, 0, 0):
                        continue
                    if not any(m in p_set for m in moves(a, b, c, d)):
                        p_set.add(state)
                        p_list.append(state)
                        count += 1
        print(f"n={a}  new={count}  total={len(p_set)}  ({time.time()-t0:.1f}s)")

    return p_list


def export(p_list, filename):
    with open(filename, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["a", "b", "c", "d", "n"])
        for a, b, c, d in p_list:
            writer.writerow([a, b, c, d, a])


if __name__ == "__main__":
    max_n = int(sys.argv[1]) if len(sys.argv) > 1 else 100
    print(f"Tabulating 4×n Chomp P-positions for n ≤ {max_n}...")
    p_list = tabulate(max_n)
    export(p_list, "p_positions_4xn.csv")
    print(f"\nDone. {len(p_list):,} P-positions written to p_positions_4xn.csv")
