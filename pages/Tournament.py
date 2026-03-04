# pages/Tournament.py

import streamlit as st
from data import tournaments

st.set_page_config(page_title="Tournament")

key = st.session_state.get("current", "main")

t = tournaments[key]

st.title("🏆 " + t["name"])

st.divider()

st.write("📅 Date:", t["date"])
st.write("🌐 Mode:", t["mode"])
st.write("♟️ Platform:", t["platform"])
st.write("💰 Fee:", t["fee"])
st.write("⏱️ Time:", t["time"])

st.divider()

st.markdown("## 📖 About")
st.write(t["about"])

st.divider()

# Buttons
st.page_link(
    "pages/Register.py",
    label="📝 Register Now",
    icon="📝"
)

st.page_link(
    "app.py",
    label="⬅️ Back Home",
    icon="🏠"
)
