import pandas as pd 
import soccerdata as sd
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
# player_profile_page = st.Page("./pgs/player_profile.py", title="player profile", icon=":material/group_search:")
# player_similarity_page = st.Page("./pgs/player_similarity_search.py", title="player similarity search", icon=":material/simulation:")
# team_comparison_page = st.Page("./pgs/team_comparison.py", title="team comparison", icon=":material/group_work:")
# team_profile_page = st.Page("./pgs/team_profile.py", title="team profile", icon=":material/groups:")
# match_prediction_page = st.Page("./pgs/match_prediction.py", title="match prediction", icon=":material/online_prediction:")
# test_page = st.Page("./pgs/test.py", title="test page", icon=":material/online_prediction:")



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



