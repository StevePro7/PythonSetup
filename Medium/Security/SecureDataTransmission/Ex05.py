# 5. Implement Rate Limiting
from flask import Flask
from flask_limiter import Limiter

app = Flask(__name__)
limiter = Limiter(app, key_func=lambda: requests.remote_addr)

@app.route("/api/resource")
@limiter.limit("10 per minute")
def secure_resource():
    return "Secure data"