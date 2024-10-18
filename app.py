# app.py
import streamlit as st
from video_processor import process_video

def main():
    st.title("Video Enhancer")
    uploaded_file = st.file_uploader("upload video", type=["mp4", "avi", "mov"])
    if uploaded_file is not None:
        st.video(uploaded_file)
        if st.button("Process Video"):
            with st.spinner("Process Video..."):
                enhanced_video = process_video(uploaded_file)
                st.success("processing")
                st.video(enhanced_video)
                st.download_button(
                    label="Download Enhanced Video",
                    data=enhanced_video,
                    file_name="enhanced_video.mp4",
                    mime="video/mp4"
                )

if __name__ == "__main__":
    main()