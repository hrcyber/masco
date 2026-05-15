import streamlit as st

# Page ka title set karne ke liye
st.title("My First Streamlit App")

# Text display karne ke liye
st.write("Hello, World!")

# Ek simple button aur interactivity ke liye
if st.button('Click Me'):
    st.success("Welcome to Streamlit!")