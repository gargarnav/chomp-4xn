# 4×n Chomp: Computational P-position Study

**Author:** Arnav Garg, BITS Pilani  
**Paper:** [Structural Conjectures for 4×n Chomp](chomp_4xn.tex) (preprint, 2026)  
**Data:** https://doi.org/10.5281/zenodo.19543929

---

Chomp is a two-player game played on an m×n grid. Players take turns choosing a square and removing it along with everything above and to the right. The top-left square is poisoned, and whoever is forced to take it loses. A P-position is one where the player to move loses with best play on both sides.

This repo contains the code for a complete tabulation of all 4,316,097 P-positions in 4×n Chomp for n up to 500, which is the most extensive computational study of the problem to date.

---

## Main Result

**Unique Extension Conjecture:** For any triple (a, b, c) with a >= b >= c >= 0, there is at most one value of d such that (a, b, c, d) is a P-position.

Verified across all 4,316,097 computed P-positions with no violations. Full conjecture statements and supporting evidence are in the paper.

---

## Files

| File | Description |
|------|-------------|
| `chomp.cpp` | C++ solver with bitpacked uint64_t states |
| `chomp.py` | Python reference implementation (n up to 100) |
| `verify.py` | Checks output against known 2×n and 3×n subcases |
| `analysis.ipynb` | Pattern analysis: ratio convergence, period-112, cone geometry |
| `chomp_4xn.tex` | LaTeX source for the paper |
| `figures/` | Figures from the paper |

The P-position CSV files are not in this repo. Download them from Zenodo at the link above.

---

## Reproducing the Results

Compile and run the solver:

```bash
g++ -O2 -std=c++17 -o chomp_solver chomp.cpp
./chomp_solver 500 > p_positions_4xn_cpp_500.csv
```

This takes around 60-70 minutes on modern hardware and produces roughly 4.3 million P-positions.

Verify the output:

```bash
python3 verify.py
```

Expected output:
```
2×n subcase: PASS
3×n subcase: PASS
```

---

## Citation

```bibtex
@article{garg2026chomp,
  title  = {Structural Conjectures for $4 \times n$ {Chomp}:
            Unique Extension, Asymptotic Ratios, and Period-112 Geometry},
  author = {Garg, Arnav},
  year   = {2026},
  note   = {Preprint, BITS Pilani}
}
```
