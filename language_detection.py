import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from tkinter import Tk, Label, Text, Button, StringVar

# Step 1: Load dataset
url = "https://raw.githubusercontent.com/amankharwal/Website-data/master/dataset.csv"
data = pd.read_csv(url)

# Step 2: Preprocessing
cv = CountVectorizer()
X = cv.fit_transform(data['Text'])
y = data['language']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Step 3: Train model
model = MultinomialNB()
model.fit(X_train, y_train)

# Step 4: Prediction function
def detect_language(text):
    vector = cv.transform([text]).toarray()
    prediction = model.predict(vector)
    return prediction[0]

# Step 5: GUI setup
def on_detect():
    input_text = text_input.get("1.0", "end-1c")  # Read from text box
    if input_text.strip() == "":
        result.set("Please enter some text.")
    else:
        lang = detect_language(input_text)
        result.set(f"Detected Language: {lang}")

# Create GUI window
root = Tk()
root.title("Language Detection App")
root.geometry("400x300")

# GUI Elements
Label(root, text="Enter text in any language:", font=("Arial", 12)).pack(pady=10)
text_input = Text(root, height=5, width=40)
text_input.pack()

Button(root, text="Detect Language", command=on_detect, font=("Arial", 12), bg="blue", fg="white").pack(pady=10)

result = StringVar()
Label(root, textvariable=result, font=("Arial", 12, "bold"), fg="green").pack(pady=10)

# Run the app
root.mainloop()
