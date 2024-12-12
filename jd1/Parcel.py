import streamlit as st
#import streamlit as st

from forms import contact
from forms.contact import contact_form


@st.dialog("Contact me")
def show_contact_form():
    contact_form()

st.title("Businfoo! :trolleybus:")
col1,col2=st.columns(2,gap="small")
with col1:
    st.image("./asets/jd.1.jpeg",width=230)
with col2:
    st.title("BOOK YOUR TICKETS NOW HURRY!!:runner:")
    st.link_button("Book now","https://forms.gle/mVnYjupNxDw9qB4r7")
    #if st.button("Book now"):

    #    show_contact_form()
with st.container():
    st.write("##")
    st.write("---")
    st.write("""You can book your ticket fast and easily. Ticket Booking
    
* Enable online booking of bus tickets.
* various payment options (credit/debit cards, digital wallets, etc.).
* Provide ticket confirmation and cancellation options.
* Send ticket confirmation and cancellation notifications via email.
""")
with st.container():
    st.write("---")
    st.write("""We are providing buses for major cities and towns.
    
* Kurnool to Hyderabad:point_up:(per 1 person ₹500 or less) :heavy_check_mark: [knl2hyd>](https://docs.google.com/document/d/1VE-exHtmttXyIVCHgh7WsoeyiCtmtCPXvTDn19SX0lY/edit?usp=sharing) 
* Kurnool  to Bangalore:point_up:(per 1 person ₹1180 or less) :heavy_check_mark:[knl2beng>](https://docs.google.com/document/d/1VE-exHtmttXyIVCHgh7WsoeyiCtmtCPXvTDn19SX0lY/edit?usp=sharing)
* Kurnool to Tirupati :point_up:(per 1 person ₹453 or less):heavy_check_mark:[knl2trp>](https://docs.google.com/document/d/1VE-exHtmttXyIVCHgh7WsoeyiCtmtCPXvTDn19SX0lY/edit?usp=sharing)
* Kurnool to Vijayawada :point_up:(per 1 person ₹955 or less):heavy_check_mark: [knl2vjwd>](https://docs.google.com/document/d/1VE-exHtmttXyIVCHgh7WsoeyiCtmtCPXvTDn19SX0lY/edit?usp=sharing)
     
By clicking the link you need to pay for tickets .After payment we will get connected with you about ticket and pickup .""")
with st.container():
    st.write("---")
    st.write("By filling the google form we can update you about your seat , price and details, we can send you in whatsapp about the payment and we will inform you further.Have a safe and nice journey")
with st.container():
    st.write("Any illegal and other activities are occur you can contact us without hesitation .Avoid stacking multiple site alerts. If you need to convey more than one message, provide a list of links within a single site alert instead of multiple, stacked alerts.")
if st.button("contact me"):
    show_contact_form()
st.title("Parcel :package: ")

with st.container():
    st.write("We are providing parcel facility which makes easier to send the parcels")
colo1,colo2=st.columns(2,gap="small")
with colo1:
    st.image("./asets/jd.2.jpeg",width=230)
with colo2:
    st.title("Send the Parcel :incoming_envelope:")
    st.write("just click the button to send the parcel and fill the details complete the payment process to get notification about the parcel tracking")
    st.link_button("send parcel","https://forms.gle/pec69CtXypbGfe6K6")
with st.container():
    st.write("___")
    st.subheader("Parcel Enquiry :mag:")
    st.write("We are providing parcel delivery through bus transport which is easy way to send something important.Bus parcel delivery is a budget-friendly option for sending parcels within India. It leverages the extensive network of bus routes to reach various locations. While it might not offer the speed of express courier services, it provides a reliable and secure way to transport parcels. However, limited tracking options and potential for damage during transit are factors to consider. By choosing a reputable bus service and packing items securely, you can effectively utilize bus parcel delivery for your shipping needs.")
