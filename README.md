# 🌸 Orchid Species Classifier

A Machine Learning–based project for **classifying Orchidaceae species using DNA sequences**. This project uses **k‑mer frequency features** extracted from DNA barcode sequences and applies **Logistic Regression** for accurate species prediction.

---

## 📌 Project Overview

Orchidaceae is one of the largest plant families, and accurate species identification is crucial for biodiversity conservation, taxonomy, and research. Manual identification is time‑consuming and error‑prone. This project automates orchid species classification using **bioinformatics and machine learning** techniques.

---

## 🧬 Dataset

* **File name:** `orchidaceae_flower.txt`
* **Data type:** DNA sequences (FASTA / text format)
* **Labels:** Orchid species names

Each DNA sequence is converted into numerical features using **k‑mer frequency extraction**.

---

## ⚙️ Technologies Used

* **Programming Language:** Python 🐍
* **Libraries:**

  * NumPy
  * Pandas
  * Scikit‑learn
* **Machine Learning Algorithm:** Logistic Regression
* **Feature Extraction:** k‑mer frequency method

---

## 🧠 Methodology

1. Load DNA sequence dataset
2. Clean and preprocess sequences
3. Extract k‑mer frequency features
4. Encode species labels
5. Train Logistic Regression classifier
6. Evaluate model accuracy
7. Predict orchid species for new DNA sequences

---

## ▶️ How to Run the Project

### 1️⃣ Clone the repository

```bash
git clone https://github.com/your-username/orchid-species-classifier.git
cd orchid-species-classifier
```

### 2️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

### 3️⃣ Run the program

```bash
python aap.py
```

---

## 📊 Model Output

* Displays **classification accuracy**
* Predicts **orchid species name** for a given DNA sequence

---

## 🧪 Example Input

```text
ATGCGTACGATCGATCGTACGATCG
```

### Example Output

```text
Predicted Species: Dendrobium nobile
```

---

## 📁 Project Structure

```
orchid-species-classifier/
│── aap.py
│── orchidaceae_flower.txt
│── requirements.txt
│── README.md
```

---

## 🚀 Future Enhancements

* Support for deep learning models (CNN / LSTM)
* Web‑based frontend for sequence upload
* Multi‑barcode sequence support
* Improved accuracy with ensemble models

---

## 👨‍💻 Author

**Vaishanth**
Machine Learning & Bioinformatics Enthusiast

---

## 📜 License

This project is licensed under the **MIT License**.

---

⭐ *If you find this project useful, please give it a star!*
