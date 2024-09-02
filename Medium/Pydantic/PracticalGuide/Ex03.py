# from pydantic import BaseModel, BeforeValidator, ValidationError
# import datetime
# from typing import Annotated
#
#
# def stamp2date(value):
#     if not isinstance(value, float):
#         raise ValidationError("incoming date must be a timestamp")
#     try:
#         res = datetime.datetime.fromtimestamp(value)
#     except ValueError:
#         raise ValidationError("Time stamp appears to be invalid")
#     return res
#
#
# class DateModel(BaseModel):
#     dob: Annotated[datetime.datetime, BeforeValidator(stamp2date)]
