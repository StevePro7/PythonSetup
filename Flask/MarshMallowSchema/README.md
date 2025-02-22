pip install marshmallow
pip install marshmallow marshmallow-dataclass


SUMMARY
Serialize
object => dictionary        schema.dump()
dictionary => JSON          json.dumps()


Deserialize
JSON => dictionary          json.loads()
dictionary => object        schema.load()


# Serialize the User object to a dictionary
user_dict = user_schema.dump(user)

# Serialize the dictionary to a JSON string
user_json = json.dumps(user_dict, indent=4)


# Deserialize the JSON string back to a dictionary
user_dict_from_json = json.loads(user_json)

# Deserialize the dictionary back to a User object
user_obj = user_schema.load(user_dict_from_json)