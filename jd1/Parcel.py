import streamlit as st
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
