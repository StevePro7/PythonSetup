import pickle
import pprint

def safe_load_pickle(path):
    # Optionally wrap in try/except to catch errors
    with open(path, "rb") as f:
        obj = pickle.load(f)
    return obj

def inspect(obj, depth=0, max_depth=3):
    """A recursive inspector that prints basic structure up to some depth."""
    indent = "  " * depth
    if depth > max_depth:
        print(indent + "…")
        return
    if isinstance(obj, dict):
        print(indent + f"dict, {len(obj)} keys:")
        for k, v in obj.items():
            print(indent + "  key:", repr(k))
            inspect(v, depth+2, max_depth)
    elif isinstance(obj, (list, tuple, set)):
        print(indent + f"{type(obj).__name__}, length {len(obj)}")
        for i, el in enumerate(obj[:10]):  # show only first few
            print(indent + f"  [{i}]:")
            inspect(el, depth+1, max_depth)
    else:
        # Base case: simple object
        print(indent + repr(obj))

if __name__ == "__main__":
    path = "model/greeting_model.pkl"
    path = "model/scaler.pkl"
    obj = safe_load_pickle(path)
    pprint.pprint(obj)  # this may be huge
    print("\n--- structure preview ---")
    inspect(obj)
