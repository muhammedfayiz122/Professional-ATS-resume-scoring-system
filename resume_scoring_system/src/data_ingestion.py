from datetime import datetime, timezone
import sys
import os
from resume_scoring_system.logger.cloud_logger import CustomLogger
from resume_scoring_system.exception.custom_exception import DocumentPortalException
from uuid import uuid4
from langchain_community.document_loaders import PyPDFLoader
from pathlib import Path
from resume_scoring_system.models.gemini_model import load_gemini_model

class DataIngestion:
    def __init__(self, data_path: str = "data/resumes"):
        self.data_path = Path(data_path)
        self.logger = CustomLogger().get_logger(__name__)
        self.model = load_gemini_model()
    def ingest_files(self, resume, save_sessions=True):
        try:
            unique_file_path = None
            with open(resume, "rb") as file:
                resume_contents = file.read()
            if save_sessions:
                unique_file = f"resume_{datetime.now(timezone.utc).strftime('%Y%m%d_%H%M%S')}_{uuid4().hex[:8]}.pdf"
                unique_file_path = self.data_path / unique_file
                os.makedirs(self.data_path, exist_ok=True)
                with open(unique_file_path, "wb") as new_file:
                    new_file.write(resume_contents)
                self.logger.info(f"Resume saved for ingestion: {unique_file_path}")
            else:
                resume.save(f"{self.data_path}/{resume.name}")   
            
            loader = PyPDFLoader(unique_file_path if save_sessions else resume) # type: ignore
            docs = loader.load()
            self.logger.info(f"Loaded {len(docs)} documents from {resume.name}")
            return docs
            
        except Exception as e:
            self.logger.error(f"Error during file ingestion: {e}")
            raise DocumentPortalException(f"Failed to ingest files: {e}", sys) from e
    
    def extract_details(self, resume_contents):
        try:
            parser =
        except Exception as e:
            self.logger.error(f"Error extracting details from resume: {e}")
            raise DocumentPortalException(f"Failed to extract details: {e}", sys) from e