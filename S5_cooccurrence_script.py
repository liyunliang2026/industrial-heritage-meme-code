"""
Co-occurrence Matrix Construction Script
----------------------------------------

This script reproduces the co-occurrence counting procedure used in the paper.
To ensure reproducibility under CNKI copyright restrictions, the full corpus
cannot be distributed. Readers who obtain access to the same 102-article corpus
can place the text files in the /corpus/ directory and run this script to 
recompute the full co-occurrence matrix.

Requirements:
    - Python 3.8+
    - jieba (Chinese tokenizer)
    - numpy, pandas

Inputs:
    /corpus/*.txt              : Raw corpus files (Chinese full texts)
    stopwords_list.txt         : Stopword list (Chinese nouns)
    S3_HighFrequencyWords.csv  : High-frequency noun list (80 words)

Outputs:
    S4_Cooccurrence_Matrix.csv : Co-occurrence edge list (word1, word2, count)

Parameters:
    window_size = 10           : Symmetric sliding window
    min_count   = 3            : Minimum co-occurrence threshold
"""

import jieba
import jieba.posseg as pseg
import csv
from pathlib import Path
from collections import Counter

# -------------------------
# CONFIGURATION (Relative paths)
# -------------------------

base_dir = Path(".")  # project root
corpus_dir = base_dir / "corpus"
stopwords_file = base_dir / "stopwords_list.txt"
highfreq_file = base_dir / "S3_HighFrequencyWords.csv"
output_file = base_dir / "S4_Cooccurrence_Matrix.csv"

WINDOW_SIZE = 10
MIN_COUNT = 3


def load_stopwords(path):
    stopwords = set()
    with open(path, "r", encoding="utf-8") as f:
        for line in f:
            lw = line.strip()
            if lw:
                stopwords.add(lw)
    return stopwords


def load_target_words(path):
    target = set()
    with open(path, "r", encoding="utf-8") as f:
        reader = csv.reader(f)
        next(reader, None)  # skip header
        for row in reader:
            if row and row[0].strip():
                target.add(row[0].strip())
    return target


def tokenize_text(text, stopwords, target_words):
    """Return list of tokens (Chinese nouns only)."""
    tokens = []
    for word, flag in pseg.cut(text):
        w = word.strip()
        if not w:
            continue
        if not flag.startswith("n"):  # keep nouns only
            continue
        if w in stopwords:
            continue
        if w not in target_words:
            continue
        tokens.append(w)
    return tokens


def build_cooccurrence(tokens, window=10, min_count=3):
    """Symmetric sliding-window co-occurrence counting."""
    co = Counter()
    n = len(tokens)

    for i in range(n):
        window_tokens = tokens[i : i + window]
        for j in range(len(window_tokens)):
            for k in range(j + 1, len(window_tokens)):
                w1 = window_tokens[j]
                w2 = window_tokens[k]
                if w1 == w2:
                    continue
                pair = tuple(sorted([w1, w2]))
                co[pair] += 1

    return {pair: c for pair, c in co.items() if c >= min_count}


def main():
    print("Loading stopwords...")
    stopwords = load_stopwords(stopwords_file)

    print("Loading high-frequency nouns...")
    target_words = load_target_words(highfreq_file)

    print("Tokenizing corpus...")
    tokens = []
    for txt_file in corpus_dir.glob("*.txt"):
        text = txt_file.read_text(encoding="utf-8", errors="ignore")
        tokens.extend(tokenize_text(text, stopwords, target_words))

    print("Building co-occurrence matrix...")
    edge_dict = build_cooccurrence(tokens, window=WINDOW_SIZE, min_count=MIN_COUNT)

    print("Saving results to:", output_file)
    with open(output_file, "w", encoding="utf-8", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["word1", "word2", "count"])
        for (w1, w2), c in sorted(edge_dict.items(), key=lambda x: -x[1]):
            writer.writerow([w1, w2, c])

    print("Done.")


if __name__ == "__main__":
    main()
