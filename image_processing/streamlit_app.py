import streamlit as st
from PIL import Image
import image_processing as ip
from io import BytesIO
import numpy as np

st.title("Image Processing App")

# Sidebar for selecting the image processing task
st.sidebar.title("Settings")
option = st.sidebar.selectbox(
    'Select an image processing task',
    ('Blur', 'Smooth', 'Rotate', 'Crop', 'Thumbnail', 'Grayscale', 'Resize', 'Perspective Transform')
)

# Main container for image input and output
with st.container():
    uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        st.image(image, caption='Uploaded Image', use_column_width=True)
        st.write("")

        try:
            # Process the image based on the selected option
            if option == 'Blur':
                radius = st.sidebar.slider('Blur radius', 1, 10, 5)
                result_image = ip.blur_image(image, radius)
            elif option == 'Smooth':
                result_image = ip.smooth_image(image)
            elif option == 'Rotate':
                angle = st.sidebar.slider('Rotation angle', 0, 360, 90)
                result_image = ip.rotate_image(image, angle)
            elif option == 'Crop':
                left = st.sidebar.number_input('Left', value=0)
                top = st.sidebar.number_input('Top', value=0)
                right = st.sidebar.number_input('Right', value=image.width)
                bottom = st.sidebar.number_input('Bottom', value=image.height)
                result_image = ip.crop_image(image, left, top, right, bottom)
            elif option == 'Thumbnail':
                width = st.sidebar.number_input('Width', value=128)
                height = st.sidebar.number_input('Height', value=128)
                result_image = ip.create_thumbnail(image.copy(), (width, height))
            elif option == 'Grayscale':
                result_image = ip.convert_to_grayscale(image)
            elif option == 'Resize':
                width = st.sidebar.number_input('Width', value=image.width)
                height = st.sidebar.number_input('Height', value=image.height)
                result_image = ip.resize_image(image, (width, height))
            elif option == 'Perspective Transform':
                st.sidebar.write("Enter coordinates of 4 points for the transformation:")
                points1 = np.float32([
                    [st.sidebar.number_input('Point 1 X', value=0), st.sidebar.number_input('Point 1 Y', value=0)],
                    [st.sidebar.number_input('Point 2 X', value=image.width), st.sidebar.number_input('Point 2 Y', value=0)],
                    [st.sidebar.number_input('Point 3 X', value=0), st.sidebar.number_input('Point 3 Y', value=image.height)],
                    [st.sidebar.number_input('Point 4 X', value=image.width), st.sidebar.number_input('Point 4 Y', value=image.height)]
                ])
                points2 = np.float32([
                    [st.sidebar.number_input('Point 1 X (new)', value=0), st.sidebar.number_input('Point 1 Y (new)', value=0)],
                    [st.sidebar.number_input('Point 2 X (new)', value=image.width), st.sidebar.number_input('Point 2 Y (new)', value=0)],
                    [st.sidebar.number_input('Point 3 X (new)', value=0), st.sidebar.number_input('Point 3 Y (new)', value=image.height)],
                    [st.sidebar.number_input('Point 4 X (new)', value=image.width), st.sidebar.number_input('Point 4 Y (new)', value=image.height)]
                ])
                result_image = ip.perspective_transform(image, points1, points2)

            st.image(result_image, caption='Processed Image', use_column_width=True)

            # Save the processed image to a BytesIO object
            buf = BytesIO()
            result_image.save(buf, format="PNG")
            byte_im = buf.getvalue()

            # Add a download button
            st.download_button(
                label="Download Processed Image",
                data=byte_im,
                file_name="processed_image.png",
                mime="image/png"
            )
        
        except Exception as e:
            st.error(f"An error occurred: {e}")