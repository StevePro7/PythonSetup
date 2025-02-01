# 10. Deployment
"""
uvicorn main:app --host 0.0.0.0 --port 8000 --workers 4
gunicorn -k uvicorn.workers.UvicornWorker main:app -w 4 -b 0.0.0.0:8000
"""