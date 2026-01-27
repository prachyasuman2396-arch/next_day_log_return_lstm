# 📈 LSTM-Based Stock Return Prediction Web App

A full-stack machine learning web application that predicts the **next-day log return of a stock** using a **Long Short-Term Memory (LSTM)** neural network.  
The project is deployed as a **public web app** using **FastAPI** and **Render**, with a clean HTML/CSS/JavaScript user interface.

---

## 🚀 Live Demo

🔗 **Public URL:**  
👉 *https://next-day-log-return-lstm.onrender.com*

Users can:
- Enter a stock ticker (e.g., `AAPL`)
- Click **Predict**
- Get the next-day log return predicted by an LSTM model

---

## 🧠 Project Overview

Financial time series are noisy and non-linear.  
This project uses an **LSTM neural network** trained on **log returns** of historical stock prices to model temporal dependencies and make short-horizon predictions.

### Key highlights:
- Uses **log returns** instead of raw prices (stationary series)
- LSTM trained once and **served only for inference**
- Clean separation of:
  - Data processing
  - Model inference
  - API layer
  - Frontend UI
- Deployed as a **single, public web service**

---

## 🏗️ Architecture

User (Browser)
↓
Web UI (HTML / CSS / JS)
↓
FastAPI Backend
↓
Saved LSTM Model (.keras)
↓
Prediction (JSON / UI)


Everything is served from **one FastAPI application**, avoiding CORS issues and simplifying deployment.

---

## 📂 Project Structure

next_day_log_return_lstm/
│
├── app/
│   ├── main.py              # FastAPI app (serves API + UI)
│   ├── data_utils.py        # Data loading & preprocessing
│   ├── model.py             # LSTM model loading & inference
│   │
│   ├── static/              # Static frontend assets
│   │   ├── style.css        # UI styling
│   │   └── script.js        # Frontend logic (API calls)
│   │
│   └── templates/           # HTML templates
│       └── index.html       # Main web UI
│
├── models/
│   └── lstm_model.keras     # Trained LSTM model (saved)
│
├── requirements.txt         # Python dependencies
├── README.md                # Project documentation
└── .gitignore               # Ignored files & folders



---

## ⚙️ Tech Stack

### Machine Learning
- TensorFlow / Keras
- LSTM (Long Short-Term Memory)
- NumPy, Pandas
- Scikit-learn

### Backend
- FastAPI
- Uvicorn

### Frontend
- HTML
- CSS
- JavaScript (Fetch API)

### Deployment
- Render (Python Web Service)

---

## 🔬 Model Details

- **Input:** Sliding window of past log returns
- **Target:** Next-day log return
- **Why log returns?**
  - Stationary
  - Additive over time
  - Standard in quantitative finance

The model is trained **offline** and saved as a `.keras` file.  
The deployed application performs **inference only**, ensuring fast and stable predictions.

---

## 🧪 Running Locally

### 1️⃣ Clone the repository
```bash
git clone <your-repo-url>
cd next_day_log_return_lstm
```
### 2️⃣ Create and activate virtual environment
```bash
python -m venv venv
source venv/bin/activate   # macOS/Linux
```
### 3️⃣ Install dependencies
```bash
pip install -r requirements.txt
```
### 4️⃣ Start the server
```bash
uvicorn app.main:app --reload
```
### 5️⃣ Open in browser
```bash
http://127.0.0.1:8000
```

🌐 API Usage
Predict next-day log return

GET /predict?ticker=AAPL

Example response
{
  "ticker": "AAPL",
  "next_day_log_return": 0.00042
}


📌 Notes & Limitations
Predictions are not financial advice
Daily stock returns are close to white noise
Model performance is limited by market efficiency
CPU-only inference (no GPU)
This project is meant for educational and portfolio purposes.

🧠 What This Project Demonstrates
End-to-end ML system design
Time-series preprocessing best practices
Neural network deployment (LSTM)
FastAPI-based model serving
Full-stack integration
Cloud deployment (Render)

✨ Future Improvements
Confidence intervals / uncertainty estimation
Support for multiple horizons
Ticker validation & error handling
Model comparison (ARIMA, GARCH, XGBoost)
Improved UI (charts, loading states)
