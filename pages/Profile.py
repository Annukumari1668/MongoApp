import streamlit as st
import pymongo
conn=pymongo.MongoClient("mongodb://127.0.0.1:27017/?directConnection=true&serverSelectionTimeoutMS=2000&appName=mongosh+2.8.2")
mydb=conn["ojt"]
my=mydb["user_info"]
col1,col2,col3=st.columns(3)
with col3:
    if st.button("Go to the previous page"):
        st.switch_page("main.py")
st.markdown("<h1 style='text-align:center;color:orange;'>🧠 BrainBoost</h1>",
            unsafe_allow_html=True)
if st.session_state.get("Username",False):
    st.write("You are safely inside the app!")
else:
    st.warning("⚠️First Login")
    st.stop()
@st.dialog("Change Password")
def cp():
    t1=st.text_input("enter the old password")
    t2=st.text_input("enter the new password")
    if st.button("Change Password"):
        my.update_one({"password":t1},{"$set":{"password":t2}})
        st.success("Password Changed successfully")
        st.balloons()
c1,c2,c3=st.columns(3)
st.success(f"Welcome:{st.session_state['Username']}")
#LOGOUT
if c1.button("Logout",use_container_width=True):
    del st.session_state["Username"]
    st.switch_page("main.py")
#PROFILE
if c2.button("see profile",use_container_width=True):
    str1=st.session_state["Username"]
    str2=st.session_state["Password"]
    res=my.find({"uname":str1,"password":str2})
    for i in res:
        st.success(f"Username={i['uname']}")
        st.success(f"Password={i['password']}")
        st.success(f"Mobile Number={i['mobile']}")
        st.success(f"Email Id={i['email']}")
        st.success(f"DOB={i['dob']}")

if c3.button("Change Password",use_container_width=True):
    cp()
   
    
   

