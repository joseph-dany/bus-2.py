import streamlit as st
def contact_form():
    with st.form("contact_form"):
        name=st.text_input("First Name")
        number=st.text_input("Contact number")
        present=st.text_input("From")
        where=st.text_input("To where")
        msg=st.text_area("Your message")
        submit_but=st.form_submit_button("submit")

        if submit_but:
            st.success("Message successfully sent!")
