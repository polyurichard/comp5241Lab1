import streamlit as st

# Initialize session state for storing past inputs
if 'text_history' not in st.session_state:
    st.session_state.text_history = []

# Create a text input box
text_input = st.text_input("Enter some text:")

# Create a submit button
submit_button = st.button("Submit")
if submit_button:
    st.session_state.text_history.append(text_input)
    st.write("You've inputted:", text_input)
    st.session_state.input_box = ""  # Clear the input box

# Create a clear button
clear_button = st.button("Clear History")
if clear_button:
    st.session_state.text_history = []

# Display the list of past submitted input
st.write("## Past inputs")
for text in st.session_state.text_history:
    st.write(text)
