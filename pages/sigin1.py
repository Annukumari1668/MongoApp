import streamlit as st
import mysql.connector
conn=mysql.connector.connect(host="127.0.0.1",user="root",database="stxaviers",passwd="")
my=conn.cursor()
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
    my.execute("select * from info where username="+"'"+t1+"'"+" and password="+"'"+t2+"'"+"")
    ans=my.fetchall()
    for i in ans:
        valid=valid+1
        st.session_state["Username"]=i[0]
        st.session_state["Password"]=i[1]
        st.switch_page("pages/Profile.py")
        st.success(f"Welcome:{i[0]}")
    if valid==0:
        st.success("Invalid User Login Details")

    

            
