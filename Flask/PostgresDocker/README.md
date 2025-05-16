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

Implement
01.
docker-compose exec app alembic revision --autogenerate -m "Initial migration"
INFO  [alembic.runtime.migration] Context impl PostgresqlImpl.
INFO  [alembic.runtime.migration] Will assume transactional DDL.
  Generating /app/migrations/versions/28271b725a81_initial_migration.py ...  done

02.
docker-compose exec app alembic upgrade head
INFO  [alembic.runtime.migration] Context impl PostgresqlImpl.
INFO  [alembic.runtime.migration] Will assume transactional DDL.
INFO  [alembic.runtime.migration] Running upgrade  -> 28271b725a81, Initial migration


d ps
d6a79e79b164   postgres:14
docker exec -it d6a79e79b164 psql -U user -d app_db

\dt


INITIAL migration no data - why?
because need to import DB models info env.py
from app.models import *


docker-compose up --build
docker-compose exec app alembic revision --autogenerate -m "Initial migration"
docker-compose exec app alembic upgrade head

docker exec -it 51f1d3c71158 psql -U user -d app_db
\dt
\dt user
\d user
SELECT * FROM public.user;
INSERT INTO public.user(username) VALUES('stevepro');



docker-compose down --volumes
docker-compose exec app env 


docker exec -it 8e757e30112c psql -U user -d app_db


LATEST
docker-compose up --build
docker-compose exec app alembic revision --autogenerate -m "Initial migration"
docker-compose exec app alembic upgrade head
docker exec -it 3882af2d385d psql -U user -d app_db
SELECT * FROM public.user;
INSERT INTO public.user(username) VALUES('stevepro');
curl http://localhost:5000/users
[{"id":1,"username":"stevepro"}]
docker-compose down --volumes


SEED
docker-compose up --build
docker-compose exec app alembic revision --autogenerate -m "Initial migration"
docker-compose exec app alembic upgrade head

docker exec -it 3882af2d385d psql -U user -d app_db
SELECT * FROM public.user;
docker-compose exec app python seed.py
curl http://localhost:5000/users
docker-compose down --volumes


Attempt to run PostgreSQL database running in a Docker container
while executing Alembic migrations locally (e.g. from PyCharm)

configure networking so that local application can connect to the database
inside the container

docker-compose up -d

IMPORTANT
update alembic.ini
sqlalchemy.url = postgresql://user:password@localhost:5432/app_database

Terminal
export DATABASE_URL="postgresql://user:password@localhost:5432/app_database"

alembic revision --autogenerate -m "Initial migration"
alembic upgrade head

F5
curl http://localhost:5000/users
[]

python seed.py
curl http://localhost:5000/users
//data


MAC
psycopg2-binary==2.9.9
OR Mac
/Applications/Postgres.app/Contents/Versions/12/bin/psql -h localhost -U user -d app_database


SUMMARY
MacOS
alembic.ini
sqlalchemy.url = postgresql://postgres:@localhost:5432/app_database
username    postgres
passowrd

OR
Linux
docker-compose up -d

export DATABASE_URL="postgresql://user:password@localhost:5432/app_database"
psql -h localhost -U user -d app_database

alembic revision --autogenerate -m "Initial migration"
alembic upgrade head

SELECT * FROM public.user;
0 rows

python seed.py
2 rows

F5
curl http://localhost:5000
curl http://localhost:5000/users

docker-compose down


