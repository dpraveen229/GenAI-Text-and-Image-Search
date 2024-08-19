import streamlit as st
import os
import google.generativeai as genai
from PIL import Image
import app

# 1. Configuration
# 2. Get Model

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

model= genai.GenerativeModel("gemini-1.5-flash")
def get_gemini_response(input, image):
    if input!="":
        response=model.generate_content([input,image])
    else:
        response=model.generate_content(image)
    return response.text

# initialize our streamlit app

st.set_page_config(page_title="Gemini image demo")

st.header("Praveen GENAI Application")

input=st.text_input("Input Prompt: ", key="input")
submit_text=st.button("Tell me answer")

if submit_text:
    response= app.get_gemini_response(input)
    st.subheader("The response is ")
    st.write(response)



uploaded_file= st.file_uploader("Choose an image...", type=["jpg","jpeg","png"])
image=""
if uploaded_file is not None:
    image=Image.open(uploaded_file)
    st.image(image, caption="uploaded image.", use_column_width=True)

submit_image=st.button("Tell me about image")

if submit_image:
    response=get_gemini_response(input, image)
    st.subheader("The Response is")
    st.write(response)