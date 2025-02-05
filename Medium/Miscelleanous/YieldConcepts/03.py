def fetch_data_from_api(api_url, page=1):
    while True:
        response = request_page(api_url, page)
        if not response['data']:
            break
        yield response['data']
        page += 1


def request_page(api_url, page=1):
    return f"{api_url}-{page}"


def process_page(data: str):
    print(data)


# Process each page as it is retrieved
for page_data in fetch_data_from_api("https://exmple.com/api/users"):
    process_page(page_data)
