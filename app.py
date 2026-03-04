# app.py

import streamlit as st
from data import tournaments

st.set_page_config(
    page_title="Nas Matrix Chess",
    layout="wide"
)

# Style
st.markdown("""
<style>
body {
    background-color:#020617;
    color:white;
}

.card {
    border:1px solid #1e293b;
    border-radius:12px;
    padding:20px;
    margin:10px;
}

.stButton>button {
    background:gold;
    color:black;
    font-weight:bold;
    border-radius:8px;
}
</style>
""", unsafe_allow_html=True)

# Header
st.markdown("""
<h1 style="text-align:center;">♟️ Nas Matrix Chess</h1>
<h4 style="text-align:center;color:gray;">
Official Chess Tournament Platform
</h4>
""", unsafe_allow_html=True)

st.divider()

# About
st.markdown("## 🏛️ About Us")

st.write("""
Nas Matrix Chess Association organizes professional
online and offline chess tournaments for all levels.
""")

st.divider()

# Tournaments
st.markdown("## 🏆 Upcoming Tournaments")

cols = st.columns(2)

i = 0

for key, t in tournaments.items():

    with cols[i % 2]:

        st.markdown(f"""
        <div class="card">
        <h3>{t["name"]}</h3>
        <p>📅 {t["date"]}</p>
        <p>💰 {t["fee"]}</p>
        </div>
        """, unsafe_allow_html=True)

        st.page_link(
            "pages/Tournament.py",
            label="View Details ♟️",
            icon="🏆"
        )

        st.session_state["current"] = key

    i += 1

st.divider()

# Footer
st.markdown("""
<p style="text-align:center;color:gray;">
© 2026 Nas Matrix Chess
</p>
""", unsafe_allow_html=True)
