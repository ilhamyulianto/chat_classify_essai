ISP CUSTOMER QUESTION CLASSIFICATION
===================================

1. Project Overview
-------------------
Project ini bertujuan untuk membangun sistem Machine Learning (ML) yang dapat
mengklasifikasikan pertanyaan pelanggan ISP ke dalam tiga kategori utama:

1. Information
   - Pertanyaan terkait informasi produk, tagihan, pembayaran, harga, promo, dll.

2. Request
   - Permintaan layanan seperti pemasangan baru, pindah alamat, reset password,
     upgrade paket, permintaan teknisi, dan layanan operasional lainnya.

3. Problem
   - Laporan gangguan atau masalah teknis seperti internet lambat, koneksi putus,
     modem bermasalah, jaringan tidak stabil, dan sejenisnya.

Dataset awal tidak memiliki label sehingga dilakukan pendekatan auto-labeling
berbasis NLP sebelum melatih model supervised learning.


2. Methodology Description
--------------------------

2.1 Auto Labeling (Weak Supervision)
Auto labeling dilakukan menggunakan pendekatan weak supervision, yaitu
mengombinasikan beberapa sinyal lemah untuk memberikan label awal pada data,
antara lain:

- Text normalization (slang, typo, istilah ISP)
- Custom stopwords (kata sapaan dan kata tidak informatif)
- Domain-specific keywords
- Semantic anchor text (CATEGORY_TEXT)
- TF-IDF cosine similarity
- Confidence thresholding

Pendekatan ini digunakan untuk menghasilkan dataset berlabel awal yang 
berkualitas tanpa anotasi manual sepenuhnya.


2.2 Text Preprocessing
Tahapan preprocessing meliputi:
- Lowercasing
- Penghapusan karakter non-alfabet
- Normalisasi istilah ISP (contoh: "lemot" -> "lambat")
- Tokenisasi menggunakan NLTK
- Stopword removal (custom stopword list)
- Penghapusan data duplikat
- Penghapusan kalimat berbahasa Inggris

Preprocessing bertujuan untuk mengurangi noise dan meningkatkan konsistensi
representasi teks.


2.3 Feature Extraction (TF-IDF)
Teks dipetakan ke dalam ruang vektor menggunakan TF-IDF dengan konfigurasi:
- Unigram dan Bigram (ngram_range = (1,2))
- min_df = 2 untuk menghilangkan kata langka
- max_df = 0.9 untuk menghilangkan kata terlalu umum
- sublinear_tf = True untuk stabilitas bobot

Pendekatan ini cocok untuk data teks pendek dan sparse seperti pertanyaan pelanggan.


2.4 Classification Model
Model yang digunakan adalah Linear Support Vector Machine (LinearSVC) dengan:
- class_weight = "balanced" untuk menangani ketidakseimbangan kelas
- Regularisasi default (C = 1.0)

Linear SVM dipilih karena:
- Cocok untuk data berdimensi tinggi dan sparse
- Lebih robust terhadap label noise
- Efisien dan stabil untuk dataset ukuran kecil-menengah
- Mudah diinterpretasi dan dievaluasi


2.5 Model Evaluation
Evaluasi dilakukan menggunakan:
- Stratified K-Fold Cross Validation (n_splits = 15)
- Metrics:
  - Accuracy
  - Precision (macro)
  - Recall (macro)

Stratifikasi digunakan untuk menjaga proporsi kelas pada setiap fold
karena dataset tidak seimbang.


3. Code Flow
------------

1. Load dataset CSV
2. Exploratory analysis (cek distribusi data)
3. Remove duplicate questions
4. Filter non-Indonesian (English) sentences
5. Text preprocessing & normalization
6. Auto labeling using:
   - Keyword signals
   - Semantic similarity with CATEGORY_TEXT
   - Threshold filtering
7. Final labeled dataset
8. TF-IDF vectorization
9. Train-test split (80-20)
10. Train Linear SVM model
11. Cross-validation with StratifiedKFold
12. Model evaluation (accuracy, precision, recall)


4. Installation Guide
---------------------

4.1 Create Virtual Environment (Optional)
-----------------------------------------
python -m venv venv
venv\Scripts\activate     

or if using conda env
create/activate desired conda environment
change directory to folder location
pip install -r requirements.txt ---- for installing dependencies at conda.

4.2 Install Dependencies
------------------------
pip install -r requirements.txt

4.3 Download NLTK Tokenizer
---------------------------
Open Python or Jupyter and run:

import nltk
nltk.download("punkt")


5. How to Run & Test the Model
------------------------------

1. Open the Jupyter Notebook (.ipynb)
2. Run cells sequentially from top to bottom
3. Ensure dataset CSV is placed in the correct directory
4. Observe:
   - Auto-labeling coverage
   - Label distribution
   - Cross-validation metrics
5. Review evaluation results:
   - Accuracy
   - Precision
   - Recall
   - Classification report


6. Expected Output
------------------
Typical evaluation result:

Accuracy  : ~0.83
Precision : ~0.65
Recall    : ~0.67

Results may vary slightly depending on random state and data distribution.


7. Notes & Limitations
----------------------
- Auto-labeling may introduce label noise
- Results depend on quality of normalization and anchor text
- Model is designed as a baseline / production-ready lightweight classifier
- Further improvements can be achieved via:
  - Manual label refinement
  - Active learning
  - Threshold tuning
  - Domain expansion


8. Conclusion
-------------
This project demonstrates an end-to-end NLP pipeline for classifying customer
questions using auto-labeling and supervised learning. The approach balances
engineering practicality, interpretability, and performance, making it suitable
for real-world ISP customer service applications.
