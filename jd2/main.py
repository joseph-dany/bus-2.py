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