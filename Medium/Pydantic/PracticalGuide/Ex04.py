# from pydantic import BaseModel, BeforeValidator, AfterValidator, ValidationError
# import datetime
# from typing import Annotated
#
#
#
# def one_year(value):
#     if value < datetime.datetime.today() - datetime.timedelta(days=365):
#         raise ValidationError("the date must be less than a year old")
#     return value
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
#     dob: Annotated[datetime.datetime, BeforeValidator(stamp2date), AfterValidator(one_year)]
