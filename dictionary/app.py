import streamlit as st
import json
import requests

def app():
    st.markdown("""
        # English Search Dictionary
        Made with ♥ by **Swastik 'Polybit' Biswas**
        ###
    """)
    query = st.text_input('Enter a word to search:')
    if query:
        query = query.lower().strip().replace(' ', '-')
        response = requests.get(f'https://api.dictionaryapi.dev/api/v2/entries/en/{query}')
        if response.status_code == 200:
            data = json.loads(response.text)
            st.markdown(f"""
            # 
            # {data[0]['word']}
            ###### Pronounciation: ({data[0]['phonetics'][0]['text']})
            """)
            st.audio("https:" + data[0]['phonetics'][0]['audio'])
            for i in data[0]['meanings']:
                st.markdown(f"""
                #### 
                #### ({i['partOfSpeech']}) {i['definitions'][0]['definition']}
                Example: {i['definitions'][0]['example']}
                """)
        elif response.status_code == 404:
            st.error('Word not found! Make sure you have entered a valid or a correctly spelled word.')
        else:
            print(response.status_code)