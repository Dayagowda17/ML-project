import numpy as numpy
import streamlit as st
import pytesseract
from PIL import Image #Python Imagining Library
st.title('OCR - OPTICAL CHARACTER RECOGNITION')
st.text('Upload the image')
uploaded_file = st.sidebar.file_uploader('Choose an image',type =['jpg','png','jpeg'])
if uploaded_file is not None:
  img = Image.open(uploaded_file)
  st.image(img,caption = 'Uploaded Image',use_column_width = True)
  st.write('')

  if st.button('PREDICT'):
    st.write('Result....')
    op = pytesseract.image_to_string(img)
    st.title(op)
