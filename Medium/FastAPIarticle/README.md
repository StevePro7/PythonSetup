Fast API — Repository Pattern and Service Layer
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
