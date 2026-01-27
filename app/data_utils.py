# app/data_utils.py

import yfinance as yf
import numpy as np
import pandas as pd

def load_log_returns(ticker: str):
    df = yf.download(ticker, start="2010-01-01", progress=False)
    df = df[['Close']]
    df['log_return'] = np.log(df['Close'] / df['Close'].shift(1))
    df.dropna(inplace=True)
    return df['log_return'].values


def create_sequences(series, window=20):
    X = []
    for i in range(len(series) - window):
        X.append(series[i:i + window])
    return np.array(X)
