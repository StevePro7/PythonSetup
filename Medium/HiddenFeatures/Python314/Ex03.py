def process_request(request):
    match request:
        # Guard expressions using 'if' within patterns
        case {"method": "GET", "path": path} if path.startswith("/api/"):
            return f"API GET request to {path}"
        
        case {"method": "POST", "data": data} if len(data) > 1000:
            return "Large POST request - processing with worker queue"
        
        case {"method": "POST", "data": data} if len(data) <= 1000:
            return "Small POST request - processing immediately"
        
        case {"method": method, "path": path} if method in ["PUT", "DELETE"]:
            return f"Modifying operation: {method} on {path}"
        
        case _:
            return "Unknown request format"

# Test the enhanced pattern matching
requests = [
    {"method": "GET", "path": "/api/users"},
    {"method": "POST", "data": "x" * 1500},
    {"method": "POST", "data": "small payload"},
    {"method": "DELETE", "path": "/users/123"}
]

for req in requests:
    print(process_request(req))