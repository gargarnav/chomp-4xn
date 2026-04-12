import csv

def generate_moves_3xn(state):
    a, b, c = state
    
    # Row 2
    for col in range(c):
        yield (a, b, col)
        
    # Row 1
    for col in range(b):
        yield (a, col, min(c, col))
        
    # Row 0
    for col in range(1, a):
        yield (col, min(b, col), min(c, col))

def tabulate_3xn(max_n):
    p_positions = set([(1, 0, 0)])
    
    for a in range(1, max_n + 1):
        for b in range(a + 1):
            for c in range(b + 1):
                state = (a, b, c)
                if state == (1, 0, 0):
                    continue
                
                is_p = True
                for move in generate_moves_3xn(state):
                    if move in p_positions:
                        is_p = False
                        break
                
                if is_p:
                    p_positions.add(state)
                    
    return p_positions

def verify():
    csv_file = "p_positions_4xn_cpp.csv"
    p_pos_csv = []
    
    try:
        with open(csv_file, 'r') as f:
            reader = csv.reader(f)
            next(reader) # skip header
            for row in reader:
                a, b, c, d, _ = map(int, row)
                p_pos_csv.append((a, b, c, d))
    except FileNotFoundError:
        print(f"Error: Could not read {csv_file}")
        return

    print("--- Check 2: 2xn Sub-case ---")
    d0_c0 = [p for p in p_pos_csv if p[2] == 0 and p[3] == 0]
    expected_2xn = set((a, a - 1, 0, 0) for a in range(1, 201))
    
    csv_2xn_set = set(d0_c0)
    
    errors_2xn = 0
    for p in d0_c0:
        if p[1] != p[0] - 1:
            print(f"FAIL 2xn: Unexpected P-position found: {p}")
            errors_2xn += 1
            
    for exp in expected_2xn:
        if exp not in csv_2xn_set:
            print(f"FAIL 2xn: Missing expected P-position: {exp}")
            errors_2xn += 1
            
    if errors_2xn == 0:
        print("PASS: 2xn sub-case exactly matches (a, a-1, 0, 0)")
        
    print("\n--- Check 1: 3xn Sub-case ---")
    max_3xn_verify = 50
    print(f"Tabulating independent 3xn truths up to n={max_3xn_verify}...")
    ground_truth_3xn = tabulate_3xn(max_3xn_verify)
    
    d0 = [p for p in p_pos_csv if p[3] == 0 and p[0] <= max_3xn_verify]
    csv_3xn_set = set((p[0], p[1], p[2]) for p in d0)
    
    errors_3xn = 0
    for p in d0:
        state_3 = (p[0], p[1], p[2])
        if state_3 not in ground_truth_3xn:
            print(f"FAIL 3xn: CSV contains {p} but it is NOT a true P-position!")
            errors_3xn += 1
            
    for truth in ground_truth_3xn:
        if truth not in csv_3xn_set:
            print(f"FAIL 3xn: Ground truth contains {truth} but missing from CSV!")
            errors_3xn += 1
            
    if errors_3xn == 0:
        print(f"PASS: 3xn sub-case perfectly matches ground truth for all n <= {max_3xn_verify}")

if __name__ == "__main__":
    verify()
