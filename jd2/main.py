import streamlit as st
from jd1 import Parce , Ticket , Timimg 
st.set_page_config(page_title="Businfoo",page_icon="bus")
st.sidebar.success("About")
about_page=st.Page("jd1/Ticket.py",
                        title="Ticket",
                        icon=":material/local_activity:",
                   default=True,)
project_1=st.Page("jd1/Timing.py",
                        title="Schedule",
                        icon=":material/event_available:",)

project_2=st.Page("jd1/Parcel.py",
                        title="Parcel",
                        icon=":material/package:",)

#pg = st.navigation(pages=[about_page,project_1,project_2])
pg = st.navigation({"Info":[about_page],
                    "Project":[project_1,project_2]})
#st.logo("asets/joseph.jd.jpeg")
st.sidebar.text("Happy journey from jd 💕")
st.balloons()
