
import streamlit as st

# Create a title and description for your form
st.title("Google Form-like App")
st.write("This is a simple form-like interface created with Streamlit.")

# Create input fields
name = st.text_input("Name", "")
email = st.text_input("Email", "")
age = st.number_input("Age", 0, 100, 0)
comment = st.text_area("Comments", "")

# Create a button to submit the form
if st.button("Submit"):
    # Process the form data (you can save it to a database or perform any other action)
    st.write("Name:", name)
    st.write("Email:", email)
    st.write("Age:", age)
    st.write("Comments:", comment)

# You can add more form fields as needed