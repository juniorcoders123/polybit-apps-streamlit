import streamlit as st
import requests
import json

def get_quote():
    response = requests.get('http://zenquotes.io/api/random')
    json_data = json.loads(response.text)
    st.session_state.get_inspired_quote = [json_data[0]['q'], json_data[0]['a']]
    st.stop()

def app():
    st.session_state.get_inspired_quote = ['Loading, please wait momentarily.','The website itself, who else did you expect?']
    st.markdown(f"""
        # Get Inspired
        #### Brighten your day with quotes from the greatest minds...
        Made by Swastik 'Polybit' Biswas
        ## 
        ## *" {st.session_state.get_inspired_quote[0]} "*
        *- {st.session_state.get_inspired_quote[1]}*
        ## 
    """)
    action = st.button("I'm still not inspired yet. Hit me with another one!")
    if action:
        get_quote()
    get_quote()
