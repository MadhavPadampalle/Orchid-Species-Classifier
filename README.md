# 🌸 Orchid Species Classifier (DNA Sequence Based)

A **web‑based Machine Learning application** for **automatic classification of Orchidaceae plant species using DNA sequences**. The system applies **k‑mer (NLP‑inspired) feature extraction** on genomic data and uses trained ML models to predict orchid species accurately.

---

## 📌 Project Title

**DNA Sequence Based Classification of Orchidaceae Plant Species using K‑mer Features and Machine Learning Techniques**

---

## 🎯 Objective

* Automate Orchidaceae species identification using DNA barcoding
* Reduce dependency on slow and error‑prone morphological classification
* Apply **NLP techniques on genomic data** (DNA as language, k‑mers as words)
* Provide a **user‑friendly web interface** for prediction

---

## 🧬 Dataset Information

* **Source:** NCBI GenBank
* **Gene Used:** `matK`
* **Format:** FASTA / Text
* **Dataset File:** `orchidaceae_flower.txt`
* **Preprocessing:**

  * Removal of low‑quality sequences
  * Uniform sequence handling
  * k‑mer encoding (hexamers)

---

## ⚙️ Technologies Used

### 🔹 Backend & ML

* Python 🐍
* NumPy
* Pandas
* Scikit‑learn
* Pickle (model serialization)

### 🔹 Machine Learning Models

* Logistic Regression
* Random Forest
* K‑Nearest Neighbors
* Support Vector Machine
* **Gradient Boosting (Best Model)**

### 🔹 Feature Extraction

* k‑mer frequency method
* CountVectorizer (NLP approach)

### 🔹 Web Framework

* Flask
* HTML (templates)
* CSS & JS (static files)

---

## 🧠 Methodology

1. Collect Orchidaceae DNA sequences (matK gene)
2. Clean and preprocess sequences
3. Convert DNA sequences into k‑mer features
4. Generate numerical vectors using CountVectorizer
5. Train multiple ML classifiers
6. Evaluate models using accuracy & F1‑score
7. Save best performing model and vectorizer
8. Deploy model using Flask web application

---

## 📊 Model Performance

| Model                  | Accuracy     |
| ---------------------- | ------------ |
| Logistic Regression    | 88.89%       |
| Random Forest          | 88.89%       |
| K‑Nearest Neighbors    | 66.67%       |
| Support Vector Machine | 88.89%       |
| **Gradient Boosting**  | **94.44%** ✅ |

---

## 📁 Project Structure

```
project_folder/
│
├── static/                  # CSS, JS, images
├── templates/               # HTML templates
│
├── app.py                   # Flask application
├── orchidaceae_flower.txt   # DNA sequence dataset
├── orchid_model.pkl         # Trained ML model
├── orchid_model4.pkl        # Improved/best model
├── vectorizer.pkl           # CountVectorizer
├── vectorizer4.pkl          # Updated vectorizer
└── README.md
```

---

## ▶️ How to Run the Project

### 1️⃣ Clone the repository

```bash
git clone https://github.com/your-username/orchid-species-classifier.git
cd orchid-species-classifier
```

### 2️⃣ Install required packages

```bash
pip install -r requirements.txt
```

### 3️⃣ Run the Flask app

```bash
python app.py
```

### 4️⃣ Open in browser

```
http://127.0.0.1:5000/
```

---

## 🧪 Sample Input

```
ATGCGTACGATCGATCGTACGATCGA
```

### Sample Output

```
Predicted Orchid Species: Dendrobium nobile
```

---

## 🌱 Future Enhancements

* Include additional gene regions (rbcL, ITS)
* Expand dataset with more orchid species
* Apply deep learning models (CNN, LSTM)
* Real‑time sequence upload & validation
* Cloud deployment (AWS / Heroku)

---

## 👨‍💻 Author

**Mr. Madhav Padampalle**
(2021BIT031)
Department of Information Technology
SGGSIET, Nanded

### 👨‍🏫 Guide

**Dr. Ankush D. Sawarkar**

---

## 📜 License

This project is licensed under the **MIT License**.

---

⭐ *If you find this project useful, feel free to star the repository!*
