import streamlit as st
import pymongo
conn=pymongo.MongoClient("mongodb+srv://Annukumari:Annu2026@annuwork.zo36zb2.mongodb.net/?appName=AnnuWork")
mydb=conn["ojt"]
my=mydb["user_info"]
col1,col2,col3=st.columns(3)
with col3:
    if st.button("Go to the previous page"):
        st.switch_page("main.py")
st.markdown("<h1 style='text-align:center;color:gold;'>🔐Sigin/Login</h1>",unsafe_allow_html=True)
t1=st.text_input("Username")
t2=st.text_input("Password",type="password")
b1=st.button("🔑 Sign In")
valid=0
if b1:
    ans=my.find({"uname":t1,"password":t2})
    for i in ans:
        valid=valid+1
        st.session_state["Username"]=i['uname']
        st.session_state["Password"]=i['password']
        st.switch_page("pages/Profile.py")
        st.success(f"Welcome:{i[0]}")
    if valid==0:
        st.success("Invalid User Login Details")

    

            
