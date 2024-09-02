from pydantic import BaseModel
from typing import Union, Optional, List, Dict
from datetime import datetime


class MyFirstModel(BaseModel):
    first_name: str
    last_name: str


class MySecondModel(BaseModel):
    first_name: str
    middle_name: Union[str, None] # This means the parameter doesn't have to be sent
    title: Optional[str] # this means the parameter should be sent, but can be None
    last_name: str


class MyThirdModel(BaseModel):
    name: Dict[str: str]
    skills: List[str]
    holidays: List[Union[str, datetime]]