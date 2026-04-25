#include <iostream>
#include <vector>
#include <tuple>
#include <fstream>
#include <chrono>
#include <algorithm>
#include <unordered_set>

using namespace std;

// We pack the state (a, b, c, d) into a single 64-bit integer since a <= 300
// Each fits in 16 bits.
uint64_t pack(int a, int b, int c, int d) {
    return ((uint64_t)a << 48) | ((uint64_t)b << 32) | ((uint64_t)c << 16) | (uint64_t)d;
}

void extract(uint64_t state, int& a, int& b, int& c, int& d) {
    a = (state >> 48) & 0xFFFF;
    b = (state >> 32) & 0xFFFF;
    c = (state >> 16) & 0xFFFF;
    d = state & 0xFFFF;
}

int main() {
    int max_n = 500;
    cout << "Starting C++ tabulation for n up to " << max_n << "..." << endl;
    
    unordered_set<uint64_t> p_positions_set;
    p_positions_set.reserve(10000000); // Pre-reserve to avoid rehashes
    vector<uint64_t> p_positions_list;
    
    uint64_t term_state = pack(1, 0, 0, 0);
    p_positions_set.insert(term_state);
    p_positions_list.push_back(term_state);
    
    auto start_time = chrono::high_resolution_clock::now();
    uint64_t cells_evaluated = 0;
    
    for (int a = 1; a <= max_n; ++a) {
        int count_n = 0;
        for (int b = 0; b <= a; ++b) {
            for (int c = 0; c <= b; ++c) {
                for (int d = 0; d <= c; ++d) {
                    if (a == 1 && b == 0 && c == 0 && d == 0) continue;
                    
                    bool is_p = true;
                    for (int col = 0; col < d; ++col) {
                        if (p_positions_set.count(pack(a, b, c, col))) { is_p = false; goto check_done; }
                    }
                    for (int col = 0; col < c; ++col) {
                        if (p_positions_set.count(pack(a, b, col, min(d, col)))) { is_p = false; goto check_done; }
                    }
                    for (int col = 0; col < b; ++col) {
                        if (p_positions_set.count(pack(a, col, min(c, col), min(d, col)))) { is_p = false; goto check_done; }
                    }
                    for (int col = 1; col < a; ++col) {
                        if (p_positions_set.count(pack(col, min(b, col), min(c, col), min(d, col)))) { is_p = false; goto check_done; }
                    }
                    
                check_done:
                    if (is_p) {
                        uint64_t st = pack(a, b, c, d);
                        p_positions_set.insert(st);
                        p_positions_list.push_back(st);
                        count_n++;
                    }
                    cells_evaluated++;
                }
            }
        }
        
        // Progress reporting every 10 steps or at end
        if (a % 10 == 0 || a == max_n) {
            auto current_time = chrono::high_resolution_clock::now();
            double elapsed = chrono::duration<double>(current_time - start_time).count();
            
            // Memory estimation: unordered_set overhead + packed values
            // Typically ~32 bytes per node in std::unordered_set
            size_t est_bytes = p_positions_set.size() * (sizeof(uint64_t) * 4); // conservative estimate
            double est_gb = est_bytes / (1024.0 * 1024.0 * 1024.0);
            
            cout << "n=" << a << " | P-found: " << p_positions_set.size() 
                 << " | Time: " << elapsed << "s" 
                 << " | Est. RAM: " << est_gb << " GB" << endl;
            
            // Safety break at 18GB
            if (est_gb > 18.0) {
                cout << "MEMORY LIMIT REACHED (18GB). Saving and exiting." << endl;
                break; 
            }
        }
    }
    
    cout << "\nExporting to CSV..." << endl;
    ofstream out("p_positions_4xn_cpp_500.csv");
    out << "a,b,c,d,n\n";
    for (uint64_t p : p_positions_list) {
        int a, b, c, d;
        extract(p, a, b, c, d);
        out << a << "," << b << "," << c << "," << d << "," << a << "\n";
    }
    out.close();
    
    return 0;
}
