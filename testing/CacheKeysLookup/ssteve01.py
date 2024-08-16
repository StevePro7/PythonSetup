my_dict: dict = {
    "Steven Glen Boland": "AB123",
    "Steve Vai": "XY987"
}


my_dict2 = {
    "Apple": "Fruit",
    "Banana": "Fruit",
    "Cherry": "Fruit",
    "apricot": "Fruit",
    "grape": "Fruit"
}



def contains_partial_key(d: dict, search_str: str) -> (bool, str):
    # Convert search string to lowercase
    search_str = search_str.lower()

    # Iterate over the dictionary keys
    for key in d:
        # Convert key to lowercase and check if search string is a substring
        if search_str in key.lower():
            return True, key
    return False, ""


# Example usage
first_name = "Steven"
last_name = "Glen"

foundA, key1 = contains_partial_key(my_dict, first_name)
foundB, key2 = contains_partial_key(my_dict, last_name)
if foundA and foundB and key1 == key2:
    print(f"FOUND '{first_name}' '{last_name}' = '{key1}' and '{key2}'")
else:
    print(f"Not found '{first_name}' '{last_name}'.")
