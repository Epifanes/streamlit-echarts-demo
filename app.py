import streamlit as st
from PIL import Image

def main():
    st.title('Streamlit plotting of processed data')
    """
    Welcome to Digital Twin Høst 2023 - Data Processing and Visualization

    This app shows acceleration data recorded during a bus drive in Ålesund Sentrum 

    Select from the sidebar menu to review the processed data you want!

    """

    # Images dictionary with names and file paths
    images = {
        'Acceleration data over time': '/workspaces/streamlit-echarts-demo/Images/connectedmesh2.PNG',
        'Fourier analysis z-acceleration': 'path_to_your_image_2.png',
        'Fourier analysis y-acceleration': 'path_to_your_image_2.png',
        'Fourier analysis x-acceleration': 'path_to_your_image_2.png',
        'Spectogram z-acceleration': 'path_to_your_image_3.png',
        'Spectogram y-acceleration': 'path_to_your_image_3.png',
        'Spectogram x-acceleration': 'path_to_your_image_3.png'
    }

    # Sidebar to select the image
    selection = st.sidebar.selectbox('Select a result', list(images.keys()))

    # Load and display the selected image
    image_path = images[selection]
    image = Image.open(image_path)
    st.image(image, caption=selection, use_column_width=True)

if __name__ == "__main__":
    main()