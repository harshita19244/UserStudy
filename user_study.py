from logging import PlaceHolder
import streamlit as st
import pandas as pd
from PIL import Image
import base64

st.set_page_config(
     page_title="User Study for Neural Machine Transliteration ",
     page_icon="🧊",
     initial_sidebar_state="expanded",
     menu_items={
         'Get Help': 'https://www.extremelycoolapp.com/help',
         'Report a bug': "https://www.extremelycoolapp.com/bug",
         'About': "# This is a header. This is an *extremely* cool app!"
     }
 )

st.markdown('<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">', unsafe_allow_html=True)

st.markdown("""
<nav class="navbar fixed-top navbar-expand-lg navbar-dark" style="background-color: #3498DB;">
  <a class="navbar-brand" href="https://youtube.com/dataprofessor" target="_blank">User Study</a>
  <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
    <span class="navbar-toggler-icon"></span>
  </button>
  <div class="collapse navbar-collapse" id="navbarNav">
    <ul class="navbar-nav">
      <li class="nav-item active">
        <a class="nav-link disabled" href="#">Home <span class="sr-only">(current)</span></a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#" target="_blank">About</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#" target="_blank">Contact</a>
      </li>
    </ul>
  </div>
</nav>
""", unsafe_allow_html=True)

st.markdown('''# **User Study for Neural Machine Transliteration task**
A simple web app to enter user input in desired language and obtain the transliterated output in the target language.''')
# image = Image.open('transliteration.png')
# st.image(image, width=200)

col1,col2 = st.columns(2)
col1.selectbox('Source Language',('English', 'Hindi'))
input = col1.text_area("Enter input text")
col2.selectbox('Target Language',('English', 'Hindi'))
col2.text_area("Output text")
result = col1.button("Submit",)
if result:
    st.write(input)