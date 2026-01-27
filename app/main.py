# app/main.py

from fastapi import FastAPI
from app.data_utils import load_log_returns, create_sequences
from app.model import predict_next_return
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi import Request


app = FastAPI(title="LSTM Stock Return API")
from fastapi.middleware.cors import CORSMiddleware
app.mount("/static", StaticFiles(directory="app/static"), name="static")

templates = Jinja2Templates(directory="app/templates")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.get("/predict")
def predict(ticker: str = "AAPL"):
    series = load_log_returns(ticker)
    sequences = create_sequences(series)
    last_sequence = sequences[-1]

    prediction = predict_next_return(last_sequence)

    return {
        "ticker": ticker,
        "next_day_log_return": prediction
    }
