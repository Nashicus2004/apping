import streamlit as st
from spam_model import train_model

# Load model and accuracy
model, acc = train_model()

# Inject CSS for styling
st.markdown("""
    <style>
        .main {
            background-color: #f4f4f4;
        }
        .stTextArea textarea {
            font-size: 16px;
            font-family: 'Segoe UI', sans-serif;
        }
        .stButton button {
            background-color: #4CAF50;
            color: white;
            border-radius: 8px;
            font-size: 16px;
            padding: 10px 20px;
        }
        .prediction-box {
            padding: 1rem;
            border-radius: 10px;
            margin-top: 1rem;
            font-size: 18px;
        }
        .spam {
            background-color: #ffe6e6;
            color: #cc0000;
        }
        .not-spam {
            background-color: #e6ffe6;
            color: #006600;
        }
    </style>
""", unsafe_allow_html=True)

# Title and subtitle
st.title("📧 Spam Detector App")
st.markdown("Check whether a message is **Spam** or **Not Spam** using NLP and Machine Learning.")

# Layout in columns
col1, col2 = st.columns([3, 2])

with col1:
    user_input = st.text_area("✏️ Enter your message here:", height=150, placeholder="Type something suspicious or regular...")

with col2:
    st.markdown(f"### 📊 Model Accuracy:\n`{acc * 100:.2f}%`")

# Prediction logic
if st.button("🔍 Predict Now"):
    if user_input.strip() == "":
        st.warning("⚠️ Please enter a message to analyze.")
    else:
        prediction = model.predict([user_input])[0]
        label = "🚫 Spam" if prediction == 1 else "✅ Not Spam"
        css_class = "spam" if prediction == 1 else "not-spam"
        st.markdown(
            f'<div class="prediction-box {css_class}">Prediction: <strong>{label}</strong></div>',
            unsafe_allow_html=True
        )

# Footer note
st.markdown("---")
st.markdown("Made with ❤️ using Streamlit and Scikit-learn")
