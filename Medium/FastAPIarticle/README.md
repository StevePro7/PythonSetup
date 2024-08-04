Fast API — Repository Pattern and Service Layer
04-Aug-2024

Re-build - setup folder structure - all Python packages
pip install -r requirements.txt

Basic FastAPI project
config/databse.py
models/region.py
models/city.py
utils/init_db.py
schemas/region_schema.py
schemas/city_schema.py
main.py
F5 or uvicorn main:app --reload

Repository
abstracts the data access layer
repository/region_repository.py
repository/city_repository.py

Service
layer acts as intermediary btwn API endpoints and repository layer
service/region_service.py
service/city_service.py

Routers
define API endpoints using FastAPI routers
router/v1/region.py
router/v1/city.py
router/api.py

03-Aug-2024
https://medium.com/@kacperwlodarczyk/fast-api-repository-pattern-and-service-layer-dad43354f07a

https://github.com/DEENUU1/property-aggregator

Notes
/home/stevepro/Bitbucket/SteveProXNA/actionstuff/MediumDigest/2023/Python/FastAPI.txt


pip install -r requirements.txt

F5
curl http://0.0.0.0:8000
sudo fuser -k 8000/tcp

OR run and hotload changes
uvicorn main:app --reload

NB:
org. file says this but is deprecated
@app.on_event("startup")

Use lifespan instead as per 
https://fastapi.tiangolo.com/advanced/events


SQLite for Linux
https://sqlitebrowser.org/dl/#linux

sudo apt-get update
sudo apt-get install sqlitebrowser

create_tables()
right click database.db
Open in | Open in Associated Application


UPDATE code
F5
http://0.0.0.0:8000/docs


http://0.0.0.0:8000/api/v1/location/city
http://0.0.0.0:8000/api/v1/location/region


Postman
POST
Body | raw | JSON
{
    "name": "Dublin"
}

