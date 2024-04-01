from fastapi import FastAPI, Form
from fastapi.responses import HTMLResponse
import pickle

# Load the trained model, TF-IDF vectorizer, and label encoder
logreg_model = pickle.load(open("model/logistic_regression_model.sav", "rb"))
tfidf_vectorizer = pickle.load(open("model/tfidf_vectorizer.pkl", "rb"))
label_encoder = pickle.load(open("model/label_encoder.pkl", "rb"))

# Create the FastAPI app
app = FastAPI()

# Define the prediction endpoint
@app.post("/predict", response_class=HTMLResponse)
async def predict_sentiment(review: str = Form(...)):
    # Transform the review text using the TF-IDF vectorizer
    review_tfidf = tfidf_vectorizer.transform([review])
    # Predict sentiment using the loaded logistic regression model
    prediction = logreg_model.predict(review_tfidf)
    # Decode the numeric prediction to the original label
    sentiment = label_encoder.inverse_transform(prediction)[0]
    return """
        <h1>Sentiment Analysis Result</h1>
        <p>Your review: {}</p>
        <p>Predicted sentiment: {}</p>
    """.format(review, sentiment)

# Define the index endpoint to render the HTML form
@app.get("/", response_class=HTMLResponse)
async def index():
    with open("templates/index.html") as f:
        html_content = f.read()
    return HTMLResponse(content=html_content, status_code=200)
