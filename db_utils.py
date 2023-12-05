# Importing necessary libraries
import pandas as pd
import yaml
from sqlalchemy import create_engine

class RDSDatabaseConnector:
    def __init__(self, credentials):
        self.credentials = credentials
        self.engine = self.create_engine()

    # Method to initialize SQLAlchemy engine
    def create_engine(self):
        db_url = f"postgresql+psycopg2://{self.credentials['RDS_USER']}:{self.credentials['RDS_PASSWORD']}@{self.credentials['RDS_HOST']}:{self.credentials['RDS_PORT']}/{self.credentials['RDS_DATABASE']}"
        engine = create_engine(db_url)
        return engine

    # Method to extract data as Pandas DataFrame
    def extract_data(self, table_name='loan_payments'):
        query = f"SELECT * FROM {table_name};"
        data_frame = pd.read_sql(query, self.engine)
        return data_frame

    # Method to save data to a local CSV file
    def save_to_csv(self, data_frame, file_name='loan_payments.csv'):
        data_frame.to_csv(file_name, index=False)
