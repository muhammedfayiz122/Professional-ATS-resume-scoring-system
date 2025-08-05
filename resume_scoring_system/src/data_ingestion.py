from datetime import datetime, timezone
from resume_scoring_system. import logger
from uuid import uuid4

class DataIngestion:
    def __init__(self, data_path):
        self.data_path = data_path

    def ingest_files(self, resume_files, save_sessions=True):
        try:
            for resume in resume_files:
                if save_sessions:
                    unique_name = f"resume_{datetime.now(timezone.utc).strftime('%Y%m%d_%H%M%S')}_{uuid4().hex[:8]}.pdf"
                    resume.save(f"{self.data_path}/{unique_name}")
                else:
                    resume.save(f"{self.data_path}/{resume.name}")
                    
                self.logger                
                
                
        except Exception as e:
            print(f"An error occurred during file ingestion: {e}")
            return None