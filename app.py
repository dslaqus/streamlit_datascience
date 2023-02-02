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

n1 = 'David Perna'
d1 = "Especialista de crédito e de cachaça"

n2 = 'Frederico Nunes'
d2 = "Minerador de dados e mineiro"

n3 = 'Tharick Souza'
d3 = "Engenheiro de dados e paulista mestiço"

n4 = 'Bruno Vitti'
d4 = "Cientista de dados e cervejeiro"



# Set the app title
st.title("Time de Data Science")
st.write(
    "Criação de webapps corporativas com python"
)
# Declare a form to receive a movie's review
form = st.form(key="my_form")
# review = form.text_input(label="Insira o teu nome para conhhecer o time de Data Science da Laqus")
submit = form.form_submit_button(label="Enter")

if submit:
    # make prediction from the input text
    # result = test_app(review)
 
    # Display results of the NLP task
    st.header("Results")
    st.write(n1,":  ", d1)
    st.write(n2,":  ", d2)
    st.write(n3,":  ", d3)
    st.write(n4,":  ", d4)