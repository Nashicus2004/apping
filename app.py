import streamlit as st
from spam_model import train_model

# Load model and accuracy
model, acc = train_model()

# Custom CSS for unique modern style
st.markdown("""
    <style>
        /* Page background gradient */
        .main {
            background: linear-gradient(135deg, #1a1a2e, #16213e);
            color: white;
        }

        html, body, [class*="css"] {
            background-color: transparent;
        }

        h1, h2, h3, h4 {
            color: #ffffff;
        }

        .stTextArea textarea {
            background: rgba(255, 255, 255, 0.1);
            border: 1px solid #ccc;
            border-radius: 12px;
            font-size: 16px;
            color: white;
        }

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

        .glass-box {
            background: rgba(255, 255, 255, 0.1);
            border-radius: 15px;
            padding: 20px;
            margin-top: 20px;
            box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.37);
            backdrop-filter: blur(5px);
            -webkit-backdrop-filter: blur(5px);
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

        footer {visibility: hidden;}
    </style>
""", unsafe_allow_html=True)

# Title
st.markdown("<h1 style='text-align: center;'>🚀 Spam Detector</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center;'>Real-time spam classification using NLP</h3>", unsafe_allow_html=True)

# Glass box container
with st.container():
    st.markdown('<div class="glass-box">', unsafe_allow_html=True)

    user_input = st.text_area("💬 Type your message below:", height=150, placeholder="Enter any message...")
    st.markdown(f"<p style='color: #bbb;'>🧠 Model Accuracy: <code>{acc * 100:.2f}%</code></p>", unsafe_allow_html=True)

    if st.button("🔍 Predict Message"):
        if user_input.strip() == "":
            st.warning("🚨 Please enter a message before predicting.")
        else:
            prediction = model.predict([user_input])[0]
            label = "🚫 Spam" if prediction == 1 else "✅ Not Spam"
            css_class = "spam" if prediction == 1 else "not-spam"
            st.markdown(
                f'<div class="prediction-box {css_class}">Result: {label}</div>',
                unsafe_allow_html=True
            )

    st.markdown('</div>', unsafe_allow_html=True)

# Footer
st.markdown("<br><hr><p style='text-align: center; color: #aaa;'>Built with ❤️ using Streamlit and Scikit-learn</p>", unsafe_allow_html=True)
