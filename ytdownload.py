import os
import streamlit as st
from pytube import YouTube

'''
# Youtube Downloader
'''

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
                # output_path = os.path.join(os.path.expanduser("~"), "Downloads")
                video_download.download()
                st.write('✅ Video downloaded: Successful!')
            except Exception:
                st.write("Wrong input! Carefully choose the itag value 😃")
                # st.write('Download Path:', os.path.join(output_path, video_download.default_filename))
            
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
                # output_path = os.path.join(os.path.expanduser("~"), "Downloads")
                audio_download.download()
                st.write('✅ Audio downloaded: Successful!')
                st.write('Download Path:', audio_download.get_file_path())
            except Exception:
                st.write("Wrong input! Carefully choose the itag value 😃")
