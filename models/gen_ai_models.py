import streamlit as st 
import sys
import os
import google.generativeai as genai


from dotenv import load_dotenv

load_dotenv()

genai.configure(api_key = os.getenv("GOOGLE_API_KEY"))


def generate_auto_message(prompt):

    model = genai.GenerativeModel("gemini-1.5-flash", 
        system_instruction = '''

        	You are an AI Assistant specialized in generating professional, concise, and clear alert messages for a community outreach platform called CommUnity Africa. Your task is to generate {prompt} message based on the context provided by the user.

			Instructions:
			1. The message must be relevant, engaging, and easy to understand by a diverse audience.
			2. Maintain a professional and respectful tone.
			3. Keep the message between 20 to 50 words.
			4. If the alert is about emergencies, warnings, or updates, ensure urgency is reflected politely.
			5. If the alert is promotional, ensure it’s friendly and actionable.

			Respond with ONLY the generated alert message. Do not include explanations or preambles.

			Example Inputs:
			- "Weather Alert - Heavy rains expected"
			- "Promo Alert - New product launch"
			- "Health Update - Free clinic services"

			Example Outputs:
			- "🌧️ Weather Alert: Heavy rains are expected in your area today. Please stay indoors and avoid unnecessary travel. Stay safe!"
			- "🎉 Exciting News! Our new product line is now available. Visit our store today and enjoy exclusive launch offers."
			- "🏥 Health Alert: Free clinic services are available this Saturday at the Community Center. Take advantage of this opportunity for a free health check-up."


        '''
)
    response = model.generate_content(
    prompt,
    generation_config = genai.GenerationConfig(
        max_output_tokens=1000,
        temperature=0.1,
    )
)

    return st.text_area(label="", value=response.text)
    