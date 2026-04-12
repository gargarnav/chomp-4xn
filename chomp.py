import csv
import time
from collections import defaultdict

def generate_moves(state):
    a, b, c, d = state
    
    # Row 3 (bottom-up often prunes faster or no difference, let's just do 3 to 0)
    # Actually yielding unique is easy since we only change one row at a time 
    # and clamp. Wait, different row picks can lead to the same state.
    # Memo lookup is O(1) so duplicates are cheap.
    
    for col in range(d):
        yield (a, b, c, col)

    for col in range(c):
        yield (a, b, col, min(d, col))
        
    for col in range(b):
        yield (a, col, min(c, col), min(d, col))
        
    for col in range(1, a):
        yield (col, min(b, col), min(c, col), min(d, col))

def tabulate_4xn(max_n):
    p_positions_set = {(1, 0, 0, 0)}
    p_positions_list = [(1, 0, 0, 0)]
    
    start_time = time.time()
    
    for n in range(1, max_n + 1):
        target_a = n
        count_n = 0
        cells_evaluated = 0
        # Iterate over all possible b, c, d
        for b in range(target_a + 1):
            for c in range(b + 1):
                for d in range(c + 1):
                    state = (target_a, b, c, d)
                    if state == (1, 0, 0, 0):
                        continue
                        
                    # Check if this state is a P-position
                    is_p = True
                    for move in generate_moves(state):
                        if move in p_positions_set:
                            # Move to a P-position makes this an N-position
                            is_p = False
                            break
                            
                    if is_p:
                        p_positions_set.add(state)
                        p_positions_list.append(state)
                        count_n += 1
                    cells_evaluated += 1
                        
        elapsed = time.time() - start_time
        print(f"n={n} | Iterated: {cells_evaluated} | P-positions added: {count_n} | Total P-Positions: {len(p_positions_set)} | Time: {elapsed:.2f}s")
        
    return p_positions_list

def export_p_positions(p_positions, filename):
    with open(filename, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['a', 'b', 'c', 'd', 'n'])
        for p in p_positions:
            # The 'n' that triggered discovery is effectively 'a'
            writer.writerow([p[0], p[1], p[2], p[3], p[0]])
            
def analyze_patterns(p_positions):
    print("\n--- Pattern Analysis ---")
    
    # We will look at differences: a-b, b-c, c-d
    with open("analysis.txt", "w") as f:
        for p in p_positions:
            a, b, c, d = p
            diffs = (a-b, b-c, c-d)
            line = f"P: {p} => a-b={diffs[0]}, b-c={diffs[1]}, c-d={diffs[2]}"
            f.write(line + "\n")
            if a <= 20: # just log a few to console
                print(line)

if __name__ == "__main__":
    max_cells = 100
    print(f"Starting tabulation for n up to {max_cells}...")
    p_pos = tabulate_4xn(max_cells)
    
    print("\nExporting to CSV...")
    export_p_positions(p_pos, "p_positions_4xn.csv")
    
    print("Performing analysis...")
    analyze_patterns(p_pos)
    print("\nDone. Results saved to p_positions_4xn.csv and analysis.txt")
