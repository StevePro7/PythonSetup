import cProfile
import pstats
from fastapi.testclient import TestClient
from main import app  # your FastAPI application

client = TestClient(app)

def profile_api():
    client.get("/your-endpoint")

profiler = cProfile.Profile()
profiler.enable()
profile_api()
profiler.disable()

stats = pstats.Stats(profiler).sort_stats("cumtime")
stats.print_stats(10)