# app/model.py

import tensorflow as tf
import numpy as np

MODEL_PATH = "models/lstm_model.keras"

model = tf.keras.models.load_model(MODEL_PATH)

def predict_next_return(sequence):
    sequence = sequence.reshape(1, -1, 1)
    prediction = model.predict(sequence, verbose=0)
    return float(prediction[0][0])
