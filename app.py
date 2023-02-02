# import packages
import streamlit as st
import os
import numpy as np
import pandas as pd
# text preprocessing modules
from string import punctuation

# text preprocessing modules
import re  # regular expression
import warnings
warnings.filterwarnings("ignore")
# seeding
np.random.seed(123)
 
# load stop words




# function to clean the text
@st.cache
def test_app(text):
    return text

df = pd.DataFrame({'Teste':'A'}, index=[0])

# Set the app title
st.title("Python - Streamlit")
st.write(
    "A simple web app with streamlit"
)
# Declare a form to receive a movie's review
form = st.form(key="my_form")
review = form.text_input(label="Enter any text message")
submit = form.form_submit_button(label="Enter")

if submit:
    # make prediction from the input text
    result = test_app(review)
 
    # Display results of the NLP task
    st.header("Results")
    st.write(df)