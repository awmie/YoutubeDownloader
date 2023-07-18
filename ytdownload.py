import os
import streamlit as st
from pytube import YouTube
import platform

'''
# Youtube Downloader
'''

# Set the default download path based on the operating system
system = platform.system()

if system == "Windows":
    default_download_path = os.path.join(os.path.expandvars("%userprofile%"), "Downloads")
else:  # Linux and other Unix-like systems
    default_download_path = os.path.join(os.path.expanduser("~"), "Downloads")


if link := st.text_input('Enter the video link here'):
    yt = YouTube(link)
    st.write("Title: ", yt.title)
    st.image(yt.thumbnail_url, use_column_width=True)
    download_type = st.selectbox('Select type', options=['only video', 'only audio'])

    if download_type == 'only video':
        video_raw = yt.streams.filter(only_video=True)
        video_list = list(enumerate(video_raw))
        for y in video_list:
            st.write(y[1])
        if selected_video := st.text_input(
                'Enter the itag value you want to download from the above list'
        ):
            video_download = video_raw.get_by_itag(selected_video)
            try:

                video_download.download(output_path=default_download_path)
                st.write('✅ Video downloaded: Successful!')
            except Exception:
                st.write("Wrong input! Carefully choose the itag value 😃")
                st.write('Download Path:', os.path.join(default_download_path, video_download.default_filename))
            
    else:
        audio_raw = yt.streams.filter(only_audio=True)
        audio_list = list(enumerate(audio_raw))
        for x in audio_list:
            st.write(x[1])
        if selected := st.text_input(
                'Enter the itag value you want to download from the above list'
        ):
            audio_download = audio_raw.get_by_itag(selected)
            try:
                audio_download.download(output_path=default_download_path)
                st.write('✅ Audio downloaded: Successful!')
                st.write('Download Path:', audio_download.get_file_path())
            except Exception:
                st.write("Wrong input! Carefully choose the itag value 😃")
                st.write('Download Path:', os.path.join(default_download_path, audio_download.default_filename))
