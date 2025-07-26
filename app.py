import streamlit as st
from spam_model import train_model

model, acc = train_model()

st.markdown("""
    <style>
        /* Set full-screen gradient background */
        body {
            background: linear-gradient(135deg, #0f2027, #203a43, #2c5364);
            background-attachment: fixed;
            background-size: cover;
            color: white;
        }

        /* Hide Streamlit branding footer */
        footer {visibility: hidden;}

        /* Style for text area */
        .stTextArea textarea {
            background-color: rgba(255, 255, 255, 0.08);
            color: #ffffff;
            border: 1px solid #ccc;
            border-radius: 12px;
            font-size: 16px;
        }

        /* Style for button */
        .stButton button {
            background: linear-gradient(45deg, #00dbde, #fc00ff);
            border: none;
            color: white;
            font-size: 18px;
            font-weight: bold;
            padding: 12px 24px;
            border-radius: 10px;
            transition: 0.3s;
        }

        .stButton button:hover {
            transform: scale(1.05);
        }

        /* Glass-style card */
        .glass-box {
            background: rgba(255, 255, 255, 0.07);
            border-radius: 15px;
            padding: 30px;
            margin-top: 20px;
            box-shadow: 0 8px 24px rgba(0, 0, 0, 0.2);
        }

        .prediction-box {
            text-align: center;
            font-size: 22px;
            margin-top: 20px;
            padding: 20px;
            border-radius: 12px;
            font-weight: bold;
            color: #fff;
        }

        .spam {
            background: rgba(255, 0, 0, 0.3);
            border: 2px solid #ff4d4d;
        }

        .not-spam {
            background: rgba(0, 255, 0, 0.2);
            border: 2px solid #4dff88;
        }
    </style>
""", unsafe_allow_html=True)

st.markdown("<h1 style='text-align: center;'>📧 Spam Message Detector AI</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center; color: #ccc;'>Instantly detect spam using Machine Learning</h3>", unsafe_allow_html=True)

with st.container():
    st.markdown('<div class="glass-box">', unsafe_allow_html=True)

    user_input = st.text_area(" Enter suspected message:", height=150, placeholder="Enter text here:")

    st.markdown(f"<p style='color: #ccc;'> Model Accuracy: <code>{acc * 100:.2f}%</code></p>", unsafe_allow_html=True)

    if st.button("🔍 Predict"):
        if user_input.strip() == "":
            st.warning(" Please enter a message.")
        else:
            prediction = model.predict([user_input])[0]
            label = " Spam" if prediction == 1 else " Not Spam"
            css_class = "spam" if prediction == 1 else "not-spam"
            st.markdown(
                f'<div class="prediction-box {css_class}">Prediction: {label}</div>',
                unsafe_allow_html=True
            )

    st.markdown('</div>', unsafe_allow_html=True)

# Footer
st.markdown("<hr><p style='text-align: center; color: #aaa;'>⚙️ Built using Streamlit, Scikit-learn & Love 💖</p>", unsafe_allow_html=True)
