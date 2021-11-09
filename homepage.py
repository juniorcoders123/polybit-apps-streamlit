import streamlit as st
import extra_streamlit_components as stx

#Initial setting up (to avoid errors)
st.set_page_config(page_title='Streamlit Apps | Swastik "Polybit" Biswas - Junior Coders', page_icon='🎯', layout = 'centered', initial_sidebar_state = 'expanded')
st.session_state.can_quote = True

#all my apps
from image_recognition import app as image_recog_app
from get_inspired import app as get_insp_app
from tic_tac_toe import app as tic_tac_toe_app
from morse_decoder_encoder import app as morse_app

#all the cookies for apps
cookie_manager = stx.CookieManager()

# latest --> oldest
cookies_ref = ('morse_app_like', 'tic_tac_toe_app_like', 'get_insp_app_like', 'image_recog_app_like')
PAGES = {
    ("⭐ " if cookie_manager.get('morse_app_like') else "") + "Morse Code Decoder + Encoder 🆕": morse_app,
    ("⭐ " if cookie_manager.get('tic_tac_toe_app_like') else "") + "Tic Tac Toe Game [broken 🛠]": tic_tac_toe_app,
    ("⭐ " if cookie_manager.get('get_insp_app_like') else "") + "Get Inspired": get_insp_app,
    ("⭐ " if cookie_manager.get('image_recog_app_like') else "") + "Image Recognition (IRM)": image_recog_app
}

query_params = st.experimental_get_query_params()
default = int(query_params["activity"][0]) if "activity" in query_params else 0

st.sidebar.title('All my Apps!')
selection = st.sidebar.radio("Go to", list(PAGES.keys()), index=default)
if selection:
    st.experimental_set_query_params(activity=list(PAGES).index(selection))
page = PAGES[selection]
page.app()

like_button_text = ''
if cookie_manager.get(cookies_ref[list(PAGES).index(selection)]):
    like_button_text = 'Dislike this current project 💔'
else:
    like_button_text = 'Like this current project! ⭐'
like_button = st.sidebar.button(like_button_text)
if like_button:
    if cookie_manager.get(cookies_ref[list(PAGES).index(selection)]):
        cookie_manager.delete(cookies_ref[list(PAGES).index(selection)])
    else:
        cookie_manager.set(cookies_ref[list(PAGES).index(selection)], True)

visit_techninja_site = "[Visit TechNinja's Site](https://share.streamlit.io/juniorcoders123/techninjaallwebapps/main/homepage.py)"
github_repo = '[Visit the GitHub repository](https://github.com/juniorcoders123/polybit-apps-streamlit)'
st.sidebar.markdown(visit_techninja_site, unsafe_allow_html=True)
st.sidebar.markdown(github_repo, unsafe_allow_html=True)
