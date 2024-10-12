from flask import Flask, render_template, flash, request, url_for, redirect, session
import numpy as np
import os
import tensorflow as tf
from tensorflow.keras.preprocessing import sequence
from tensorflow.keras.models import load_model
import pickle

# Set up the Flask app
app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Needed for session handling

IMAGE_FOLDER = os.path.join('static', 'img_pool')
app.config['UPLOAD_FOLDER'] = IMAGE_FOLDER

# Load the tokenizer and model globally
with open('tokenizer.pickle', 'rb') as handle:
    tokenizer = pickle.load(handle)

model = load_model('sentiment_analysis.h5')

@app.route('/', methods=['GET'])
def home():
    # Retrieve results from session if available
    sentiment = session.get('sentiment')
    probability = session.get('probability')
    image = session.get('image')
    text = session.get('text')

    # Clear session variables to avoid repeated data
    session.clear()

    return render_template("index.html", text=text, sentiment=sentiment, probability=probability, image=image)

@app.route('/sentiment_prediction', methods=['POST'])
def sent_anly_prediction():
    if request.method == 'POST':
        text = request.form['text']

        # Convert the input text to sequences and pad them
        tw = tokenizer.texts_to_sequences([text])
        tw = sequence.pad_sequences(tw, maxlen=200)

        # Predict sentiment using the model
        probability = model.predict(tw)[0][0]
        prediction = int(model.predict(tw).round().item())

        if prediction == 0:
            sentiment = 'Negative'
            img_filename = os.path.join(app.config['UPLOAD_FOLDER'], 'sad.gif')
        else:
            sentiment = 'Positive'
            img_filename = os.path.join(app.config['UPLOAD_FOLDER'], 'happy.gif')

        # Store results in the session, converting probability to float
        session['text'] = text
        session['sentiment'] = sentiment
        session['probability'] = round(float(probability), 4)   # Convert float32 to float
        session['image'] = img_filename

        # Redirect to the home page to prevent form resubmission on refresh
        return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)
