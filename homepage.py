import streamlit as st
from bokeh.models.widgets import Div

#Initial setting up (to avoid errors)
st.set_page_config(page_title='Streamlit Apps | Swastik "Polybit" Biswas - Junior Coders', page_icon='🎯', layout = 'centered', initial_sidebar_state = 'expanded')
st.session_state.can_quote = True

#all my apps
from image_recognition import app as image_recog_app
from get_inspired import app as get_insp_app
from tic_tac_toe import app as tic_tac_toe_app

PAGES = {
    "Image Recognition (IRM)": image_recog_app,
    "Get Inspired": get_insp_app,
    "Tic Tac Toe Game (broken)": tic_tac_toe_app
}

query_params = st.experimental_get_query_params()
default = int(query_params["activity"][0]) if "activity" in query_params else 0

st.sidebar.title('All my Apps!')
selection = st.sidebar.radio("Go to", list(PAGES.keys()), index=default)
if selection:
    st.experimental_set_query_params(activity=list(PAGES).index(selection))
page = PAGES[selection]
page.app()

visit_techninja_site = st.button("Visit TechNinja's Site")
if visit_techninja_site:
    js = "window.open('https://share.streamlit.io/juniorcoders123/techninjaallwebapps/main/homepage.py?activity=0')"  # New tab or window
    html = '<img src onerror="{}">'.format(js)
    div = Div(text=html)
    st.bokeh_chart(div)
github_site = st.button("Visit GitHub repository")
if github_site:
    js = "window.open('https://github.com/juniorcoders123/polybit-apps-streamlit')"  # New tab or window
    html = '<img src onerror="{}">'.format(js)
    div = Div(text=html)
    st.bokeh_chart(div)
