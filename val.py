import streamlit as st
st.title("Number Validator")
a=st.text_input(label="Enter a variable or number")
print(a)
if st.button("Submit"):
    num= a
    if num.isdigit() or num.isalpha() :
        st.write("Yes, the input is valid")
    else :
        st.write("No, the input is not valid")