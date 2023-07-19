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
    download_type = st.selectbox('Select type', options=['only video','only audio'])
    if download_type == 'only video':
        video_raw = yt.streams.filter(only_video=True)
        loading_message_vid = st.empty()
        loading_message_vid.info('Loading Video...')
        for i in list(enumerate(video_raw)):
            st.write(i)
        video_download = video_raw.first()
        video_download.download()
        video_path = video_download.default_filename
        with open(video_path, 'rb') as videofile:
            video_bytes = videofile.read()
            
        loading_message_vid.info('Video loaded successfully!')
        os.remove(video_path)
        if st.download_button(label='Download Video', data=video_bytes, mime='video/mp4', file_name=f'{yt.title}.mp4'):
            loading_message_vid.empty()
            st.success('Download Successful')
                
            
    else:
        loading_message = st.empty()
        loading_message.info('Loading audio...')
        audio_raw = yt.streams.filter(only_audio=True)
        audio_download = audio_raw.get_audio_only()
        audio_download.download()
        audio_path = audio_download.default_filename

        with open(audio_path, 'rb') as file:
            audio_bytes = file.read()
            
        loading_message.info('Audio loaded successfully!')
        os.remove(audio_path)
        if st.download_button(label='Download Audio', data=audio_bytes,mime='audio/mpeg', file_name=f'{yt.title}.mp3'):
            loading_message.empty()
            st.success('Download Successful')
                
                
                

