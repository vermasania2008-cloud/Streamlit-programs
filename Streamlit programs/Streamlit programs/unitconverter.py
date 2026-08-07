import streamlit as st
st.title("Unit converter")
st.sidebar.title("Conversion options")
category=st.sidebar.selectbox("What do u want to convert?",["Length","Weight","Time","Temperature","Speed","Data storage"])
given=st.text_input("Enter the value to convert")
if category=="Length":
   selected=st.selectbox("Units",["Meter->Kilometer","Kilometer->Meter","Centimeter->Meter","Meter->Centimeter","Inch->Centimeter","Centimeter->Inch","Feet->Meter","Meter->Feet"])        
elif category=="Weight":
     selected=st.selectbox("Units",["Kilogram->Gram","Gram->Kilogram","Pound->Kilogram","Kilogram->Pound"])
elif category=="Time":    
    selected=st.selectbox("Units",["Second->Minute","Minute->Second","Hour->Minute","Minute->Hour","Day->Hour","Hour->Day"])
elif category=="Temperature":
    selected=st.selectbox("Units",["Celsius->Fahrenheit","Fahrenheit->Celsius","Celsius->Kelvin","Kelvin->Celsius"])
elif category=="Speed":
    selected=st.selectbox("Units",["Kilometer/hour->Meter/second","Meter/second->Kilometer/hour"])
elif category=="Data storage":
    selected=st.selectbox("Units",["KB->MB","MB->KB","MB->GB","GB->MB"])
else:
    st.write("Please select a category to convert")

clicked=st.button("Enter") 
answer=None  

if category=="Length" and clicked:
    if selected=="Meter->Kilometer":
       answer= (float(given)/1000)
    elif selected=="Kilometer->Meter":
       answer= (float(given)*1000) 
    elif selected=="Centimeter->Meter":
       answer=(float(given)/100)
    elif selected=="Meter->Centimeter":
       answer= (float(given)*100)
    elif selected=="Inch->Centimeter":
       answer= (float(given)*2.54)
    elif selected=="Centimeter->Inch":
       answer= (float(given)/2.54)
    elif selected=="Feet->Meter":
       answer=(float(given)*0.3048)
    elif selected=="Meter->Feet":
        answer=(float(given)/0.3048)
if category=="Weight" and clicked:
    if selected =="Kilogram->Gram":
        answer=(float(given)*1000)
    elif selected=="Gram->Kilogram":
        answer=(float(given)/1000)
    elif selected=="Pound->Kilogram":
        answer=(float(given)*0.453592)
    elif selected=="Kilogram->Pound":
        answer=(float(given)/0.453592)
if category =="Time" and clicked:
    if selected=="Second->Minute":
        answer=(float(given)/60)
    elif selected=="Minute->Second":
        answer=(float(given)*60)
    elif selected=="Hour->Minute":
        answer=(float(given)*60)
    elif selected=="Minute->Hour":
        answer=(float(given)/60)
    elif selected=="Day->Hour":
        answer=(float(given)*24)
    elif selected=="Hour->Day":
        answer=(float(given)/24)
if category=="Temperature" and clicked:
    if selected=="Celsius->Fahrenheit":
        answer=((float(given)*9/5)+32)
    elif selected=="Fahrenheit->Celsius":
        answer=((float(given)-32)*5/9)
    elif selected=="Celsius->Kelvin":
        answer=(float(given)+273.15)
    elif selected=="Kelvin->Celsius":
        answer=(float(given)-273.15)
if category=="Speed" and clicked:
    if selected=="Kilometer/hour->Meter/second":
        answer=(float(given)/3.6)
    elif selected=="Meter/second->Kilometer/hour":
        answer=(float(given)*3.6)
if category=="Data storage" and clicked:
    if selected=="KB->MB":
        answer=(float(given)/1024)
    elif selected=="MB->KB":
        answer=(float(given)*1024)
    elif selected=="MB->GB":
        answer=(float(given)/1024)
    elif selected=="GB->MB":
        answer=(float(given)*1024)
if selected =="":
    st.write("Please select a unit to convert")
if answer is not None:
   st.write(" Answer is :",answer)
