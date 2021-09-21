import subprocess
from sys import stderr, stdout
import streamlit as st
from streamlit_ace import st_ace, KEYBINDINGS, LANGUAGES, THEMES

def app():
    st.markdown("""
        # Python Web IDE
        Made by Swastik 'Polybit' Biswas
        ### A reliable runtime for Python 3
        ## 
    """)

    # code editor
    with st.container():
        st.markdown("""
            ## Code Editor
            ###### Powered by Ace
            ### 
        """)
        content = st_ace(
            placeholder='Write your Python code here',
            language='python',
            theme='twilight',
            keybinding='vscode',
            font_size=15,
            tab_size=4,
            show_gutter=True,
            show_print_margin=False,
            wrap=True,
            auto_update=False,
            readonly=False,
            key='ace'
        )

        # output terminal
        run_button = st.button('Run Python File')
        st.markdown("""
            ### 
            ## Output Terminal
            ###### Note that the terminal cannot accept inputs yet
            ### 
        """)
        output_area = st.empty()
        output_area.code('ㅤ\nㅤ\nㅤ\nㅤ\nㅤ')
        info_placeholder = st.empty()
        if run_button:
            with open("python_ide/run_folder/script.py", "w") as f:
                f.write(content + '\nquit()')
            result = subprocess.run(['python','python_ide/run_folder/script.py'], shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
            output_area.code(result.stdout.decode('utf-8'))
            print(result.stdout.decode('utf-8'))
            info_placeholder.info('Program executed and terminated.')