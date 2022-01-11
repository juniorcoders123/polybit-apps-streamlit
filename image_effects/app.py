import streamlit as st
import cv2
import numpy as np
from PIL import Image, ImageOps, ImageFilter, ImageEnhance
from io import BytesIO
import base64

def app():
    st.markdown('''
    # Image Effects
    Made by **Swastik 'Polybit' Biswas**
    ### 
    ### ''')
    uploaded_file = st.file_uploader("Upload an image...", type=["jpg", "png", "jpeg"])
    if uploaded_file is not None:
        original_image = Image.open(uploaded_file)
        final_image = original_image
        original_image_holder, final_image_holder = st.columns(2)
        original_image_holder.image(original_image, 'Original Image', use_column_width=True)
        fx = st.selectbox('Select an image effect...', ['None', 'Invert', 'Grayscale', 'Blur', 'Sharpen', 'Contrast', 'Brightness', 'Oil Painting Effect', 'Sketch Effect'])
        if fx == 'None':
            pass
        elif fx == 'Invert':
            final_image = ImageOps.invert(original_image)
        elif fx == 'Grayscale':
            final_image = original_image.convert('L')
        elif fx == 'Blur':
            radius = st.slider('Blur Radius', 1, 15, 3)
            final_image = original_image.filter(ImageFilter.BoxBlur(radius))
        elif fx == 'Sharpen':
            quality = st.slider('Sharpen Quality', 1, 5, 2)
            final_image = original_image.filter(ImageFilter.SHARPEN)
            for i in range(quality-1):
                final_image = final_image.filter(ImageFilter.SHARPEN)
        elif fx == 'Contrast':
            enhancer = ImageEnhance.Contrast(original_image)
            factor = st.slider('Contrast Factor', 0.1, 3.0, 1.5)
            final_image = enhancer.enhance(factor)
        elif fx == 'Brightness':
            enhancer = ImageEnhance.Brightness(original_image)
            factor = st.slider('Brightness Factor', 0.1, 3.0, 1.5)
            final_image = enhancer.enhance(factor)
        elif fx == 'Oil Painting Effect':
            detail = st.slider('Oil Painting Detail', 1, 10, 5)
            final_image = cv2.xphoto.oilPainting(np.array(original_image), 11-detail, 1)
        elif fx == 'Sketch Effect':
            detail = st.slider('Sketch Detail', 15, 39, 21)
            gray_image = cv2.cvtColor(np.array(original_image), cv2.COLOR_BGR2GRAY)
            inverted_gi = 255 - gray_image
            blurred_img = cv2.GaussianBlur(inverted_gi, (detail, detail), 0)
            inverted_bi = 255 - blurred_img
            final_image = cv2.divide(gray_image, inverted_bi, scale=256.0)
        else:
            st.error('Please select a valid image effect from the dropdown...')
        final_image_holder.image(final_image, 'Final Image', use_column_width=True)
        if fx == 'Oil Painting Effect' or fx == 'Sketch Effect':
            final_image = Image.fromarray(final_image)
        final_image.save('image_effects/image.jpg')
        st.download_button('Download Final Image', 'image_effects/image.jpg')