import streamlit as st
st.title("Fibonacci Series")
a = st.text_input(label="enter the value")
print(a)
if st.button("Submit"):
    try:
        num=int(a)
        if num<0 :
            st.write("Please enter a non-negative number")
        elif num==0 :
            st.write("Fibonacci term of 0 is :",0)
        else :
            fib_1,fib_2=0,1
            for i in range(num):
                fib_1,fib_2=fib_2,fib_1+fib_2
            st.write("Fibonacci term of ",num,"is :",fib_2)
    except ValueError:
        st.write("Please enter a valid number")