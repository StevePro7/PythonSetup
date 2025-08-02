from fastapi import FastAPI
from config import get_settings
import uuid

# app = FastAPI()
#
# @app.get("/")
# async def root():
#     ADMIN_API_KEY = get_settings().ADMIN_API_KEY
#     return {"message": "Hello World"}


def main():
    ADMIN_API_KEY = get_settings().ADMIN_API_KEY
    #ADMIN_API_KEY = str(uuid.uuid4())
    print(f'{ADMIN_API_KEY}')


if __name__ == '__main__':
    main()