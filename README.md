---

# Customer Feedback Sentiment Analysis

A Flask web application utilizing a Long Short-Term Memory (LSTM) Recurrent Neural Network (RNN) to classify customer reviews as **Positive** or **Negative**.

## Table of Contents

1. [Getting Started](#getting-started)
2. [Prerequisites](#prerequisites)
3. [Installation](#installation)
4. [Running the Application](#running-the-application)
5. [Dataset](#dataset)
6. [Built With](#built-with)
7. [Snapshots](#snapshots)

## Getting Started

Follow these instructions to set up and run the application locally.

### 1. Clone the Repository

Clone the repository using the following command:

```bash
git clone https://github.com/Nehal04052/Customer-Feedback-Sentiment-Analysis-using-LSTM.git
```

Alternatively, you can [download the repository as a ZIP](https://github.com/Nehal04052/Customer-Feedback-Sentiment-Analysis-using-LSTM/archive/refs/heads/main.zip) and extract the contents.

### 2. Set Up a Python Virtual Environment

1. Navigate to the project directory:
    ```bash
    cd Customer-Feedback-Sentiment-Analysis-using-LSTM
    ```

2. Create a virtual environment:
    ```bash
    python -m venv flaskapp
    ```
    > You can replace `flaskapp` with a name of your choice.

3. Activate the virtual environment:
    - On **Windows**:
        ```bash
        flaskapp\Scripts\activate.bat
        ```
    - On **Mac/Linux**:
        ```bash
        source flaskapp/bin/activate
        ```
## Installation
### 3. Install Dependencies

Install the required packages listed in `requirements.txt`:

```bash
pip install -r requirements.txt
```

## Prerequisites

Ensure you have the following software installed on your system:

- [Python 3.x](https://www.python.org/downloads/)

## Running the Application

### 4. Configure Environment Variables

Set the necessary environment variables for Flask:

- On **Windows**:
    ```bash
    set FLASK_APP=app.py
    set FLASK_ENV=development
    ```
- On **Mac/Linux**:
    ```bash
    export FLASK_APP=app.py
    export FLASK_ENV=development
    ```

### 5. Run the Flask Application

Run the app with:

```bash
python -m flask run
```

The app will be hosted locally at `http://127.0.0.1:5000/`. Open this URL in your web browser to interact with the app.

## Dataset

The project uses the [Twitter US Airline Sentiment Dataset](https://www.kaggle.com/crowdflower/twitter-airline-sentiment) for training and testing the LSTM-based sentiment classification model. The dataset contains customer feedback in the form of labeled tweets.

## Built With

- **[Python](https://www.python.org/)** - The main programming language used.
- **[TensorFlow](https://www.tensorflow.org/)** - For building and training the LSTM neural network model.
- **[Flask](https://flask.palletsprojects.com/)** - Lightweight web framework to serve the model and handle HTTP requests.
- **[Pandas](https://pandas.pydata.org/)** - Data manipulation and analysis library.

## Snapshots

### Home Page
![Home Page](./Snapshot/Home_Page.png)

### Positive Sentiment Prediction
![Positive Prediction](./Snapshot/Positive_Prediction.png)

### Negative Sentiment Prediction
![Negative Prediction](./Snapshot/Negative_Prediction.png)

---
