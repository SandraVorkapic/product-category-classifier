import joblib

model = joblib.load("models/model.pkl")
vectorizer = joblib.load("models/vectorizer.pkl")

while True:
    title = input("Enter product title: ")
    X = vectorizer.transform([title])
    prediction = model.predict(X)
    print("Predicted category:", prediction[0])