import streamlit as st
import pandas as pd
import africastalking
import os
import sys
import requests
import google.generativeai as genai
import smtplib

from email.mime.text import MIMEText
from st_audiorec import st_audiorec

from streamlit_lottie import st_lottie
from streamlit.components.v1 import html
# from streamlit_drawable_canvas import st_canvas

sys.path.insert(1, './models')
print(sys.path.insert(1, '../models/'))

from gen_ai_models import generate_auto_message

from dotenv import load_dotenv

load_dotenv()

genai.configure(api_key = os.getenv("GOOGLE_API_KEY"))

africastalking.initialize(
    username='EMID',
    api_key = os.getenv("AT_API_KEY")
)

sms = africastalking.SMS
airtime = africastalking.Airtime


def send_bulk_message(community, df, final_message):

    sms = africastalking.SMS

    for get_phone_number in df['phone_numbers']:

        # phone_number = [743158232]

        recipients = [f"+254{str(get_phone_number)}"]

        # airtime_rec = "+254" + str(phone_number)

        print(recipients)
        print(get_phone_number)
        print(community)

        # Set your message
        
        message = f"{community.upper()} \n{final_message}.";

        # Set your shortCode or senderId
        sender = 20880

        try:
            # responses = airtime.send(phone_number=airtime_rec, amount=amount, currency_code=currency_code)
            response = sms.send(message, recipients, sender)

            st.toast(f"Message sent Successfully")

            print(response)

            # print(responses)

        except Exception as e:
            st.toast(f"Message not sent. Contact admin ")
            print(f'Houston, we have a problem: {e}')


def send_bulk_airtime(amount, df):

    airtime = africastalking.Airtime

    for get_phone_number in df['phone_numbers']:

        currency_code = "KES"

        airtime_rec = "+254" + str(get_phone_number)

        print(airtime_rec)
        print(get_phone_number)
        

        # Set your shortCode or senderId
        sender = 20880

        try:
            responses = airtime.send(phone_number=airtime_rec, amount=amount, currency_code=currency_code)

            st.toast(f"Airtime sent Successfully")

            print(responses)

        except Exception as e:
            st.toast(f"Airtime not sent. Contact admin ")
            print(f'Houston, we have a problem: {e}')

    


@st.dialog("AI Generated Text")
def get_auto_params(item):
    alert_message = st.text_input(label=f'more information about the {item}')
    more_infor_btn = st.button('Generate')

    if 'response' not in st.session_state:
        st.session_state.response = "No message yet."
    
    if more_infor_btn==True:
        st.session_state.response = generate_auto_message(alert_message)

    return st.session_state.response

header = st.container()
community_projects = st.container()
contents = st.container()
body = st.container()


with header:
    st.image('./src/community-outreach.jpg', width=1900)

with community_projects:
    col1, col2, col3, col4 = st.columns(4)

    with col1:
        social_welfare = st.button(label='Social Welfare', icon='📢', use_container_width=True)
        

    with col2:
        healthcare = st.button(label='Healthcare', icon='🏥', use_container_width=True)
        

    with col3:
        skills_ed = st.button(label='Skills & Education', icon='🎒', use_container_width=True)
        

    with col4:
        infrastructure = st.button(label='Infrastructure', icon='🏗️', use_container_width=True)
        
 # ======================================================================= #

    if social_welfare:
        with contents:
            st.write('This is the social welfare section')

    elif healthcare:
        with contents:
            st.write('This is the healthcare section')

    elif skills_ed:
        with contents:
            st.write('This is the Skills and Education section')

    elif infrastructure:
        with contents:
            st.write('This is the InfrastructureS section')

    else:
        with contents:
            st.write('')

 # ========================================================================= #

    col1, col2 = st.columns(2)

    with col1:
        community_name = st.text_input("Community | Project | Ministry | Association", key='community_name')

    with col2:
        st.write('')
        st.write('')
        community_name_submit_button = st.button('Submit')



