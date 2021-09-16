from PIL import Image
import streamlit as st
from image_recognition.predict import predict, sort
from streamlit.elements.image import image_to_url

def app():
    st.markdown("""
        # Image Recognition Model
        Made by Swastik 'Polybit' Biswas
        ###
        ### Upload an image and the model will try to predict the item in the image*

        *Only for specific items: Airplane, Automobile, Bird, Cat, Deer, Dog, Frog, Horse, Ship, Truck
        # 
    """)
    uploaded_image = st.file_uploader('Upload Image', type=['png','jpeg','jpg'])
    image_display = st.empty()
    output = st.empty()
    if not uploaded_image: output.warning('Please upload an image to proceed!')
    else:
        image = Image.open(uploaded_image)
        image_display.image(image, caption='Uploaded Image')
        output.info('Processing, please wait momentarily...')
        image.save('image_recognition/image.jpg')
        predictions = predict('image_recognition/image.jpg')
        list_index = sort(predictions)
        print(list_index)
        output.markdown(f"""
            # 
            # Predictions!
            ### 1️⃣  {list_index[0]}
            ### 2️⃣  {list_index[1]}
            ### 3️⃣  {list_index[2]}
            ### 4️⃣  {list_index[3]}
            ### 5️⃣  {list_index[4]}
        """)
