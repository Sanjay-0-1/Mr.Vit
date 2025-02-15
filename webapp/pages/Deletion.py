from navigation import make_sidebar
import streamlit as st
import auth_functions

make_sidebar()

st.header('Delete account:')
password = st.text_input(label='Confirm your password',type='password')
st.button(label='Delete Account',on_click=auth_functions.delete_account,args=[password],type='primary')