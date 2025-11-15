from typing import Annotated
from pydantic import TypeAdapter, Field

UserId = Annotated[int, Field(gt=0)]
user_id_adapter = TypeAdapter(UserId)

def load_user(uid_raw):
    uid = user_id_adapter.validate_python(uid_raw)
    print("Loading user", uid)