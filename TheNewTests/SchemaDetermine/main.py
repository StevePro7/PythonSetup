def inspect_types(d):
    if isinstance(d, dict):
        for key, value in d.items():
            print(f"Key: {key}, Type: {type(key)}")
            print(f"Val: {value}, Type: {type(value)}")
            if isinstance(value, dict):
                inspect_types(value)
            elif isinstance(value, list):
                for item in value:
                    if isinstance(item, dict):
                        inspect_types(item)


param_grid = {
    'X': 0.001,
    'F': {
        "foo": "bar"
    }
}

param_grid = {
    'C': [0.001, 0.01, 0.1, 1, 10, 100],
    'gamma': [0.001, 0.01, 0.1, 1, 10, 100]
}

inspect_types(param_grid)
