import streamlit as st
from dotenv import load_dotenv
from embedding import process_file

load_dotenv()

def uploading_screen():
    st.write("Upload Content!")
    uploaded_file = st.file_uploader(
        "Upload your document (PDF, DOCX, or image)", 
        type=["pdf", "docx"]
    )

    if uploaded_file and "file_chunks" not in st.session_state:
        st.session_state.file_chunks = process_file(uploaded_file)
        st.success("File processed and ready!")


if __name__ == "__main__":
    uploading_screen()