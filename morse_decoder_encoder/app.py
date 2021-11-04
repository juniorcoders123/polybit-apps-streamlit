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
    ## 
    ## ''')
    operation = st.selectbox('Select type of operation', ('English to Morse','Morse to English'))
    st.markdown('''
    ## ''')
    if operation == 'English to Morse':
        st.write('Enter your English text here')
        english = st.text_area('')
        st.markdown('## ')
        st.write('Morse Code Encoding')
        st.markdown('## ')
        st.code(morse_encode(english))
    elif operation == 'Morse to English':
        st.write('Enter your Morse Code here')
        morse = st.text_area('')
        st.markdown('## ')
        st.write('English Decoding')
        st.markdown('## ')
        try:
            st.code(morse_decode(morse))
        except:
            st.error('Please enter valid Morse Code')
