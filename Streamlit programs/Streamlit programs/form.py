import streamlit as st
st.title("Form")
name=st.text_input("Enter your name")
email=st.text_input("Enter your email")
st.radio("Select your gender",["Male","Female"])
age=st.slider("Select your age",0,100)
col1,col2,col3=st.columns(3)
with col1:
     Date=st.selectbox("Select your date",list(range(1,32)))
with col2:
    Month=st.selectbox("Select your month",list(range(1,13)))
with col3:
    Year=st.selectbox("Select your year",list(range(1900,2027)))
agreement=st.checkbox("I agree to all the terms and conditions")
if agreement:
   st.button("Submit")
else:
   st.write("Please agree to the terms and conditions to submit the form")
