# Importing necessary libraries to get everything set up
from dotenv import load_dotenv  
import streamlit as st  
import os  
import google.generativeai as genai  

# Load the environment variables, which includes our Google API key
load_dotenv()  

# Configure the Generative AI API by using the API key we stored in the .env file
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Initialize the Gemini model so it’s ready to answer questions
model = genai.GenerativeModel("gemini-pro")

# Define a function to get a response from the Gemini model
def get_gemini_response(question):
  response = model.generate_content(question)
  return response.text

# Set up the basic configuration for our Streamlit app
st.set_page_config(page_title="LLM Query Engine")  

# Add a header to the app so users know what it does
st.header("Query Engine - Q&A")

# Create an input field where users can type their questions
input = st.text_input("Input: ", key="input")

# Add a button which users will click this to get their answer
submit = st.button("Give me the Answer")

# Check if the button was clicked
if submit:
  response = get_gemini_response(input)
  st.subheader("The response is:")
  st.write(response)
