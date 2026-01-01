import streamlit as st
import google.generativeai as genai
import os

# --- APP CONFIGURATION ---
st.set_page_config(page_title="Tennis Pro Tutor", page_icon="🎾")

# --- API SETUP ---
# Securely fetch the key from DigitalOcean's environment settings
api_key = os.environ.get("GEMINI_API_KEY")

if api_key:
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel('gemini-1.5-flash')
else:
    st.error("API Key not found. Please set GEMINI_API_KEY in environment variables.")

# --- UI LAYOUT ---
st.title("🎾 AI Tennis Strategy Tutor")
st.markdown("Personalized tactical coaching for your next match.")

# User Profile Section
st.header("Your Profile")
col1, col2 = st.columns(2)

with col1:
    gender = st.selectbox("Gender", ["Male", "Female", "Non-binary"])
    age = st.number_input("Age", min_value=5, max_value=100, value=25)

with col2:
    level = st.selectbox(
        "Proficiency Level", 
        ["Beginner", "Intermediate", "Expert", "Pro"]
    )
    player_type = st.selectbox(
        "Your Playing Style", 
        ["Aggressive Baseliner", "Pusher / Counter-Puncher", "Serve & Volley", "All-Court Player"]
    )

# Opponent Section
st.header("The Match-up")
opponent_type = st.selectbox(
    "Opponent's Playing Style", 
    ["Aggressive Baseliner", "Pusher", "Serve & Volley", "Left-Handed Player", "Power Server", "Moonballer"]
)

# --- GENERATE STRATEGY ---
if st.button("Generate Tactical Plan"):
    if not api_key:
        st.error("The app is not configured with an API key.")
    else:
        with st.spinner("Analyzing playing styles..."):
            prompt = f"""
            Act as an elite tennis coach. 
            User Profile: {gender}, {age} years old, {level} level.
            User Style: {player_type}.
            Opponent Style: {opponent_type}.

            Provide a tactical breakdown:
            1. Key Weakness to Exploit: Identify one specific weakness of a {opponent_type}.
            2. Strategic Patterns: Suggest 2 shot patterns (e.g., 'Wide serve then approach').
            3. Defensive Adjustment: How should
