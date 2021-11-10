import streamlit as st
from PIL import Image, ImageOps, ImageFilter, ImageEnhance

def app():
    st.markdown('''
    # Image Effects
    Made by **Swastik 'Polybit' Biswas**
    ### 
    ### ''')
    uploaded_file = st.file_uploader("Upload an image...", type=["jpg", "png", "jpeg"])
    if uploaded_file is not None:
        original_image = Image.open(uploaded_file)
        original_image.save('image_effects/images/original.png')
        final_image = original_image
        final_image.save('image_effects/images/final.png')
        original_image_holder, final_image_holder = st.columns(2)
        original_image_holder.image('image_effects/images/original.png', 'Original Image', use_column_width=True)
        fx = st.selectbox('Select an image effect...', ['None', 'Invert', 'Grayscale', 'Blur', 'Sharpen', 'Contrast', 'Brightness'])
        if fx == 'None':
            pass
        elif fx == 'Invert':
            final_image = ImageOps.invert(original_image)
            final_image.save('image_effects/images/final.png')
        elif fx == 'Grayscale':
            final_image = original_image.convert('L')
            final_image.save('image_effects/images/final.png')
        elif fx == 'Blur':
            radius = st.slider('Blur Radius', 1, 15, 3)
            final_image = original_image.filter(ImageFilter.BoxBlur(radius))
            final_image.save('image_effects/images/final.png')
        elif fx == 'Sharpen':
            quality = st.slider('Sharpen Quality', 1, 5, 2)
            final_image = original_image.filter(ImageFilter.SHARPEN)
            for i in range(quality-1):
                final_image = final_image.filter(ImageFilter.SHARPEN)
            final_image.save('image_effects/images/final.png')
        elif fx == 'Contrast':
            enhancer = ImageEnhance.Contrast(original_image)
            factor = st.slider('Contrast Factor', 0.1, 3.0, 1.5)
            final_image = enhancer.enhance(factor)
            final_image.save('image_effects/images/final.png')
        elif fx == 'Brightness':
            enhancer = ImageEnhance.Brightness(original_image)
            factor = st.slider('Brightness Factor', 0.1, 3.0, 1.5)
            final_image = enhancer.enhance(factor)
            final_image.save('image_effects/images/final.png')
        else:
            st.error('Please select a valid image effect from the dropdown...')
        final_image_holder.image('image_effects/images/final.png', 'Final Image',use_column_width=True)
        st.download_button('Download Final Image...', open('image_effects/images/final.png', 'rb').read(), file_name='final.png')
