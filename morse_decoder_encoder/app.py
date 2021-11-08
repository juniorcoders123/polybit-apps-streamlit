import streamlit as st

# write a function that converts english to morse code
def morse_encode(text):
    morse_code = {
        'A': '.-', 'B': '-...',
        'C': '-.-.', 'D': '-..', 'E': '.',
        'F': '..-.', 'G': '--.', 'H': '....',
        'I': '..', 'J': '.---', 'K': '-.-',
        'L': '.-..', 'M': '--', 'N': '-.',
        'O': '---', 'P': '.--.', 'Q': '--.-',
        'R': '.-.', 'S': '...', 'T': '-',
        'U': '..-', 'V': '...-', 'W': '.--',
        'X': '-..-', 'Y': '-.--', 'Z': '--..',
        '1': '.----', '2': '..---', '3': '...--',
        '4': '....-', '5': '.....', '6': '-....',
        '7': '--...', '8': '---..', '9': '----.',
        '0': '-----', ', ': '--..--', '.': '.-.-.-',
        '?': '..--..', '/': '-..-.', '-': '-....-',
        '(': '-.--.', ')': '-.--.-', ' ': '/'
    }
    return ' '.join(morse_code[char] for char in text.upper())

# write a function that converts morse code to english
def morse_decode(text):
    morse_code = {
        '.-': 'A', '-...': 'B',
        '-.-.': 'C', '-..': 'D', '.': 'E',
        '..-.': 'F', '--.': 'G', '....': 'H',
        '..': 'I', '.---': 'J', '-.-': 'K',
        '.-..': 'L', '--': 'M', '-.': 'N',
        '---': 'O', '.--.': 'P', '--.-': 'Q',
        '.-.': 'R', '...': 'S', '-': 'T',
        '..-': 'U', '...-': 'V', '.--': 'W',
        '-..-': 'X', '-.--': 'Y', '--..': 'Z',
        '.----': '1', '..---': '2', '...--': '3',
        '....-': '4', '.....': '5', '-....': '6',
        '--...': '7', '---..': '8', '----.': '9',
        '-----': '0', '--..--': ', ', '.-.-.-': '.',
        '..--..': '?', '-..-.': '/', '-....-': '-',
        '-.--.': '(', '-.--.-': ')', '/': ' '
    }
    return ''.join(morse_code[char] for char in text.split(' '))

def app():
    st.markdown('''
    # Morse Decoder + Encoder
    Made by **Swastik 'Polybit' Biswas**

    Special Thanks to **TechNinja** for the idea!
    ### 
    ### Enter either English or Morse Code to convert to the other.
    ### ''')
    operation = st.selectbox('Select type of operation', ('English to Morse (Encoder)','Morse to English (Decoder)'))
    st.markdown('''
    ## ''')
    if operation == 'English to Morse (Encoder)':
        english = st.text_area('Enter your English text here')
        st.markdown('## ')
        st.markdown('###### Morse Code Encoding')
        output = st.empty()
        try:
            output.code(morse_encode(english))
        except:
            output.error('Please use only alphabet characters (A-Z), numbers (0-9), spaces and special characters (,.?/())...\nAny other unicode characters are either not allowed till now or their morse code translations have not been added yet... ')
        if st.button('Convert to Morse Code'):
            try:
                output.code(morse_encode(english))
            except:
                output.error('Please use only alphabet characters (A-Z), numbers (0-9), spaces and special characters (,.?/())...\nAny other unicode characters are either not allowed till now or their morse code translations have not been added yet... ')
    elif operation == 'Morse to English (Decoder)':
        morse = st.text_area('Enter your Morse Code here')
        st.markdown('## ')
        st.markdown('###### English Decoding')
        output = st.empty()
        if st.button('Convert to English'):
            try:
                output.code(morse_decode(morse))
            except:
                output.code('Please enter valid Morse Code')
        try:
            output.code(morse_decode(morse))
        except:
            output.error('Please enter valid Morse Code')
