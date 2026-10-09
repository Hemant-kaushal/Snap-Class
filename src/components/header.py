import streamlit as st
import base64

def header_home():
    with open("/Users/hemantkaushal/Downloads/Snap_Class_logo.png", "rb") as f:
        img_data = base64.b64encode(f.read()).decode("utf-8")

    st.markdown(f"""
        <div style="display:flex; flex-direction:column; align-items:center; justify-content:center; margin-bottom:0px;">
            <img src='data:image/png;base64,{img_data}' style='height:170px;' />
            <h1 style='text-align:center; color:#E0E3FF'>SNAP<br/>CLASS</h1>
        </div>
    """, unsafe_allow_html=True)


def header_dashboard():

    with open("/Users/hemantkaushal/Downloads/Snap_Class_logo.png", "rb") as f:
        img_data = base64.b64encode(f.read()).decode("utf-8")

    st.markdown(f"""
        <div style="display:flex; align-items:center; justify-content:center; gap:10px">
            <img src='data:image/png;base64,{img_data}' style='height:75px;' />
            <h2 class='logo-heading' style='text-align:left;'>SNAP<br/>CLASS</h2>
        </div>
    """, unsafe_allow_html=True)

