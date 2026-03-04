# pages/Register.py

import streamlit as st
import pandas as pd
from datetime import datetime
import os
from data import tournaments

st.set_page_config(page_title="Register")

key = st.session_state.get("current", "main")

t = tournaments[key]

st.title("📝 Registration")
st.subheader(t["name"])

st.divider()

# Form
with st.form("form"):

    name = st.text_input("Full Name *")
    chess_id = st.text_input("Chess.com Username *")
    phone = st.text_input("Phone *")
    email = st.text_input("Email")
    age = st.number_input("Age", 5, 100)

    submit = st.form_submit_button("Submit")

FILE = f"reg_{key}.csv"

if submit:

    if name and chess_id and phone:

        data = {
            "Name": name,
            "Chess ID": chess_id,
            "Phone": phone,
            "Email": email,
            "Age": age,
            "Time": datetime.now()
        }

        df = pd.DataFrame([data])

        if os.path.exists(FILE):
            old = pd.read_csv(FILE)
            df = pd.concat([old, df])

        df.to_csv(FILE, index=False)

        st.success("🎉 Registered Successfully!")
        st.balloons()

    else:
        st.error("Fill all required fields")

st.divider()

st.page_link(
    "pages/Tournament.py",
    label="⬅️ Back",
    icon="♟️"
)
