import streamlit as st

#Initial setting up (to avoid errors)
st.set_page_config(page_title='Streamlit Apps | Swastik "Polybit" Biswas - Junior Coders', page_icon='🎯', layout = 'centered', initial_sidebar_state = 'expanded')

#all my apps
from image_recognition import app as image_recog_app
from tic_tac_toe import app as tic_tac_toe_app
from morse_decoder_encoder import app as morse_app
from image_effects import app as image_fx_app

# latest --> oldest
PAGES = {
    "Image Effects 🆕": image_fx_app,
    "Morse Code Decoder + Encoder": morse_app,
    "Tic Tac Toe Game [broken 🛠]": tic_tac_toe_app,
    "Image Recognition (IRM)": image_recog_app
}

query_params = st.experimental_get_query_params()
default = int(query_params["activity"][0]) if "activity" in query_params else 0

st.sidebar.title('All my Apps!')
selection = st.sidebar.radio("Go to", list(PAGES.keys()), index=default)
if selection:
    st.experimental_set_query_params(activity=list(PAGES).index(selection))
page = PAGES[selection]
page.app()

visit_techninja_site = "[Visit TechNinja's Site](https://share.streamlit.io/juniorcoders123/techninjaallwebapps/main/homepage.py)"
github_repo = '[Visit the GitHub repository](https://github.com/juniorcoders123/polybit-apps-streamlit)'
st.sidebar.markdown(visit_techninja_site, unsafe_allow_html=True)
st.sidebar.markdown(github_repo, unsafe_allow_html=True)
