import streamlit as st

#Initial setting up (to avoid errors)
st.set_page_config(page_title='Streamlit Apps | Swastik "Polybit" Biswas - Junior Coders', page_icon='🎯', layout = 'centered', initial_sidebar_state = 'expanded')

#all my apps
from image_recognition import app as image_recog_app
from get_inspired import app as get_insp_app

PAGES = {
    "Image Recognition (IRM)": image_recog_app,
    "Get Inspired": get_insp_app
}

st.sidebar.title('All my Apps!')
selection = st.sidebar.radio("Go to", list(PAGES.keys()))
page = PAGES[selection]
page.app()
