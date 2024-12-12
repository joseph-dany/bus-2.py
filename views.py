import streamlit as st
st.set_page_config(page_title="Businfoo",page_icon="bus")
st.sidebar.success("About")
about_page=st.Page("views/Ticket.py",
                        title="Ticket",
                        icon=":material/local_activity:",
                   default=True,)
project_1=st.Page("views/Timing.py",
                        title="Schedule",
                        icon=":material/event_available:",)

project_2=st.Page("views/Parcel.py",
                        title="Parcel",
                        icon=":material/package:",)

#pg = st.navigation(pages=[about_page,project_1,project_2])
pg = st.navigation({"Info":[about_page],
                    "Project":[project_1,project_2]})
st.logo("asets/joseph.jd.jpeg")
st.sidebar.text("Happy journey from jd 💕")
pg.run()
st.balloons()

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


st.title("Timing :mantelpiece_clock:")

st.subheader("Know the Timings of buses you want :dart:")
st.write("""
* Kurnool to Hyderabad :point_right:[k2h.list>](https://docs.google.com/spreadsheets/d/1Cts-Y6vJB_e55_YYZG_QUp3SzhmVQmehStqKdNWaxdk/edit?usp=sharing)
* Kurnool  to Bangalore:point_right:[k2b.list>](https://docs.google.com/spreadsheets/d/1vG5q_LBV-LhKcNnlHG9v6s9aHVuz14se6YGpf9G2alk/edit?usp=sharing)
* Kurnool to Tirupati :point_right:[k2t.list>](https://docs.google.com/spreadsheets/d/1Z0u5lpXS9tLtKOVISxjzjxqBFFwLbssayE7zh-sJSpQ/edit?usp=sharing)
* Kurnool to Vijayawada:point_right:[ktv.list>](https://docs.google.com/spreadsheets/d/1ictO8SNqlm27GCe8p0p7bS19fPHV-vCYNiVw6v6rcmM/edit?usp=sharing)""")
st.write("---")
st.write("May the timings can be delay but you can catch the bus with in or after 15-20 mins . We are assure you that be careful with online payment don't give or send money to unknown :thumbsup:")


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
