class SQLConnector:
    def __init__(self, connection_string):
        self.connection_string = connection_string
        self.connection = None

    def connect(self):
        import sqlalchemy
        self.connection = sqlalchemy.create_engine(self.connection_string)

    def execute_query(self, query):
        with self.connection.connect() as conn:
            result = conn.execute(query)
            return result.fetchall()

    def close(self):
        if self.connection:
            self.connection.dispose()