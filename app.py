
import streamlit as st
import pandas as pd
from datetime import date
from PIL import Image

st.set_page_config(page_title="Butterfly Bet Tracker", page_icon="🦋", layout="centered")

# Load logo
logo = Image.open("butterfly_twi_logo.png")
st.image(logo, width=100)

st.title("🦋 Butterfly Bet Tracker")
st.markdown("Track your daily baseball bets and build smart habits — gracefully.")

# Initialize session state for the data table
if "bets" not in st.session_state:
    st.session_state.bets = []

# Input form
with st.form("bet_form"):
    col1, col2 = st.columns(2)
    with col1:
        game_date = st.date_input("Date", value=date.today())
        teams = st.text_input("Teams (e.g. Cubs vs Cardinals)")
        odds = st.text_input("Odds (e.g. -110)")
    with col2:
        bet_type = st.selectbox("Bet Type", ["Moneyline", "Run Line", "Total", "Prop", "Other"])
        pick = st.text_input("Your Pick (e.g. Cubs ML)")
        stake = st.text_input("Stake ($)", placeholder="e.g. 5.00")

    reasoning = st.text_area("Reasoning / Notes")
    result = st.selectbox("Result", ["Pending", "Win", "Loss"])

    submitted = st.form_submit_button("Add Bet")
    if submitted:
        st.session_state.bets.append({
            "Date": game_date,
            "Teams": teams,
            "Pick": pick,
            "Type": bet_type,
            "Odds": odds,
            "Stake": stake,
            "Result": result,
            "Reasoning": reasoning
        })
        st.success("Bet added!")

# Display table of logged bets
if st.session_state.bets:
    st.markdown("### 📊 Logged Bets")
    df = pd.DataFrame(st.session_state.bets)
    st.dataframe(df, use_container_width=True)
else:
    st.info("No bets added yet. Use the form above to start tracking.")

st.markdown("---")
st.markdown("*“I bet with purpose. Not pressure. I grow gracefully.”*")
