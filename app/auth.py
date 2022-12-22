import streamlit as st
#import streamlit_authenticator
import hashlib
from database import insert_user,get_user

def signup():
    st.subheader("Create New Account")
    new_user = st.text_input("Username")
    new_password = st.text_input("Password", type='password')
    new_password = hashlib.sha256(new_password.encode('utf-8')).hexdigest()
    new_age = st.text_input("Age")
    new_email = st.text_input("Email")
    gender = ['Male','Female','Other']
    new_gender = st.radio('',gender)
    insurance = ['Yes','No']
    new_insurance = st.radio('',insurance)
    new_surname = st.text_input("Surname")
    new_other_name = st.text_input("Other Name")
    new_phone_number = st.text_input("Phone Number")
    role = ['Patient','Doctor','Nurse']
    new_role = st.radio('',role)
    if st.button("Sign Up"):
        insert_user(
            username=new_user,
            password=new_password,
            age=new_age,
            email=new_email,
            gender=new_gender,
            insurance=new_insurance,
            surname=new_surname,
            other_name=new_other_name,
            phone_number=new_phone_number,
            role=new_role.lower()# type: ignore
        )
        st.success("You have successfully created a valid Account continue to login")

def login():
    st.subheader("Login Section")
    username = st.text_input("User Name")
    password = st.text_input("Password", type='password')
    role = ['Patient','Doctor','Nurse']
    new_role = st.radio('',role)

    if st.button("Login"):
        user = get_user(username,password)
        if user:
            if new_role == user['role']:
                st.success("Logged In as {}".format(username))
            st.error('Role isn\'t correct')

