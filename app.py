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
        'Acceleration data over time': '/workspaces/streamlit-echarts-demo/Images/Acc_over_time.png',
        'Fourier analysis overall': '/workspaces/streamlit-echarts-demo/Images/Freq_spectrum.png',
        'Fourier analysis z-acceleration': '/workspaces/streamlit-echarts-demo/Images/Fourier_z.png',
        'Fourier analysis y-acceleration': '/workspaces/streamlit-echarts-demo/Images/Fourier_y.png',
        'Fourier analysis x-acceleration': '/workspaces/streamlit-echarts-demo/Images/Fourier_x.png',
        'Spectogram z-acceleration': '/workspaces/streamlit-echarts-demo/Images/Spectogram_z.png',
        'Spectogram y-acceleration': '/workspaces/streamlit-echarts-demo/Images/Spectogram_y.png',
        'Spectogram x-acceleration': '/workspaces/streamlit-echarts-demo/Images/Spectogram_x.png'
    }

    # Sidebar to select the image
    selection = st.sidebar.selectbox('Select a result', list(images.keys()))

    # Load and display the selected image
    image_path = images[selection]
    image = Image.open(image_path)
    st.image(image, caption=selection, use_column_width=True)

if __name__ == "__main__":
    main()