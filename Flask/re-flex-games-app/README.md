Using Flask-Marshmallow for easy JSON Serialization
30-Nov-2024

https://dev.to/brythewiseguy/flask-easy-mode-using-flask-marshmallow-for-serialization-3bbo

GitHub
https://github.com/BryTheWiseGuy/re-flex-games-app/tree/main/server


python -m venv .venv
source .venv/bin/activate

pip install -r requirements.txt

flask-marshmallow==0.15.0
marshmallow==3.20.1; python_version >= '3.8'
marshmallow-sqlalchemy==0.29.0


app.py
from flask_marshmallow import Marshmallow
ma = Marshmallow(app)

class User_Schema(ma.SQLAlchemySchema):
    pass


alembic init migrations

NB: could not get the migrations or seed database working
but did not matter so much for this example as we focused
on Marshmallow serialization / de-serialization facility.


Endpoints
GET /api/games
GET /api/platforms
GET /api/games/1
GET /api/games/1/platforms
GET /api/games/2/platforms


curl http://127.0.0.1:5555/api/games
curl http://127.0.0.1:5555/api/platforms

curl http://127.0.0.1:5555/api/games/2/platforms
curl http://127.0.0.1:5555/api/platforms/2/games

401
curl http://127.0.0.1:5555/api/users
curl http://127.0.0.1:5555/api/users?username=steve


