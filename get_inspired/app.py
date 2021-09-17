import streamlit as st
import requests
import json

def get_quote():
    response = requests.get('http://zenquotes.io/api/random')
    json_data = json.loads(response.text)
    quote = [json_data[0]['q'], json_data[0]['a']]
    return quote

def app():
    st.session_state.quote = get_quote()
    st.markdown(f"""
        # Get Inspired
        #### Brighten your day with quotes from the greatest minds...
        Made by Swastik 'Polybit' Biswas
        ## 
        ## *" {st.session_state.quote[0]} "*
        *- {st.session_state.quote[1]}*
        ## 
    """)
    action = st.button("I'm still not inspired yet. Hit me with another one!")
    if action:
        st.session_state.quote = get_quote()