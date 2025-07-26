# app.py
import streamlit as st
from spam_model import train_model

# Load model and accuracy
model, acc = train_model()

st.title("📧 Spam Detector App")
st.markdown("Enter a message below to check if it's **spam** or **not spam**.")

# Text input
user_input = st.text_area("Message:", height=150)

# Predict
if st.button("Predict"):
    if user_input.strip() == "":
        st.warning("Please enter a message.")
    else:
        prediction = model.predict([user_input])[0]
        label = "🚫 Spam" if prediction == 1 else "✅ Not Spam"
        st.write("### Prediction:", label)

# Show accuracy
st.markdown(f"**Model Accuracy:** `{acc * 100:.2f}%`")
