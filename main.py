import streamlit as st
import datetime
import pandas as pd
from io import BytesIO
from pyxlsb import open_workbook as open_xlsb
import io
buffer = io.BytesIO()

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

df = pd.DataFrame(get_record())

edited_df = st.data_editor(df)

new_time_in = edited_df.loc[edited_df["Time Out"].idxmax()]

if view_record:
    st.write(pd.DataFrame(get_record()))

# @st.cache_resource
# def convert_to_csv(df):
#     # IMPORTANT: Cache the conversion to prevent computation on every rerun
#     return df.to_csv(index=False).encode('utf-8')

# csv = convert_to_csv(df)

# with pd.ExcelWriter(buffer, engine='xlsxwriter') as writer:
#     # Write each dataframe to a different worksheet.
#     df.to_excel(writer, sheet_name='Sheet1', index=False)
#     writer.save()
#     download2 = st.download_button(
#         label="Download data as Excel",
#         data=buffer,
#         file_name='large_df.xlx',
#         mime='application/vnd.ms-excel'
#     )
