Chat GPT
15-Dec-2024

Share


You said:
linux ubuntu postgresql docker container running alembic migration python flask application

python -m venv .venv
source .venv/bin/activate

Docker
sudo apt-get update
sudo apt-get install -y docker.io

Docker compose
sudo apt-get install -y docker-compose


pip install -r requirements.txt
pip install --upgrade pip


Alembic
alembic init migrations
- creates migrations folder
- creates alembic.ini


Update all files

IMPORTANT
this line seemed to be missing to bind the route
app.register_blueprint(bp)

F5
curl http://localhost:5000

docker-compose up --build
curl http://localhost:5000

docker-compose exec app alembic revision --autogenerate -m "Initial migration"
docker-compose exec app alembic upgrade head


d ps
d6a79e79b164   postgres:14
docker exec -it d6a79e79b164 psql -U user -d app_db

\dt