with body:
     sms, email, airtime, voice, vid_conf, promotion = st.tabs(['🗃️ Bulk SMS','📧 Email', '📶 Airtime', '📡 Audio', '📽️ Video Conference', '🎯 Advertisements'])

     with sms:
        # sms_btn = st.button('bulk sms')
        
        sms_category_option = ['Alert','Notice', 'Event', 'Announcement', 'Meetup']
        sms_category = st.selectbox(label='select message category', options=sms_category_option)


        # ====================== Alert Section ================================ #

        if sms_category == 'Alert':
            alerts_body, alert_image = st.columns(2, vertical_alignment="top")

            with alerts_body:

                st.write(f"<h3 style='text-align: left; color: #3EA99F;'>🛗 {community_name}<h3>", unsafe_allow_html=True)

                csv_imp, attach_contact = st.columns(2)

                with csv_imp:
                    import_contacts = st.button('upload contacts', icon=':material/upload_file:', use_container_width=True)

                with attach_contact:
                    open_contacts = st.button('import', icon=':material/add_call:', use_container_width=True)

                recipients_number, add_num = st.columns([5, 1])
                
                with recipients_number:
                    # get_number = st.number_input('', value=0, min_value=0, max_value=int(10e10), key="number1")

                    contact_list = []

                    if 'number_count' not in st.session_state:
                        st.session_state.number_count = 1

                    for i in range(st.session_state.number_count):
                        get_number = st.number_input(label='', min_value=0, max_value=int(10e10), key=f'number_{i}')
                        contact_list.append(get_number)

                    df = pd.DataFrame({'phone_numbers':contact_list})
                    st.dataframe(df.head())
                    


                with add_num:
                    
                    st.write('')
                    st.write('')
                    add_num_btn = st.button(label="", icon=':material/add_call:')

                    remove_num_btn = st.button(label="", icon=':material/phone_forwarded:')

                    if add_num_btn:
                        st.session_state.number_count += 1

                    if remove_num_btn and st.session_state.number_count > 1:
                        st.session_state.number_count -= 1


                ai_generated_text = st.button('Hub-AI', icon='🪄')
                alert_message = st.text_area('write your alert message here...')

                if ai_generated_text:
                    alert_message = get_auto_params(sms_category)

                alert_message = alert_message

                send_message = st.button(label='send message ', icon=':material/send:')

                if send_message==True:
                    send_bulk_message(community_name, df, alert_message)



            with alert_image:
                st.image('./src/alert-design-template-a47c54921c5fd69591ac6dc693c34784_screen.jpg', width=500)


        # ====================== Notice Section ================================ #

        elif sms_category == 'Notice':

            notice_body, notice_image = st.columns(2, vertical_alignment="top")

            with notice_body:

                st.write(f"<h3 style='text-align: left; color: #3EA99F;'>🛗 {community_name}<h3>", unsafe_allow_html=True)

                csv_imp, attach_contact = st.columns(2)

                with csv_imp:
                    import_contacts = st.button('upload contacts', icon=':material/upload_file:', use_container_width=True)

                with attach_contact:
                    open_contacts = st.button('import', icon=':material/add_call:', use_container_width=True)

                recipients_number, add_num = st.columns([5, 1])
                
                with recipients_number:
                    # get_number = st.number_input('', value=0, min_value=0, max_value=int(10e10), key="number1")

                    contact_list = []

                    if 'number_count' not in st.session_state:
                        st.session_state.number_count = 1

                    for i in range(st.session_state.number_count):
                        get_number = st.number_input(label='', min_value=0, max_value=int(10e10), key=f'number_{i}')
                        contact_list.append(get_number)

                    df = pd.DataFrame({'phone_numbers':contact_list})
                    st.dataframe(df.head())



                with add_num:
                    
                    st.write('')
                    st.write('')
                    add_num_btn = st.button(label="", icon=':material/add_call:')

                    remove_num_btn = st.button(label="", icon=':material/phone_forwarded:')

                    if add_num_btn:
                        st.session_state.number_count += 1

                    if remove_num_btn and st.session_state.number_count > 1:
                        st.session_state.number_count -= 1

                ai_generated_text = st.button('Hub-AI', icon='🪄')
                notice_message = st.text_area('write your alert message here...')

                if ai_generated_text:
                    alert_message = get_auto_params(sms_category)
                                    

                send_message = st.button(label='send message ', icon=':material/send:')

                if send_message==True:
                    send_bulk_message(community_name, df, notice_message)

            with notice_image:
                st.image('./src/images (1).png', width=500)


        # ====================== Events Section ================================ #

        elif sms_category == 'Event':

            event_feature, event_image = st.columns(2)

            with event_feature:

                csv_imp, attach_contact = st.columns(2)

                with csv_imp:
                    import_contacts = st.button('upload contacts', icon=':material/upload_file:', use_container_width=True)

                with attach_contact:
                    open_contacts = st.button('import', icon=':material/add_call:', use_container_width=True)

                recipients_number, add_num = st.columns([5, 1])
                
                with recipients_number:
                    # get_number = st.number_input('', value=0, min_value=0, max_value=int(10e10), key="number1")

                    contact_list = []

                    if 'number_count' not in st.session_state:
                        st.session_state.number_count = 1

                    for i in range(st.session_state.number_count):
                        get_number = st.number_input(label='', min_value=0, max_value=int(10e10), key=f'number_{i}')
                        contact_list.append(get_number)

                    df = pd.DataFrame({'phone_numbers':contact_list})
                    st.dataframe()

                with add_num:
                    
                    st.write('')
                    st.write('')
                    add_num_btn = st.button(label="", icon=':material/add_call:')

                    remove_num_btn = st.button(label="", icon=':material/phone_forwarded:')

                    if add_num_btn:
                        st.session_state.number_count += 1

                    if remove_num_btn and st.session_state.number_count > 1:
                        st.session_state.number_count -= 1


                filter_date_col1, filter_date_col2 = st.columns(2)

                with filter_date_col1:

                    st.write('Event Date')
                    
                    set_start_date1 = st.checkbox(label="set start date", key="start_date_checkbox1")

                    if set_start_date1:
                        event_start_date = st.date_input(label="select start date", key="start_date1")

                    set_end_date1 = st.checkbox(label="set end date", key="end_date_checkbox1")

                    if set_end_date1:
                        event_end_date = st.date_input(label="select end date", key="end_date1")

                with filter_date_col2:

                    st.write('Event Time')

                    set_start_time = st.checkbox(label="set start time", key="start_date_checkbox2")

                    if set_start_time:
                        event_start_time = st.time_input(label="select start time", key="start_date2")

                    set_end_time = st.checkbox(label="set end time", key="end_date_checkbox2")
                    
                    if set_end_time:   
                        event_end_time = st.time_input(label="select end time", key="end_date2")

                venue = st.text_input('Venue: ')
                theme = st.text_input('Theme: ') 
                host = st.text_input('Host')

                ai_generated_text = st.button('Hub-AI', icon='🪄')
                event_message = st.text_area('write your event message here...')

                if ai_generated_text:
                    event_message = get_auto_params(sms_category)
                                    

                send_message = st.button(label='send message ', icon=':material/send:')

                if send_message:

                    final_event_message = f"Venue: {venue} \nTheme: {theme} \nDate: {event_start_date} - {event_start_time} \n{event_message}"

                    send_bulk_message(community_name, df, final_event_message)


            with event_image:
                st.image('./src/images (1).jpg', width=500)

        # ====================== Announcement Section ================================ #

        elif sms_category == 'Announcement':
            notice_body, notice_image = st.columns(2, vertical_alignment="top")

            with notice_body:

                st.write(f"<h3 style='text-align: left; color: #3EA99F;'>🛗 {community_name}<h3>", unsafe_allow_html=True)

                csv_imp, attach_contact = st.columns(2)

                with csv_imp:
                    import_contacts = st.button('upload contacts', icon=':material/upload_file:', use_container_width=True)

                with attach_contact:
                    open_contacts = st.button('import', icon=':material/add_call:', use_container_width=True)

                recipients_number, add_num = st.columns([5, 1])
                
                with recipients_number:
                    # get_number = st.number_input('', value=0, min_value=0, max_value=int(10e10), key="number1")

                    contact_list = []

                    if 'number_count' not in st.session_state:
                        st.session_state.number_count = 1

                    for i in range(st.session_state.number_count):
                        get_number = st.number_input(label='', min_value=0, max_value=int(10e10), key=f'number_{i}')
                        contact_list.append(get_number)

                    df = pd.DataFrame({'phone_numbers':contact_list})
                    st.dataframe(df.head())



                with add_num:
                    
                    st.write('')
                    st.write('')
                    add_num_btn = st.button(label="", icon=':material/add_call:')

                    remove_num_btn = st.button(label="", icon=':material/phone_forwarded:')

                    if add_num_btn:
                        st.session_state.number_count += 1

                    if remove_num_btn and st.session_state.number_count > 1:
                        st.session_state.number_count -= 1

                ai_generated_text = st.button('Hub-AI', icon='🪄')
                announcement_message = st.text_area('write your announcement message here...')

                if ai_generated_text:
                    announcement_message = get_auto_params(sms_category)
                                    

                send_message = st.button(label='send message ', icon=':material/send:')

                if send_message==True:
                    send_bulk_message(community_name, df, notice_message)

            with notice_image:
                st.image('./src/download (3).jpg', width=500)

        # ====================== Meetup Section ================================ #

        elif sms_category == 'Meetup':
            event_feature, event_image = st.columns(2)

            with event_feature:

                csv_imp, attach_contact = st.columns(2)

                with csv_imp:
                    import_contacts = st.button('upload contacts', icon=':material/upload_file:', use_container_width=True)

                with attach_contact:
                    open_contacts = st.button('import', icon=':material/add_call:', use_container_width=True)

                recipients_number, add_num = st.columns([5, 1])
                
                with recipients_number:
                    # get_number = st.number_input('', value=0, min_value=0, max_value=int(10e10), key="number1")

                    contact_list = []

                    if 'number_count' not in st.session_state:
                        st.session_state.number_count = 1

                    for i in range(st.session_state.number_count):
                        get_number = st.number_input(label='', min_value=0, max_value=int(10e10), key=f'number_{i}')
                        contact_list.append(get_number)

                    contact_table = st.dataframe(pd.DataFrame({'phone_numbers': contact_list}))

                with add_num:
                    
                    st.write('')
                    st.write('')
                    add_num_btn = st.button(label="", icon=':material/add_call:')

                    remove_num_btn = st.button(label="", icon=':material/phone_forwarded:')

                    if add_num_btn:
                        st.session_state.number_count += 1

                    if remove_num_btn and st.session_state.number_count > 1:
                        st.session_state.number_count -= 1


                filter_date_col1, filter_date_col2 = st.columns(2)

                with filter_date_col1:

                    st.write('Event Date')
                    
                    set_start_date1 = st.checkbox(label="set start date", key="start_date_checkbox1")

                    if set_start_date1:
                        meetup_start_date = st.date_input(label="select start date", key="start_date1")

                    set_end_date1 = st.checkbox(label="set end date", key="end_date_checkbox1")

                    if set_end_date1:
                        meetup_end_date = st.date_input(label="select end date", key="end_date1")

                with filter_date_col2:

                    st.write('Event Time')

                    set_start_time = st.checkbox(label="set start time", key="start_date_checkbox2")

                    if set_start_time:
                        meetup_start_time = st.time_input(label="select start time", key="start_date2")

                    set_end_time = st.checkbox(label="set end time", key="end_date_checkbox2")
                    
                    if set_end_time:   
                        meetup_end_time = st.time_input(label="select end time", key="end_date2")

                venue = st.text_input('Venue: ')
                theme = st.text_input('Theme: ') 
                host = st.text_input('Host')

                ai_generated_text = st.button('Hub-AI', icon='🪄')
                notice_message = st.text_area('write your event message here...')

                if ai_generated_text:
                    alert_message = get_auto_params(sms_category)
                                    

                send_message = st.button(label='send message ', icon=':material/send:')

                if send_message:

                    final_meetup_message = f"Venue: {venue} \nTheme: {theme} \nDate: {meetup_start_date} - {meetup_start_time} \n{event_message}"

                    send_bulk_message(community_name, df, final_meetup_message)


            with event_image:
                st.image('./src/meetup-logo-vector-download.jpg', width=500)

        # ====================== Announcement Section ================================ #

        elif sms_category == 'Announcement':
            notice_body, notice_image = st.columns(2, vertical_alignment="top")

            with notice_body:

                st.write(f"<h3 style='text-align: left; color: #3EA99F;'>🛗 {community_name}<h3>", unsafe_allow_html=True)

                csv_imp, attach_contact = st.columns(2)

                with csv_imp:
                    import_contacts = st.button('upload contacts', icon=':material/upload_file:', use_container_width=True)

                with attach_contact:
                    open_contacts = st.button('import', icon=':material/add_call:', use_container_width=True)

                recipients_number, add_num = st.columns([5, 1])
                
                with recipients_number:
                    # get_number = st.number_input('', value=0, min_value=0, max_value=int(10e10), key="number1")

                    contact_list = []

                    if 'number_count' not in st.session_state:
                        st.session_state.number_count = 1

                    for i in range(st.session_state.number_count):
                        get_number = st.number_input(label='', min_value=0, max_value=int(10e10), key=f'number_{i}')
                        contact_list.append(get_number)

                    df = pd.DataFrame({'phone_numbers':contact_list})

                    st.dataframe(df.head())



                with add_num:
                    
                    st.write('')
                    st.write('')
                    add_num_btn = st.button(label="", icon=':material/add_call:')

                    remove_num_btn = st.button(label="", icon=':material/phone_forwarded:')

                    if add_num_btn:
                        st.session_state.number_count += 1

                    if remove_num_btn and st.session_state.number_count > 1:
                        st.session_state.number_count -= 1

                ai_generated_text = st.button('Hub-AI', icon='🪄')
                notice_message = st.text_area('write your meetup message here...')

                if ai_generated_text:
                    alert_message = get_auto_params(sms_category)
                                    

                send_message = st.button(label='send message ', icon=':material/send:')

                if send_message==True:
                    send_bulk_message(community_name, df, notice_message)

            with notice_image:
                st.image('./src/download (3).jpg', width=500)



     with email:

        # Taking inputs
        email_sender = st.text_input('From')
        email_receiver = st.text_input('To')
        subject = st.text_input('Subject')
        body = st.text_area('Body')
        password = st.text_input('Password', type="password") 

        if st.button("Send Email"):
            try:
                msg = MIMEText(body)
                msg['From'] = email_sender
                msg['To'] = email_receiver
                msg['Subject'] = subject

                server = smtplib.SMTP('smtp.gmail.com', 587)
                server.starttls()
                server.login(email_sender, password)
                server.sendmail(email_sender, email_receiver, msg.as_string())
                server.quit()

                st.success('Email sent successfully! 🚀')
            except Exception as e:
                st.error(f"Error sending Email : {e}")
        

     with airtime:

        airtime_feature, airtime_image = st.columns(2)

        with airtime_feature:
            
            contact_list = []

            amount_option = [5, 20, 50, 100, 200, 500, 1000]
            airtime_amount = st.pills('set amount', options=amount_option)
            phone_number_for_airtime = st.number_input(label='Recipients Phone number', value=0)

            contact_list.append(phone_number_for_airtime)

            df = pd.DataFrame({'phone_numbers': contact_list})
            st.dataframe(df)

            send_airtime_btn = st.button('Send airtime', icon='📲')

            if send_airtime_btn==True:
                send_bulk_airtime(airtime_amount, df)

        with airtime_image:
            st.image('./src/hero.png', width=1250)


        
     with voice:
        aud = st.title("🎙️ Audio Recorder")

        audio_feature, audio_image = st.columns([3, 2])

        with audio_feature:
            voice_btn = st.button(label="", icon=':material/mic:',use_container_width=True)

            wav_audio_data = st_audiorec()
            if wav_audio_data is not None:
                st.audio(wav_audio_data, format='audio/wav')

        with audio_image:
            st.image('./src/download (2).png', width=350)


     with vid_conf:

        room_name = st.text_input('Enter Room name')

        if room_name:
            st.markdown(f"""
                <iframe src="https://meet.jit.si/{room_name}"
                        width="1100" height="600" allow="camera; microphone; fullscreen"
                        style="border:none;">
                </iframe>
            """, unsafe_allow_html=True)
            

     with promotion:
        
        pass


        
