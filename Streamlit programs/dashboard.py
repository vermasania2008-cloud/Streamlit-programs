import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
st.title("Dashboard")
st.subheader("Overview of Student performance and analytics")
df=pd.read_csv("student.csv",sep=",")
tab1,tab2=st.tabs(["Dashboard","Filters"])
with tab1:
        col1,col2,col3,col4=st.columns(4) 
        with col1:
            with st.container(border=True):
             st.metric("🧑🏻‍🎓Total students",15)
        with col2:
            with st.container(border=True):
             st.metric("✅Passing students",13)
        with col3:
            with st.container(border=True):
             st.metric("❌Failing students",2)
        with col4:
            with st.container(border=True):
             st.metric("📊Average marks",86.7)
        fig1,fig2,fig3=st.columns(3)
        with fig1:
            with st.container(border=True):
                    stream_count=df["Stream"].value_counts()
                    chart1=px.pie(values=stream_count.values,names=stream_count.index,
                    title="📊 Streams ")
                    chart1.update_layout(height=300)
                    st.plotly_chart(chart1,use_container_width=True)
        with fig2:
                with  st.container(border=True):
                            Subjects = ["Maths", "English", "Punjabi", "Computer"]
                            average_marks=df[Subjects].mean()
                            chart2=px.bar(x=average_marks.index,y=average_marks.values, title="📊 Distribution of Marks"
                                        , labels={"x":"Subjects","y":"Average Marks"})
                            chart2.update_layout(height=300)
                            st.plotly_chart(chart2,use_container_width=True)

        with fig3:
                with st.container(border=True):
                        passing_students=df["Pass Status"].value_counts()
                        chart3=px.pie(values=passing_students.values,names=passing_students.index,hole=0.5,title="Pass&Fail")
                        chart3.update_layout(height=300)
                        st.plotly_chart(chart3,use_container_width=True)
        st.dataframe(df)
with tab2:
  city=st.selectbox("City ",["All","Amritsar","Jalandhar","Patiala"])
  if city!="All":
         df = df[df["City"] == city]
  
  subject=st.selectbox("Streams",["All","BCA","BSC.IT","BSC AI&ML"])
  if subject!="All":
         df = df[df["Stream"] == subject]
  
  marks=st.slider("Marks",0,100)
  df["Average Marks"] = df[Subjects].mean(axis=1)

  df = df[df["Average Marks"] >= marks]

  
  sort_by=st.radio("Order",["Ascending order","Descending order"])
  
  if sort_by=="Ascending order":
       df=df.sort_values("Average Marks", ascending=True)
  else:
       df=df.sort_values("Average Marks", ascending=False) 
st.dataframe(df)
