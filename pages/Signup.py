import streamlit as st
import pymongo
conn=pymongo.MongoClient("mongodb+srv://Annukumari:Annu2026@annuwork.zo36zb2.mongodb.net/?appName=AnnuWork")

mydb=conn["ojt"]
my=mydb["user_info"]
col1,col2,col3=st.columns(3)
with col3:
    if st.button("Go to the previous page"):
        st.switch_page("main.py")
st.markdown("""<h1 style='text-align:center;
            color:deeppink;'>👤➕SIGN UP</h1>""",unsafe_allow_html=True)
t1=st.text_input("Username")
t2=st.text_input("Password",type="password")
t3=st.text_input("Mobile number")
t4=st.text_input("Email Id")
t5=st.date_input(
    "DOB", 
    value=date.today(), 
    min_value=date(1900, 1, 1), 
    max_value=date(2025, 12, 31)
)
b= st.button("SIGN UP")
if b:
    my.insert_one({"uname":t1,"password":t2,"mobile":str(t3),"email":t4,"dob":str(t5)});
    st.success("✅Sign up Successfully")
    st.balloons()
    





