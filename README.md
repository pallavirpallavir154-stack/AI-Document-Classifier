# 📄 AI Document Classifier

An AI-powered document classification application that automatically identifies the category of uploaded documents using Machine Learning and Natural Language Processing (NLP).

## 🚀 Project Overview

The AI Document Classifier uses TF-IDF vectorization and Logistic Regression to analyze document text and predict its category.

Users can upload documents and instantly receive a predicted category along with confidence scores.

## ✨ Features

- Upload and classify text documents.
- Automatic document category prediction.
- Machine Learning-based classification.
- TF-IDF text feature extraction.
- Confidence score for predictions.
- Category-wise confidence visualization.
- Interactive web interface using Streamlit.
- Document preview before classification.

## 🛠️ Technologies Used

- Python
- Machine Learning
- Natural Language Processing (NLP)
- Scikit-learn
- TF-IDF Vectorization
- Logistic Regression
- Streamlit
- Pickle

## 📂 Project Structure

```text
AI-Document-Classifier/
│
├── document_classifier/
│   ├── model.pkl
│   └── vectorizer.pkl
│
├── app.py
├── requirements.txt
└── README.md
```

## 🧠 Machine Learning Model

The project uses:

- **TF-IDF:** Converts text documents into numerical feature vectors.
- **Logistic Regression:** Predicts the category based on extracted text features.
- **Confidence Scores:** Displays prediction probabilities for each category.

## 📊 Supported Categories

The current model supports four categories:

1. comp.graphics
2. rec.sport.baseball
3. sci.med
4. talk.politics.misc

## 📈 Sample Classification Result

**Input Document:** sports.txt

**Document Content:** The baseball team played an excellent match. The players scored several runs and won the championship.

**Predicted Category:** rec.sport.baseball

**Prediction Confidence:** 96.02%

**Result:** Successfully classified.

## ⚙️ Installation and Setup

### 1. Clone the repository

```bash
git clone https://github.com/pallavirpallavir154-stack/AI-Document-Classifier.git
```

### 2. Navigate to the project directory

```bash
cd AI-Document-Classifier
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the application

```bash
streamlit run app.py
```

The application will open in your browser.

## 🎯 Project Objective

To simplify document organization by using Machine Learning and NLP techniques to automatically categorize textual information, reducing manual effort and improving efficiency.

## 👩‍💻 Developer

**Pallavi R**

B.E. Computer Science and Engineering – AI & ML

GitHub: [pallavirpallavir154-stack](https://github.com/pallavirpallavir154-stack)

LinkedIn: [Pallavi R](https://www.linkedin.com/in/pallavi-r-pallavi-r/)

---

⭐ If you find this project interesting, consider giving it a star!
