from dotenv import load_dotenv
load_dotenv()

import streamlit as st
import os
import google.generativeai as genai
from PIL import Image
from gtts import gTTS
from streamlit_option_menu import option_menu

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Function to load Gemini Pro model and get responses
model = genai.GenerativeModel("gemini-1.5-flash")
def get_gemini_response(image):
    if image:
        response = model.generate_content(image)
        return response.text
    return ""

# Initialize Streamlit app
st.set_page_config(page_title="Image Caption Generator", page_icon="📸")

# Sidebar Navigation
with st.sidebar:
    selected = option_menu(
        "Navigation", 
        ["Home", "Abstract", "About Me","Feedback"],
        icons=["house", "book", "person", "chat"], 
        menu_icon="cast", 
        default_index=0,
    )
if selected == "Home":
    st.title("Image Caption Generator")

    # Main App Section
    st.header("Upload an Image")
    uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])
    image = None
    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        st.image(image, caption="Uploaded Image.", use_column_width=True)

    submit = st.button("Generate Image Caption")

    # If submit button is clicked and image is uploaded
    if submit and image:
        response = get_gemini_response(image)
        st.subheader("Generated Caption:")
        st.write(response)
        
        # Convert text to speech
        tts = gTTS(response)
        tts.save("caption_audio.mp3")
        
        # Play the audio
        audio_file = open("caption_audio.mp3", "rb")
        audio_bytes = audio_file.read()
        st.audio(audio_bytes, format="audio/mp3")

    elif submit:
        st.warning("Please upload an image first.")

elif selected == "Abstract":
    st.title("Abstract")
    st.write("""
    This application utilizes Google's Gemini 1.5-Flash model to generate captions for uploaded images. 
    Simply upload an image, and the model will provide a descriptive caption. Additionally, the caption 
    can be converted to speech and played back to you. The app demonstrates the power of generative AI in 
    providing meaningful descriptions for visual content, making it easier for users to understand the context 
    of their images.
    """)

elif selected == "About Me":
    st.title("About Me")
    st.write("""
    I am Aravind Kumar Y, pursuing a Master\'s Degree in Computer Science. This project is a demonstration of generating image captions using advanced Deep Learning models. I have Implemented this with using Generative AI of pre-trained Transformers model.
    I am dedicated to creating tools that enhance our interaction with technology and simplify complex tasks. 
    Feel free to reach out if you have any questions, suggestions, or feedback on my work. This is helpful to train for future scope of using Generative AI models like Gemini Api Nano for Android and iOS applications.
    Thank you for visiting!
    """)
elif selected == "Feedback":
    st.title("Feedback")
    
    st.write("""
    If you have any feedback, suggestions, or questions, feel free to email us at:
    [your-email@example.com](mailto:yaravind007@protonmail.com)
    """)