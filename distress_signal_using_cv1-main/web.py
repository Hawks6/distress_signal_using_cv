import pandas as pd
import plotly.express as px
import streamlit as st
import xlwings as xw
from PIL import Image
st.set_page_config(layout="wide")
header_left, header_mid, header_right = st.columns([1,3,1],gap = 'small')

with header_mid:
    st.title(':yellow[Police Dashboard]')


filepath = r"C:\Users\91823\Downloads\distress_signal_using_cv1-main\distress_signal_using_cv1-main\data.xlsx"




col1, col2 = st.columns(2)

ws = xw.Book(filepath).sheets['sheet']

x = ws.range("A1").value
y = ws.range("B1").value
with col1:
    st.title(':red[current status:]')

    if x + y == 2:
        st.header(':red[Potential Threat Detected!]')
        st.subheader("Attention Needed")
        st.write("Distress Signal Detected in your Vicinity\n\n\n")
        st.divider()
        st.header("Location:")
        st.subheader("Udaypalya")

    elif x + y == 1:
        st.header("New Alert Detected!!")
        st.divider()
        st.header("Location:")
        st.subheader("Udaypalya")
        st.divider()

    else:
        st.header(':yellow[No Attention Required]')

with col2:
    col3,col4=st.columns(2)

    if x + y > 0:
        st.header(':red[Snapshots]')
        with col3:

            image = Image.open(r'C:\Users\91823\Downloads\distress_signal_using_cv1-main\distress_signal_using_cv1-main\data\frameframe0.jpg')
            st.image(image, width=200)
            image1 = Image.open(r'C:\Users\91823\Downloads\distress_signal_using_cv1-main\distress_signal_using_cv1-main\data\frameframe20.jpg')
            st.image(image1, width=200)
            image2 = Image.open(r'C:\Users\91823\Downloads\distress_signal_using_cv1-main\distress_signal_using_cv1-main\data\frameframe40.jpg')
            st.image(image2, width=200)
        with col4:
            image3 = Image.open(r'C:\Users\91823\Downloads\distress_signal_using_cv1-main\distress_signal_using_cv1-main\data\frameframe60.jpg')
            st.image(image3, width=200)
            image4 = Image.open(r'C:\Users\91823\Downloads\distress_signal_using_cv1-main\distress_signal_using_cv1-main\data\frameframe80.jpg')
            st.image(image4, width=200)
            image5 = Image.open(r'C:\Users\91823\Downloads\distress_signal_using_cv1-main\distress_signal_using_cv1-main\data\frameframe100.jpg')
            st.image(image5, width=200)


    else:
        st.subheader("Snapshots \n from local surveillance cameras \n will be updated here in case of emergency")