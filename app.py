import streamlit as st
import pathlib
import pandas as pd

def load_css(file_path):
    with open (file_path) as f:
        st.html(f"<style>{f.read()}</style>")

css_path=pathlib.Path("/Users/darshanpoojary/AskMyDoc/assets/styles.css")
load_css(css_path)

st.markdown("""
            <div class='my-title'>
            <h1>AskMyDoc</h1>
            </div>
            """,
            unsafe_allow_html=True)
st.markdown(
    """<div class='my-subheader'>
    <h3> RAG Implementation Testing!!</h3>
    </div>
""",unsafe_allow_html=True
)
st.markdown(
    """<div class='stApp'>
    </div>
""",unsafe_allow_html=True
)
df=st.file_uploader(" ")
if df:
    df=pd.read_csv(df)
    st.write(df.head())
    
