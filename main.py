import streamlit as st
import datetime
import pandas as pd

@st.cache_resource

def get_record():
    return []

def timeIn_funct():
    times = []
    for hours in range(0, 23):
        for minutes in range(0, 59):
            times.append(datetime.time(hours, minutes))
    timeIn_output=st.selectbox("Time In", times, key="timeIn", format_func=lambda t: t.strftime("%H:%M"))
    return timeIn_output


def timeOut_funct():
    times = []
    for hours in range(0, 23):
        for minutes in range(0, 59):
            times.append(datetime.time(hours, minutes))
    timeOut_output=st.selectbox("Time Out", times, key="timeOut", format_func=lambda t: t.strftime("%H:%M"))
    return timeOut_output
    
visitor_name = st.text_input('Visitor Name', key="name")

date = st.date_input('Date', key="date")

timeIn = timeIn_funct()

timeOut = timeOut_funct()

telephone = st.text_input('Telephone', key="tel")

address = st.text_input('Address', key="address")

purpose = st.text_input('Purpose of Visit', key="purpose")

department = st.selectbox('Select Department', ['None', 'IT', 'Marketing', 'Faults', 'HR'], key="dept")


def clearForm():
    st.session_state.name = ""
    st.session_state.tel = ""
    st.session_state.address = ""
    st.session_state.purpose = ""
    st.session_state.dept = "None"



add_new_info_button = st.button('Submit Visitor Info')

view_record = st.button('View Records')

clr_form_btn = st.button('New Form', on_click=clearForm)

if add_new_info_button:
    get_record().append({"Date": date, "Visitor Name": visitor_name, "Telephone": telephone, "Address": address, "Purpose":purpose, "Department": department, "Time In": timeIn, "Time Out": timeOut})

if view_record:
    st.write(pd.DataFrame(get_record()))




