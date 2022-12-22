import streamlit as st
from streamlit.logger import get_logger
from auth import login,signup

LOGGER = get_logger(__name__)

st.set_page_config(page_title="HealthCare System",page_icon="app\\logo.png")
st.title = "HealthCare System"
#st.sidebar.success("select a page")
st.markdown("# Main Page #")
st.sidebar.markdown("# Main Page #")

with st.sidebar:
    #st.image("logo.png")#app\\logo.png profile
    menu = ["Login", "SignUp"]
    choice = st.radio("LoginMenu", menu)
if choice == "Login":
    login()
    st.info("Dont have an account? ")
    if st.button(
        label="Sign up here"
    ): st.session_state.runpage()
elif choice == "SignUp":
    signup()





