import streamlit as st

# Title of the app
st.title("Simple Streamlit App")

# Input box
user_input = st.text_input("Enter some text:")

# Submit button
if st.button("Submit"):
    st.write("You entered:", user_input)