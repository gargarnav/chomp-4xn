"""
Verify the 4×n Chomp solver output against two known ground truths:
  1. The 2×n subcase: P-positions with c = d = 0 must be exactly (a, a-1, 0, 0).
  2. The 3×n subcase: P-positions with d = 0 must match an independent solver.

Usage:
    python3 verify.py [csv_file]   (default: p_positions_4xn_cpp_500.csv)
"""

import csv
import sys

CSV_FILE = sys.argv[1] if len(sys.argv) > 1 else "p_positions_4xn_cpp_500.csv"
VERIFY_3XN_UP_TO = 50


def moves_3xn(a, b, c):
    for col in range(c):
        yield (a, b, col)
    for col in range(b):
        yield (a, col, min(c, col))
    for col in range(1, a):
        yield (col, min(b, col), min(c, col))


def tabulate_3xn(max_n):
    p = {(1, 0, 0)}
    for a in range(1, max_n + 1):
        for b in range(a + 1):
            for c in range(b + 1):
                state = (a, b, c)
                if state == (1, 0, 0):
                    continue
                if not any(m in p for m in moves_3xn(a, b, c)):
                    p.add(state)
    return p


def load_csv(path):
    positions = []
    with open(path) as f:
        reader = csv.reader(f)
        next(reader)  # skip header
        for row in reader:
            a, b, c, d, _ = map(int, row)
            positions.append((a, b, c, d))
    return positions


def check_2xn(positions):
    subset = [(a, b, c, d) for a, b, c, d in positions if c == 0 and d == 0]
    failures = [p for p in subset if p[1] != p[0] - 1]
    max_a = max(p[0] for p in subset)
    missing = [(a, a - 1, 0, 0) for a in range(1, max_a + 1)
               if (a, a - 1, 0, 0) not in set(subset)]
    if not failures and not missing:
        print(f"2×n subcase: PASS  ({len(subset)} positions, up to n={max_a})")
    else:
        if failures:
            print(f"2×n subcase: FAIL  {len(failures)} wrong positions: {failures[:5]}")
        if missing:
            print(f"2×n subcase: FAIL  {len(missing)} missing positions: {missing[:5]}")


def check_3xn(positions):
    print(f"3×n subcase: tabulating ground truth up to n={VERIFY_3XN_UP_TO}...", end=" ", flush=True)
    truth = tabulate_3xn(VERIFY_3XN_UP_TO)
    print("done")

    csv_3xn = {(a, b, c) for a, b, c, d in positions if d == 0 and a <= VERIFY_3XN_UP_TO}
    extra   = csv_3xn - truth
    missing = truth - csv_3xn

    if not extra and not missing:
        print(f"3×n subcase: PASS  ({len(truth)} positions, n≤{VERIFY_3XN_UP_TO})")
    else:
        if extra:
            print(f"3×n subcase: FAIL  {len(extra)} spurious positions: {sorted(extra)[:5]}")
        if missing:
            print(f"3×n subcase: FAIL  {len(missing)} missing positions: {sorted(missing)[:5]}")


def main():
    try:
        positions = load_csv(CSV_FILE)
    except FileNotFoundError:
        print(f"Error: {CSV_FILE} not found.")
        print("Download the dataset from https://doi.org/10.5281/zenodo.19543929")
        sys.exit(1)

    print(f"Loaded {len(positions):,} P-positions from {CSV_FILE}\n")
    check_2xn(positions)
    check_3xn(positions)


if __name__ == "__main__":
    main()
