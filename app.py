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

dic = {
    'David Perna': "Especialista de crédito e de cachaça",
    'Frederico Nunes': "Minerador de dados e mineiro",
    'Tharick Souza': "Engenheiro de dados e paulista mestiço",
    'Bruno Vitti': "Cientista de dados e cervejeiro"
}

df = pd.DataFrame(dic)

# Set the app title
st.title("Time de Data Science")
st.write(
    "Criação de webapps corporativas com python"
)
# Declare a form to receive a movie's review
form = st.form(key="my_form")
review = form.text_input(label="Insira o teu nome para conhhecer o time de Data Science da Laqus")
submit = form.form_submit_button(label="Enter")

if submit:
    # make prediction from the input text
    result = test_app(review)
 
    # Display results of the NLP task
    st.header("Results")
    st.write(df)