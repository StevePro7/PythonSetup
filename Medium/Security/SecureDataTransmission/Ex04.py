# 4. Secure Authentication with OAuth2 and JWT
import jwt
import datetime

secret='your-s56-bit-secret'
token = jwt.encode({
'user_id': 123,
    'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=1)
}, secret, algorithm='HS256')

print(token)