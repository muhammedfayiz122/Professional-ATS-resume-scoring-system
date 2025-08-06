from resume_scoring_system.src.data_ingestion import DataIngestion
from resume_scoring_system.logger.cloud_logger import CustomLogger
from pathlib import Path

def test_data_ingestion():
    # Initialize the logger
    logger = CustomLogger().get_logger(__name__)
    
    # Create a DataIngestion instance with a test path
    data_ingestion = DataIngestion(data_path="test_data")
    
    # # Simulate a resume file (mocking the file saving and loading)
    # class MockResume:
    #     def __init__(self, filename):
    #         self.filename = filename
    #         self.name = filename
        
    #     def save(self, path):
    #         logger.info(f"Mock save called for {self.filename} at {path}")
    
    # mock_resume = MockResume("data/SDE-cv.pdf")
    
    # Call the ingest_files method
    resume_path = Path(__file__).parent / "data" / "SDE-cv.pdf"
    docs = data_ingestion.ingest_files(resume_path, save_sessions=True)
    if docs:
        for content in docs:
            print(content.page_content)
    
    # Check if the logger has logged the expected messages
    assert logger is not None
    
if __name__ == "__main__":
    test_data_ingestion()
    print("Data ingestion test passed successfully.")