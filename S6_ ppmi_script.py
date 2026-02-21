"""
PPMI Matrix Construction Script
-------------------------------

This script computes the Positive Pointwise Mutual Information (PPMI) matrix
from a co-occurrence edge list.

It is designed to be used together with S5_cooccurrence_script.py:

    1) Run S5_cooccurrence_script.py to generate:
       - S4_Cooccurrence_Matrix.csv  (word1, word2, count)

    2) Run this script (S6_ppmi_script.py) to generate:
       - S6_PPMI_Matrix.csv          (word1, word2, ppmi)

Requirements:
    - Python 3.8+
    - numpy, pandas (optional but recommended)

Input:
    S4_Cooccurrence_Matrix.csv   : co-occurrence edge list

Output:
    S6_PPMI_Matrix.csv           : PPMI edge list

PPMI definition:
    PPMI(i, j) = max( log2( p(i,j) / ( p(i) * p(j) ) ), 0 )

    where:
        p(i,j)  = c(i,j) / N
        p(i)    = c(i)   / N
        c(i)    = sum_j c(i,j)
        N       = sum_{i,j} c(i,j)
"""

import csv
import math
from collections import defaultdict
from pathlib import Path

# -------------------------
# CONFIGURATION (relative paths)
# -------------------------

base_dir = Path(".")  # project root
coocc_file = base_dir / "S4_Cooccurrence_Matrix.csv"
output_file = base_dir / "S6_PPMI_Matrix.csv"


def load_cooccurrences(path: Path):
    """
    Load co-occurrence edge list:
        word1, word2, count
    Returns:
        edges: list of (w1, w2, c)
    """
    edges = []
    with path.open("r", encoding="utf-8") as f:
        reader = csv.reader(f)
        header = next(reader, None)
        for row in reader:
            if len(row) < 3:
                continue
            w1 = row[0].strip()
            w2 = row[1].strip()
            try:
                c = float(row[2])
            except ValueError:
                continue
            if w1 and w2 and c > 0:
                edges.append((w1, w2, c))
    return edges


def compute_ppmi(edges):
    """
    Compute PPMI values from co-occurrence counts.

    edges: list of (w1, w2, c)

    Returns:
        list of (w1, w2, ppmi)
    """
    # Marginal counts c(i)
    marginals = defaultdict(float)
    total = 0.0

    for w1, w2, c in edges:
        marginals[w1] += c
        marginals[w2] += c
        total += c

    if total == 0:
        return []

    ppmi_edges = []

    for w1, w2, c in edges:
        p_ij = c / total
        p_i = marginals[w1] / total
        p_j = marginals[w2] / total

        if p_i <= 0 or p_j <= 0 or p_ij <= 0:
            continue

        pmi = math.log2(p_ij / (p_i * p_j))
        ppmi = max(pmi, 0.0)

        if ppmi > 0:
            ppmi_edges.append((w1, w2, ppmi))

    return ppmi_edges


def save_ppmi(ppmi_edges, path: Path):
    """
    Save PPMI values as edge list:
        word1, word2, ppmi
    """
    with path.open("w", encoding="utf-8", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["word1", "word2", "ppmi"])
        # sort just for readability: by ppmi descending
        for w1, w2, v in sorted(ppmi_edges, key=lambda x: -x[2]):
            writer.writerow([w1, w2, f"{v:.6f}"])


def main():
    print("Loading co-occurrence edge list from:", coocc_file)
    edges = load_cooccurrences(coocc_file)
    print(f"Number of co-occurrence edges: {len(edges)}")

    print("Computing PPMI values...")
    ppmi_edges = compute_ppmi(edges)
    print(f"Number of PPMI edges (PPMI > 0): {len(ppmi_edges)}")

    print("Saving PPMI matrix to:", output_file)
    save_ppmi(ppmi_edges, output_file)
    print("Done.")


if __name__ == "__main__":
    main()
