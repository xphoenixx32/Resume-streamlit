import streamlit as st

def txt(a,b):
    col1, col2 = st.columns([3,1])
    with col1:
        st.markdown(a)
    with col2:
        st.markdown(b)