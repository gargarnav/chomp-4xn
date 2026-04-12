# Structural Conjectures for 4×n Chomp: Unique Extension, Asymptotic Ratios, and Period-112 Geometry

**Arnav Garg**
BITS Pilani, Pilani Campus
gargarnav2007@gmail.com

## Abstract
We present a computational study of P-positions in $4 \times n$ Chomp. Using an optimized C++ solver, we tabulate all 4,316,097 P-positions for $n \leq 500$. Our analysis reveals four structural conjectures: (1) a **Unique Extension** property; (2) convergence of row-length ratios to fixed asymptotic constants; (3) a **period-112** modular structure; and (4) a **linear cone geometry**. These findings suggest a richer deterministic structure in $4 \times n$ Chomp than previously suspected.

---

## 1. Introduction
Chomp is a two-player combinatorial game played on an $m \times n$ grid. The top-left corner is poisoned; the player forced to take it loses. While $2 \times n$ is solved and $3 \times n$ shows complex periodic structure, the $4 \times n$ case has lacked systematic treatment.

We address this gap by tabulating P-positions up to $n=500$. Our central finding is the **Unique Extension Conjecture**: for any $3$-row prefix $(a, b, c)$, there is at most one $d$ such that $(a, b, c, d)$ is a P-position.

## 2. Computational Setup
- **Solver**: Optimized C++ using bitpacked `uint64_t` states (four 16-bit fields).
- **Efficiency**: Tabulated 4.3M positions in 70 minutes on an Apple M4.
- **Verification**: Cross-checked against $2 \times n$ and $3 \times n$ ground truths.

### Table 1: First 10 P-positions (Lexicographical Order)
| a | b | c | d |
|---|---|---|---|
| 1 | 0 | 0 | 0 |
| 2 | 1 | 0 | 0 |
| 2 | 2 | 1 | 0 |
| 2 | 2 | 2 | 1 |
| 3 | 1 | 1 | 0 |
| 3 | 2 | 0 | 0 |
| 3 | 3 | 1 | 1 |
| 4 | 1 | 1 | 1 |
| 4 | 2 | 2 | 0 |
| 4 | 3 | 0 | 0 |

**Initial d-sequence**: `0, 0, 0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 2, 0, 2, 0, 2, 0, 0, 0, 2, 0, 2, 0, 2, 3, 4, 0, 3, 0`

## 3. Main Conjectures

### Conjecture 1: Unique Extension
For any triple $(a, b, c)$ with $a \ge b \ge c \ge 0$, there exists at most one $d$ such that $(a, b, c, d)$ is a P-position.
*   **Evidence**: Observed in 100% of 4,316,097 P-positions ($n \le 500$).

### Conjecture 2: Asymptotic Ratios
The row lengths converge to fixed ratios as $a \to \infty$:
- $b/a \to L_1 \approx 0.7620$
- $c/a \to L_2 \approx 0.4989$
- $d/a \to L_3 \approx 0.2239$

**Algebraic Identity**: No exact identities found. $\cos(3\pi/7) \approx 0.2225$ is a suggestive near-miss for $L_3$.

### Conjecture 3: Period-112 Modular Mask
The set of extendable triples follows a modular period of **112**.
- Decomposes as $\text{lcm}(7, 8) \times 2$.
- Period 7 is inherited from $3 \times n$ Chomp.
- Period 8 is of unknown origin.

### Conjecture 4: Linear Cone Geometry
The P-position space forms a linear cone in $(a, b, c)$ space:
$\text{width}(c) \approx 1.375 \cdot c + f(c \pmod{112})$

## 4. Discussion
The $4 \times n$ game appears more "deterministic" than the $3 \times n$ game due to the Unique Extension property. If this generalizes to $k \times n$, Chomp may be recursively solvable across all dimensions.

## 5. Open Questions
1. Can the Unique Extension conjecture be proved?
2. Are the limits $L_i$ algebraic?
3. Does the property hold for $5 \times n$ Chomp?
4. What is the cause of the Period-8 signature?

## 6. References
- Berlekamp, Conway, & Guy (2001). *Winning Ways for Your Mathematical Plays*.
- Brouwer, Horváth, et al. (2005). "On three-rowed Chomp," *Integers*.
- Zeilberger (2001). "Three-rowed Chomp," *Advances in Applied Mathematics*.
