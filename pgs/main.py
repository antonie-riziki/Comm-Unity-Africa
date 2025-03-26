
import pandas as pd 
import streamlit as st 
import matplotlib.pyplot as plt 
import seaborn as sb 
import numpy as np 
import csv
import warnings
import folium


from streamlit_folium import st_folium



header = st.container()
body = st.container()
home_sidebar = st.container()


# header = st.container()
# home_sidebar = st.container()



with header:
	st.write("<h1 style='text-align: center; color: #38ACEC; margin-bottom: 1px;'>Comm-Unity Africa</h3>", unsafe_allow_html=True)
	st.write('''CommUnity Africa is an all-in-one communication and outreach platform designed to bridge the gap between businesses, organizations, and their communities across Africa. Our system empowers you to connect, engage, 
		and grow your audience seamlessly through Bulk SMS, Voice Calls, Chatbots, WhatsApp Messaging, Airtime Rewards, and USSD services — all in one powerful suite.''', unsafe_allow_html=True)
	st.image('./src/addiction-awareness-and-prevention-through-community-outreach.jpg')


with body:

	# ================== About Us ================== ================== #

	 st.write("<h3 style='text-align: left; color: #3EA99F; margin-bottom: 1px;'>About Us</h3>", unsafe_allow_html=True)

	 st.write('''At CommUnity Africa, we believe in the power of communication as the backbone of community development and business growth. Our platform offers businesses, NGOs, and institutions easy-to-use tools to reach 
	 	their audiences — even in remote areas without smartphones or internet access.
		\nWith features like bulk messaging, voice broadcasts, interactive chatbots, airtime rewards, and USSD services, we help you engage clients, gather feedback, run 
		campaigns, and strengthen customer relationships. Whether you're running a local business, a community-based organization, or a large enterprise, CommUnity Africa 
		is your trusted partner in building meaningful, inclusive, and impactful connections.

	 	''')



	# ================== Our Services ================== ================== #

	 st.write("<h3 style='text-align: left; color: #3EA99F; margin-bottom: 1px;'>Our Services</h3>", unsafe_allow_html=True)

	 sms, email, airtime = st.columns(3, vertical_alignment="center")
	 voice, vid_conf, promotion = st.columns(3, vertical_alignment="center")

	 with sms:
	 	st.image('./src/Bulk-sms.png', width=200)
	 	st.write("<h5 style='text-align: center; margin-bottom: 1px;'>Bulk SMS</h5>", unsafe_allow_html=True)
	 	# st.write('Enjoy our bulk sms services and reach to your audience within seconds')

	 with email: 
	 	st.image('./src/image1-3.png', width=200)
	 	st.write("<h5 style='text-align: center; margin-bottom: 1px;'>Email</h5>", unsafe_allow_html=True)
	 	# st.write('Enjoy our bulk sms services and reach to your audience within seconds')

	 with airtime:
	 	st.image('./src/airtime.png', width=200)
	 	st.write("<h5 style='text-align: center; margin-bottom: 1px;'>Airtime</h5>", unsafe_allow_html=True)
	 	# st.write('Enjoy our bulk sms services and reach to your audience within seconds')


	 with voice:
	 	st.image('./src/img_ill_traffic@2x1.png', width=200)
	 	st.write("<h5 style='text-align: center; margin-bottom: 1px;'>Voice over</h5>", unsafe_allow_html=True)
	 	# st.write('Enjoy our bulk sms services and reach to your audience within seconds')

	 with vid_conf:
	 	st.image('./src/6527718effb6ccecd3cffb24_Blog-feature-practical-workplace-tech.png', width=250)
	 	st.write("<h5 style='text-align: center; margin-bottom: 1px;'>Video Conferencing</h5>", unsafe_allow_html=True)
	 	# st.write('Enjoy our bulk sms services and reach to your audience within seconds')

	 with promotion: 
	 	st.image('./src/download (2).jpg', width=200)
	 	st.write("<h5 style='text-align: center; margin-bottom: 1px;'>Digital Marketing</h5>", unsafe_allow_html=True)
	 	# st.write('Enjoy our bulk sms services and reach to your audience within seconds')



	 # ================== Our Packages ================== ================== #

	 st.write("<h3 style='text-align: left; color: #3EA99F; margin-bottom: 1px;'>Our Packages</h3>", unsafe_allow_html=True)

	 st.image('./src/CommUnity Africa.png')

	 # free, premium, advance = st.columns(3)

	 # with free:
	 # 	st.image('./src/istockphoto-1208627394-612x612.jpg')

	 # with premium:
	 # 	st.image('./src/istockphoto-1208627394-612x612.jpg')

	 # with advance:
	 # 	st.image('./src/istockphoto-1208627394-612x612.jpg')



	 # ================== Our Partners ================== ================== #

	 st.write("<h3 style='text-align: left; color: #3EA99F; margin-bottom: 1px;'>Our Partners</h3>", unsafe_allow_html=True)
	 # st.write("<h6 style='text-align: left; margin-bottom: 1px;'>here are some of our partners</h6>", unsafe_allow_html=True)

	 col1, col2, col3, col4, col5 = st.columns(5)

	 with col1:
	 	st.image('./src/AT_Color-71519b9f-5507-4527-a596-45a7698d82b7.png', width=150)

	 with col2:
	 	st.image('./src/Fida-Kenya.jpg', width=150)

	 with col3:
	 	st.image('./src/download (3).png', width=150)

	 with col4:
	 	st.image('./src/pngimg.com - google_PNG19644.png', width=150)

	 with col5:
	 	st.image('./src/website-photo-5.png', width=150)





	 # ================== Our Clients ================== ================== #

	 st.write("<h3 style='text-align: left; color: #3EA99F; margin-bottom: 1px;'>Our Clients</h3>", unsafe_allow_html=True)
	 # st.write("<h6 style='text-align: left; margin-bottom: 1px;'>here are some of our customers</h6>", unsafe_allow_html=True)

	 col1, col2, col3, col4, col5 = st.columns(5)

	 with col1:
	 	st.image('./src/logo-without-bg-1.png', width=150)

	 with col2:
	 	st.image('./src/naivas-supermarket-logo-png_seeklogo-351966.png', width=150)

	 with col3:
	 	st.image('./src/KICTANET-Transparent-logo-1-1024x280.png', width=150)

	 with col4:
	 	st.image('./src/gertrudes_childrens_hospital_logo.jpg', width=150)

	 with col5:
	 	st.image('./src/kenia.397cdba4b70f1fe02af3fb034d2f2421.png', width=150)



	 # ================== Contact US ================== ================== #	

	 st.write("<h3 style='text-align: left; color: #3EA99F; margin-bottom: 1px;'>Contact Us</h3>", unsafe_allow_html=True)

	 loc_map, loc_text = st.columns(2)

	 with loc_map:

	 	# Coordinates for Africa's Talking HQ
	 	location = [-1.2921, 36.7765]

	 	# Create the folium map
	 	m = folium.Map(location=location, zoom_start=12)

	 	folium.Marker(
	 		location,
	 		popup="Comm-Unity Africa",
	 		tooltip="Click for more info",
	 		icon=folium.Icon(color="blue", icon="info-sign"),
	 		).add_to(m)

	 	st_folium(m, width=900, height=300)


	 with loc_text:
	 	st.write('')
	 	st.write('')
	 	st.write("<h6 style='text-align: left; margin-bottom: 1px;'>🏢 Apple Cross 23 - Lavington</h6>", unsafe_allow_html=True)
	 	st.write("<h6 style='text-align: left; margin-bottom: 1px;'>📬 P.O. Box 00200</h6>", unsafe_allow_html=True)
	 	st.write("<h6 style='text-align: left; margin-bottom: 1px;'>📌 Nairobi, Kenya</h6>", unsafe_allow_html=True)
	 	st.write("<h6 style='text-align: left; margin-bottom: 1px;'>📞 Tel: +254 71234 5678</h6>", unsafe_allow_html=True)
	 	st.write("<h6 style='text-align: left; margin-bottom: 1px;'>📧 Email: info@echominds.africa</h6>", unsafe_allow_html=True)



