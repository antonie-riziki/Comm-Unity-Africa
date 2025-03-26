import pandas as pd 
import streamlit as st 
import matplotlib.pyplot as plt 
import seaborn as sb 
import numpy as np  
import csv
import os
import warnings

reg_page = st.Page("./pgs/registration.py", title="register", icon=":material/thumb_up:")
signin_page = st.Page("./pgs/signin.py", title="sign in", icon=":material/thumb_down:")
home_page = st.Page("./pgs/main.py", title="home page", icon=":material/house:")
hub_page = st.Page("./pgs/hub.py", title="hub", icon=":material/query_stats:")
chatbot_page = st.Page("./pgs/chatbot.py", title="chatbot", icon=":material/chat:")



pg = st.navigation([reg_page, signin_page, home_page, hub_page, chatbot_page])



st.set_page_config(
    page_title="CommUnity Africa",
    page_icon="🗺️",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        'Get Help': 'https://www.echominds.africa',
        'Report a bug': "https://www.echominds.africa",
        'About': "# Driving Impact Through Communication \nTry *CommUnity Africa* and experience reality!"
    }
)

st.logo('./src/224916.png')

pg.run()



