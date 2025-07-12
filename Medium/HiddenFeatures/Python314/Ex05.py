from typing import ReadOnly, TypeIs, TypedDict
from dataclasses import dataclass

# ReadOnly for immutable fields in TypedDict
@dataclass
class UserProfile(TypedDict):
    id: ReadOnly[int]          # Cannot be modified after creation
    username: ReadOnly[str]    # Cannot be modified after creation
    email: str                 # Can be modified
    last_login: str           # Can be modified

# TypeIs for more precise type narrowing
def is_positive_int(value: object) -> TypeIs[int]:
    """Type guard that checks if value is a positive integer"""
    return isinstance(value, int) and value > 0

def is_valid_email(value: object) -> TypeIs[str]:
    """Type guard that checks if value is a valid email string"""
    return isinstance(value, str) and "@" in value and "." in value

def process_user_data(data: dict) -> UserProfile | None:
    """Process user data with enhanced type checking"""
    
    # Extract and validate user ID
    user_id = data.get("id")
    if not is_positive_int(user_id):
        return None
    # After this check, type checker knows user_id is int
    
    # Extract and validate email
    email = data.get("email")
    if not is_valid_email(email):
        return None
    # After this check, type checker knows email is str
    
    # Create user profile with ReadOnly fields
    profile: UserProfile = {
        "id": user_id,           # ReadOnly - cannot be changed later
        "username": data.get("username", ""),  # ReadOnly
        "email": email,          # Mutable
        "last_login": data.get("last_login", "never")  # Mutable
    }
    
    return profile

# Example usage
test_data = {
    "id": 123,
    "username": "john_doe",
    "email": "john@example.com",
    "last_login": "2024-10-15"
}

user = process_user_data(test_data)
if user:
    print(f"Created user: {user}")
    # user["id"] = 456  # Type checker will warn: ReadOnly field cannot be assigned