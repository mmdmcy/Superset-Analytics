import os
import json
from sqlalchemy import create_engine
from data_layer.models.data_models import ExampleDataModel

def load_example_data(db_uri):
    engine = create_engine(db_uri)
    with engine.connect() as connection:
        # Example data to be loaded
        example_data = [
            ExampleDataModel(field1='Example 1', field2='Value 1'),
            ExampleDataModel(field1='Example 2', field2='Value 2'),
            ExampleDataModel(field1='Example 3', field2='Value 3'),
        ]
        
        # Load data into the database
        for data in example_data:
            connection.execute(
                ExampleDataModel.__table__.insert().values(
                    field1=data.field1,
                    field2=data.field2
                )
            )
    print("Example data loaded successfully.")

if __name__ == "__main__":
    DATABASE_URI = os.getenv('DATABASE_URI', 'sqlite:///example.db')
    load_example_data(DATABASE_URI)