import streamlit as st
def set_background_color(color: str):
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-color: {color};
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

def colored_text(text, color):
    st.markdown(f'<p style="color:{color};">{text}</p>', unsafe_allow_html=True)