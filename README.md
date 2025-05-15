## 🧠 Project Title: Language Detection Using Machine Learning

### 📌 Project Description:

This project focuses on detecting the language of a given text input using a machine learning model trained on multilingual data. It uses natural language processing techniques to convert raw text into numerical vectors, then applies a **Naive Bayes classifier** to predict the language. The trained model is integrated with a **Graphical User Interface (GUI)** built using Tkinter, allowing users to enter any text and detect its language instantly.

---

### 🎯 Objective:

To build an intelligent system that can:

* Learn patterns from text data in multiple languages.
* Detect the language of a given input sentence.
* Provide user-friendly interaction through a simple GUI.

---

### 🧰 Tools & Technologies Used:

* **Python** – Programming language
* **Pandas** – Data handling
* **Scikit-learn** – Machine learning (Naive Bayes, CountVectorizer)
* **Tkinter** – For GUI design
* **Dataset** – 22 languages, 1000 samples each (from Aman Kharwal's GitHub)

---

### 🧪 How It Works:

1. **Dataset Loading**: The model is trained on a dataset of 22 languages with labeled text samples.
2. **Preprocessing**: Text is converted to numeric form using `CountVectorizer`.
3. **Model Training**: A **Multinomial Naive Bayes** classifier is trained on the text features.
4. **GUI Integration**: A user-friendly interface is created where users can enter a sentence and click a button to detect the language.
5. **Prediction**: The model predicts the language and displays the result on the screen.

---

### ✅ Features:

* Detects 22 different languages
* Instant prediction from text input
* Clean, responsive GUI using Tkinter
* Accuracy printed in the backend (can be extended to display in GUI)

