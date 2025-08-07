import streamlit as st
from pathlib import Path
from uuid import uuid4
import os

def main():
    st.title("Resume Scoring System")
    st.write("This is an agentic system for the Resume Scoring System.")
    
    st.sidebar.title("Navigation")
    page = st.sidebar.selectbox("Select a page", ["Home", "Upload Resume", "View Scores", "Recommendations", "Visualizations"])

    uploaded_resume = None
    if page == "Home":
        st.subheader("Welcome to the Resume Scoring System")
        st.write("Use the sidebar to navigate through the system.")
    elif page == "Upload Resume":
        st.subheader("Upload Resume")
        st.write("Upload your resume for analysis.")
        uploaded_resume = st.file_uploader("Choose a file", type=["pdf", "docx", "txt"])
    elif page == "View Scores":
        st.subheader("View Scores")
        st.write("View the scores of uploaded resumes.")
    elif page == "Recommendations":
        st.subheader("Recommendations")
        st.write("Get recommendations for improving your resume.")
    elif page == "Visualizations":
        st.subheader("Visualizations")
        st.write("View visual representations of resume data.")
    
    # if 'session_id' not in st.session_state:
    #     session_id = 
    #     st.session_state.session_id = 
    if 'message' not in st.session_state:
        st.session_state.messages = []
    if 'autogen_team_state' not in st.session_state:
        st.session_state.autogen_team_state = None
    
    print(st.session_state)
        
    if uploaded_resume :
        pass
        
        
        
if __name__ == "__main__":
    main()