import streamlit as st
col1,col2,col3=st.columns(3)
with col3:
    if st.button("Go to previous page"):
        st.switch_page("pages/number.py")
st.markdown("<h1 style=text-align:center;color:orange;'>🔢 Prime Number</h1>",unsafe_allow_html=True)
if st.session_state.get("Username",False):
    st.write(" ")
else:
    st.warning("⚠️First Login !!!")
    st.stop()
st.markdown("""<h2 style=text-align:left;
                      text-decoration:underline;'>
                      📖Theory:</h2>
                      """,unsafe_allow_html=True)
st.markdown("""<h4>
# A prime number is a natural number greater thaan 1 that
has exactly two positive factor:<br>
•first- 1<br>
•second- the number itself<br>
<br># if a number has more than two factors,it is called a
Composite number.<br>
example:2,3,5,7 etc.<br>
<br># Note:2 is the only even prime number and 1 is neither
prime nor composite.

</h4>""",unsafe_allow_html=True)
st.write(" ")
st.markdown("""<h3 style=text-align:left;'>
💻 Code:</h3>""",unsafe_allow_html=True)
with st.expander("💻see the code"):
        st.code("""
import streamlit st
st.header("check a number is Prime or not")
n=st.slider("Pick a number")
    if st.button("check"):
        c=0
        for i in range(1,n+1):
            if n%i==0:
                c=c+1
        if c==2:
            st.success(f"{n} is prime number")
        else:
            st.success(f"{n} is  not prime number")
        """)
st.markdown("<h3 style=text-align:left;'>🚀 Working:</h3>",unsafe_allow_html=True)
st.subheader("Check a number is Prime or Not")
n=st.slider("Pick a number")
if st.button("check"):
    c=0
    for i in range(1,n+1):
        if n%i==0:
            c=c+1
    if c==2:
        st.success(f"{n} is prime number")
    else:
        st.success(f"{n} is  not prime number")
