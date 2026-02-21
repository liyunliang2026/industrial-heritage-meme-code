# Industrial Heritage Meme Genome – Data and Reproducibility Package

This repository provides the data files and analysis scripts associated with the paper:

**“A Semantic Feature Extraction–Based Meme Genome Model for Industrial Heritage”**

Due to CNKI copyright restrictions, the full text corpus used in the study cannot be publicly redistributed.  
However, all metadata, high-frequency vocabulary lists, example data structures, and full analysis scripts are provided to ensure complete methodological transparency and reproducibility.

---

## 📁 Repository Contents

### **S1_Corpus_List.docx**
List of 102 CSSCI journal articles that constitute the original Chinese-language corpus.  
Readers may obtain access to these articles independently through the CNKI database.

### **S2_stopwords_list.txt**
Custom Chinese noun stopword list used during tokenization and filtering.

### **S3_HighFrequencyWords.csv**
The 80 high-frequency nouns extracted from the corpus, including occurrences.

### **S4_Cooccurrence_Matrix.csv**
A small *illustrative example* of the co-occurrence matrix structure (word1, word2, count).  
Values are demonstrative and not identical to the full analysis, which can be regenerated with the scripts below.

### **S5_cooccurrence_script.py**
Python script that computes the co-occurrence edge list from the full Chinese corpus  
(tokenization → noun extraction → stopword filtering → sliding window co-occurrence counting).

### **S6_ppmi_script.py**
Python script that transforms the co-occurrence matrix into a PPMI-weighted network  
(used for semantic network construction and community detection).

### **S7_Modularity_Values.csv**
Modularity values (Q ± sd) used to generate the parameter sensitivity heatmap in the paper.

---

## 🔁 Reproducibility Instructions

To fully reproduce the semantic network, PPMI matrix, and community detection results:

1. Obtain access to the 102 CNKI articles listed in **S1_Corpus_List.docx**.
2. Place all corpus `.txt` files into a directory named `corpus/` in the project root.
3. Install dependencies:

   ```bash
   pip install jieba numpy pandas
   # Industrial Heritage Meme Genome – Data and Reproducibility Package

This repository provides the data files and analysis scripts associated with the paper:

**“A Semantic Feature Extraction–Based Meme Genome Model for Industrial Heritage”**

Due to CNKI copyright restrictions, the full text corpus used in the study cannot be publicly redistributed.  
However, all metadata, high-frequency vocabulary lists, example data structures, and full analysis scripts are provided to ensure complete methodological transparency and reproducibility.

---

## 📁 Repository Contents

### **S1_Corpus_List.docx**
List of 102 CSSCI journal articles that constitute the original Chinese-language corpus.  
Readers may obtain access to these articles independently through the CNKI database.

### **S2_stopwords_list.txt**
Custom Chinese noun stopword list used during tokenization and filtering.

### **S3_HighFrequencyWords.csv**
The 80 high-frequency nouns extracted from the corpus, including occurrences.

### **S4_Cooccurrence_Matrix.csv**
A small *illustrative example* of the co-occurrence matrix structure (word1, word2, count).  
Values are demonstrative and not identical to the full analysis, which can be regenerated with the scripts below.

### **S5_cooccurrence_script.py**
Python script that computes the co-occurrence edge list from the full Chinese corpus  
(tokenization → noun extraction → stopword filtering → sliding window co-occurrence counting).

### **S6_ppmi_script.py**
Python script that transforms the co-occurrence matrix into a PPMI-weighted network  
(used for semantic network construction and community detection).

### **S7_Modularity_Values.csv**
Modularity values (Q ± sd) used to generate the parameter sensitivity heatmap in the paper.

---

## 🔁 Reproducibility Instructions

To fully reproduce the semantic network, PPMI matrix, and community detection results:

1. Obtain access to the 102 CNKI articles listed in **S1_Corpus_List.docx**.
2. Place all corpus `.txt` files into a directory named `corpus/` in the project root.
3. Install dependencies:

   ```bash
   pip install jieba numpy pandas
Run:

S5_cooccurrence_script.py → generates S4_Cooccurrence_Matrix.csv (full version)

S6_ppmi_script.py → generates S6_PPMI_Matrix.csv (full version)

Use the resulting PPMI network for subsequent semantic clustering or Leiden community detection.

⚠️ Copyright Notice

The Chinese-language corpus consists of journal articles retrieved from CNKI,
whose full texts are protected under publisher copyright.

Therefore, the actual corpus cannot be redistributed in this repository.

All scripts, metadata, and example data structures are shared here to enable full methodological reproducibility.

📚 Citation

If you use this repository or adapt the scripts, please cite:

[Your Name] (2026). Industrial Heritage Meme Genome – Data and Reproducibility Package.
GitHub repository: https://github.com/…
 (replace with your URL)
