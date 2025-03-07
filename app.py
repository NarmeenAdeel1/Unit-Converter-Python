import streamlit as st

# Set Page Configuration with Icon
st.set_page_config(page_title="Unit Converter", page_icon="🔢")

# Custom CSS for Animated Background & Styling
st.markdown(
    """
    <style>
    /* Animated Gradient Background */
    .stApp {
        background: linear-gradient(-45deg, #ff9a9e, #fad0c4, #ffdde1, #ff758c);
        background-size: 400% 400%;
        animation: gradientBG 8s ease infinite;
        color: black;
    }
    @keyframes gradientBG {
        0% {background-position: 0% 50%;}
        50% {background-position: 100% 50%;}
        100% {background-position: 0% 50%;}
    }
    
    /* Stylish Input Fields */
    .stTextInput, .stSelectbox, .stNumberInput {
        border-radius: 10px;
        padding: 10px;
        background: rgba(255, 255, 255, 0.6);
        color: black;
    }
    
    /* Stylish Button */
    .stButton>button {
        background: linear-gradient(90deg, #ff758c, #ff7eb3);
        color: white;
        font-size: 16px;
        font-weight: bold;
        border-radius: 10px;
        padding: 12px;
        transition: all 0.4s;
    }
    .stButton>button:hover {
        background: linear-gradient(90deg, #ff5e78, #ff4f7b);
        transform: scale(1.05);
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Title
st.title("🔢 Unit Converter with Style ✨")

# Function for Unit Conversion
def convert_units(value, unit_from, unit_to):
    conversions = {
        "meter_kilometer": 0.001,
        "kilometer_meter": 1000,
        "gram_kilogram": 0.001,
        "kilogram_gram": 1000,
    }
    key = f"{unit_from}_{unit_to}"
    return value * conversions.get(key, "Conversion not available")

# User Input
value = st.number_input("💡 Enter value to convert:", min_value=1, step=1)
unit_from = st.selectbox("📏 Convert from:", ["meter", "kilometer", "gram", "kilogram"])
unit_to = st.selectbox("🔄 Convert to:", ["meter", "kilometer", "gram", "kilogram"])

# Convert Button
if st.button("🚀 Convert Now"):
    result = convert_units(value, unit_from, unit_to)
    st.write(f"🎯 Converted Value: **{result} {unit_to}**")
