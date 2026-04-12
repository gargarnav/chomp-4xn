# 4×n Chomp — Computational P-position Study

**Author:** Arnav Garg, BITS Pilani, Pilani Campus
**Contact:** gargarnav2007@gmail.com
**Paper:** *Structural Conjectures for 4×n Chomp: Unique Extension,
Asymptotic Ratios, and Period-112 Geometry* (preprint, 2026)

---

## What is Chomp?

Chomp is a two-player combinatorial game played on an m×n grid.
Players alternate taking a square plus all squares above and to the right.
The player forced to take the top-left (poisoned) square loses.

A **P-position** is a losing position for the player to move under
optimal play. Finding P-positions for 4×n Chomp is an open problem —
this repository presents the most extensive computational study to date.

---

## Main Result

**Unique Extension Conjecture:** For any triple (a, b, c) with a ≥ b ≥ c ≥ 0,
there exists at most one non-negative integer d such that (a, b, c, d)
is a P-position of 4×n Chomp.

Verified across **4,316,097 P-positions** for all n ≤ 500. Zero violations found.

---

## Repository Structure

```
chomp-4xn/
├── chomp.cpp              # C++ solver (primary, bitpacked uint64_t)
├── chomp.py               # Python solver (reference implementation, n≤100)
├── verify.py              # Ground truth verification (2×n and 3×n subcases)
├── analysis.ipynb         # Full pattern analysis notebook (all 7 rounds)
├── CONJECTURES.md         # Formal conjecture statements with evidence
├── paper_draft.tex        # LaTeX paper draft
├── paper_draft.md         # Markdown version of the paper
├── figures/
│   ├── fig2_ratio_convergence.png   # Asymptotic ratio convergence plot
│   ├── fig3_cone.png                # 3D cone geometry visualization
│   ├── fig4_autocorrelation.png     # Period-112 autocorrelation plot
│   └── fig5_mask_slices.png         # Prefix mask slices at fixed c
└── README.md
```

---

## Reproducing the Results

### Requirements
- C++17 compiler (g++ or clang++)
- Python 3.9+ with: pandas, numpy, matplotlib, scipy, sklearn
- ~2 GB disk space for output data

### Compile and run the solver

```bash
g++ -O2 -std=c++17 -o chomp_solver chomp.cpp
./chomp_solver 500 > p_positions_4xn_cpp_500.csv
```

This will run for approximately **60–70 minutes** on modern hardware
and produce ~4.3 million P-positions.

### Verify the output

```bash
python verify.py
```

Expected output:
```
2×n subcase: PASS (all positions match (a, a-1, 0, 0))
3×n subcase: PASS (all d=0 positions match independent solver, n≤50)
```

### Run the analysis notebook

```bash
jupyter notebook analysis.ipynb
```

Run all cells in order. The notebook is organized in rounds (1–7),
each building on the previous. Key outputs:
- Round 2: Family growth analysis, ratio convergence
- Round 5: Period-112 chi-squared tests, cone geometry
- Round 7: Algebraic identity search, final limit verification

---

## Data

The full P-position dataset (4,316,097 rows, ~180 MB) is available at:
**[add Zenodo/Google Drive link here after upload]**

Format: CSV with columns `a, b, c, d` (no header), one P-position per row.

---

## Key Findings

| Conjecture | Statement | Status |
|---|---|---|
| Unique Extension | Each (a,b,c) prefix has ≤1 valid d | STRONG (4.3M positions verified) |
| Asymptotic Ratios | b/a→0.762, c/a→0.499, d/a→0.224 | STRONG (numerical) |
| Period-112 Mask | Extending triples have period-112 structure | MODERATE |
| Linear Cone | width(c) ≈ (11/8)c + f(c mod 112) | MODERATE |

---

## Citation

If you use this code or data, please cite:

```bibtex
@article{garg2026chomp,
  title   = {Structural Conjectures for $4 \times n$ Chomp:
             Unique Extension, Asymptotic Ratios, and Period-112 Geometry},
  author  = {Garg, Arnav},
  year    = {2026},
  note    = {Preprint, BITS Pilani}
}
```

---

## Related Work

- Zeilberger (2001) — Three-rowed Chomp, n≤130,000
- Brouwer et al. (2005) — Cubic algorithm for 3×n P-positions
- Berlekamp, Conway, Guy — Winning Ways (foundational theory)
