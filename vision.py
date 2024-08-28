import streamlit as st
import os
import google.generativeai as genai
from PIL import Image
from style import set_background_color, colored_text


# 1. Configuration
# 2. Get Model

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))



model= genai.GenerativeModel("gemini-1.5-flash")
def get_gemini_response_image(image):
    if input!="":
        response=model.generate_content([image])
    else:
        response=model.generate_content(image)
    return response.text

def get_gemini_response_text(question):
    response=model.generate_content(question)
    return response.text
# initialize our streamlit app

st.set_page_config(page_title="Gemini image demo")

st.header("Praveen GENAI Application")

input=st.text_input("Input Prompt: ", key="input")
submit_text=st.button("Tell me answer")


if submit_text:
    response_text= get_gemini_response_text(input)
    st.subheader("The text question response is ")
    st.write(response_text)



uploaded_file= st.file_uploader("Choose an image...", type=["jpg","jpeg","png"])
image=""
if uploaded_file is not None:
    image=Image.open(uploaded_file)
    st.image(image, caption="uploaded image.", use_column_width=True)

submit_image=st.button("Tell me about image")

if submit_image:
    response_image=get_gemini_response_image(image)
    st.subheader("The Image Response is")
    st.write(response_image)

# Define the CSS style for background color
set_background_color('lightblue')