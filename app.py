import streamlit as st
from model import Model
from scipy.stats import zscore
import numpy as np

# Load Stanford GloVe model
model = Model("glove.6B.100d.txt")  # replace with the path to your GloVe model file

# Function to remove outliers
def remove_outliers(words):
    word_vectors = [model.find_word(word.lower()).vector for word in words if model.find_word(word.lower())]
    if len(word_vectors) < 3: return None
    word_vectors = np.array(word_vectors)
    if len(word_vectors.shape) > 1:
        word_vectors = word_vectors.reshape(-1, 1)
    z_scores = zscore(word_vectors)
    return [word for word, z_score in zip(words, z_scores) if abs(z_score) < 3]

# Streamlit app
