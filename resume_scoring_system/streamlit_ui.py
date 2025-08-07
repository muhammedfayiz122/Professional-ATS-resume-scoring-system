import streamlit as st

def main():
    st.title("Resume Scoring System")
    st.write("This is an agentic system for the Resume Scoring System.")
    
    st.sidebar.title("Navigation")
    page = st.sidebar.selectbox("Select a page", ["Home", "Upload Resume", "View Scores", "Recommendations", "Visualizations"])

    if page == "Home":
        st.subheader("Welcome to the Resume Scoring System")
        st.write("Use the sidebar to navigate through the system.")
    elif page == "Upload Resume":
        st.subheader("Upload Resume")
        st.write("Upload your resume for analysis.")
        file = st.file_uploader("Choose a file", type=["pdf", "docx", "txt"])
        print(file)
    elif page == "View Scores":
        st.subheader("View Scores")
        st.write("View the scores of uploaded resumes.")
    elif page == "Recommendations":
        st.subheader("Recommendations")
        st.write("Get recommendations for improving your resume.")
    elif page == "Visualizations":
        st.subheader("Visualizations")
        st.write("View visual representations of resume data.")
        
if __name__ == "__main__":
    main()