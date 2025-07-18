# snowflake_db.py
import snowflake.connector


class SnowflakeDB:
    def __init__(self, user, password, account, warehouse, database, schema):
        self.user = user
        self.password = password
        self.account = account
        self.warehouse = warehouse
        self.database = database
        self.schema = schema
        self.connection = None
        self.cursor = None

    def open_connection(self):
        self.connection = snowflake.connector.connect(
            user=self.user,
            password=self.password,
            account=self.account,
            warehouse=self.warehouse,
            database=self.database,
            schema=self.schema
        )
        self.cursor = self.connection.cursor()

    def execute_query(self, query, params=None):
        if not self.cursor:
            raise RuntimeError("Connection not open. Call open_connection() first.")

        self.cursor.execute(query, params) if params else self.cursor.execute(query)
        return self.cursor.fetchall()

    def close_connection(self):
        if self.cursor:
            self.cursor.close()
        if self.connection:
            self.connection.close()
