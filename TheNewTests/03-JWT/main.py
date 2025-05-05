import jwt

from datetime import datetime, timedelta

# Secret for signing
SECRET_KEY = "verysecret"

# Example user
user = {
    "id": 2,
    "username": "stevepro",
    "roles": ["admin"],
    "permissions": ["read", "write", "delete"]
}

# Create a JWT token
def generate_token(user):
    payload = {
        "sub": user["id"],
        "username": user["username"],
        "roles": user["roles"],
        "permissions": user["permissions"],
        "exp": datetime.utcnow() + timedelta(minutes=30)
    }
    token = jwt.encode(payload, SECRET_KEY, algorithm="HS256")
    #token = jwt.encode(payload, algorithm="HS256")
    return token
    #return token if isinstance(token, str) else token.decode('utf-8')

def print_hi(name):
    token = generate_token(user)
    print("JWT Token:", token)


if __name__ == '__main__':
    print_hi('PyCharm!!')
