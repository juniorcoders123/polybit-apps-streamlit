import streamlit as st

#all the apps
from image_recognition import app as image_recog_app

st.set_page_config(page_title='Streamlit Apps | Swastik "Polybit" Biswas - Junior Coders', page_icon='🎯', layout = 'centered', initial_sidebar_state = 'expanded')

PAGES = {
    "Image Recognition (IRM)": image_recog_app
}

st.sidebar.title('All my Apps!')
selection = st.sidebar.radio("Go to", list(PAGES.keys()))
page = PAGES[selection]
page.app()
