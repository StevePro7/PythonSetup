# Method name suggestions
class DatabaseConnection:
    def execute_query(self, sql):
        return f"Executing: {sql}"

db = DatabaseConnection()

try:
    db.execute_querry("SELECT * FROM users")  # Intentional typo
except AttributeError as e:
    print(e)

# Output: 'DatabaseConnection' object has no attribute 'execute_querry'. 
# Did you mean 'execute_query'?