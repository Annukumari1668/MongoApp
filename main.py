import streamlit as st
col1,col2,col3,col4,col5=st.columns(5)
with col1:
    if st.button("👤➕SINGUP"):
        st.switch_page("pages/Signup.py")
with col3:
    if st.button("🔐SIGNIN/LOGIN"):
        st.switch_page("pages/signin.py")
with col5:
     if st.button("👤PROFILE"):
         st.switch_page("pages/Profile.py")
        


st.set_page_config(page_title="BrainBoost", layout="wide")

# Custom CSS
st.markdown("""
<style>
.card {
    padding: 20px;
    border-radius: 15px;
    background-color: #262730;
    text-align: center;
    box-shadow: 2px 2px 10px rgba(0,0,0,0.3);
}
.card h3 {
    color: orange;
}
</style>
""", unsafe_allow_html=True)

# Title
st.markdown("<h1 style='text-align:center;color:orange;'>🧠 BrainBoost</h1>",
            unsafe_allow_html=True)

st.markdown("<h4 style='text-align:center;'>Learn Python with Easy Programs</h4>",
            unsafe_allow_html=True)

st.write("")

# Cards
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    <div class="card">
        <h3>🔢 Number Programs</h3>
        <p>Prime, Armstrong, Palindrome</p>
    </div>
    """, unsafe_allow_html=True)
    if st.button("Open",key="num"):
        st.switch_page("pages/number.py") 

with col2:
    st.markdown("""
    <div class="card">
        <h3>⭐ Pattern Programs</h3>
        <p>Triangle, Pyramid, Diamond</p>
    </div>
    """, unsafe_allow_html=True)

    if st.button("Open", key="pat"):
        st.session_state.page = "pattern"

with col3:
    st.markdown("""
    <div class="card">
        <h3>📈 Series Programs</h3>
        <p>Fibonacci, Prime Series</p>
    </div>
    """, unsafe_allow_html=True)

    if st.button("Open", key="ser"):
        st.session_state.page = "series"
with col1:
    st.markdown("""
    <div class="card">
        <h3>🔢 Loops</h3>
        <p>For lopp,While loop</p>
    </div>
    """, unsafe_allow_html=True)

    if st.button("Open", key="loop"):
        st.session_state.page = "Loops"
