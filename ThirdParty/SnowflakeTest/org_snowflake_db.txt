import snowflake.connector

class SnowflakeDB:
    def __init__(self, user, password, account, warehouse, database, schema):
        self.connection = snowflake.connector.connect(
            user=user,
            password=password,
            account=account,
            warehouse=warehouse,
            database=database,
            schema=schema
        )
        self.cursor = self.connection.cursor()

    def execute_query(self, query, params=None):
        try:
            if params:
                self.cursor.execute(query, params)
            else:
                self.cursor.execute(query)
            data = self.cursor.fetchall()
            return data
            #return self.cursor.fetchall()
        except Exception as e:
            print(f"Query execution failed: {e}")
            raise
        finally:
            self.cursor.close()

    def close(self):
        self.connection.close()
