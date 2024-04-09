import streamlit as st
from wv import Model
from scipy.stats import zscore

model = Model("/full/path/to/your/models/glove_short.txt")


st.title("Remove Outliers from a list of words")

print("Loading model from models/glove_short.txt ...")
print("Loaded in", model.load_time, "secs")

words = st.text_input("Please enter a comma separated list of words:")

if words:
    words = words.split(",")
    if len(words) < 3:
        st.error("Please enter at least 3 words.")
    else:
        filtered_words = [word.strip() for word in words if word.strip() in model]
        z_scores = zscore([model[word] for word in filtered_words])
        filtered_words = [filtered_words[i] for i, z_score in enumerate(z_scores) if abs(z_score) < 3]

        st.success(f"With outliers removed, your list looks like this: {', '.join(filtered_words)}")
