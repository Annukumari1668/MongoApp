import streamlit as st
col1, col2, col3 = st.columns(3)
with col3:
    if st.button("Go to previous page"):
        st.switch_page("main.py")
if st.session_state.get("Username",False):
    st.write("You are safely inside the app!")
else:
    st.warning("⚠️First Login !!!")
    st.stop()
st.markdown("<h1 style='text-align:center;color:orange;'>🔢 Number Programs</h1>",
     unsafe_allow_html=True)
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
col1, col2, col3 = st.columns(3)
with col1:
    st.markdown("""
    <div class="card">
        <h3>🔢 Prime Number</h3>
        <p>Theory, Code, Working</p>
    </div>
    """, unsafe_allow_html=True)
    if st.button("Open",key="num"):
        st.switch_page("pages/prime.py") 
    
