from google.cloud import storage
from google.cloud.storage.client import Client

def init_storage_client() -> Client:
    return storage.Client()

def upload_file(bucket_name, blob_name, file_name):
    client: Client = init_storage_client()
    bucket = client.bucket(bucket_name)

    destination_blob_name: str = f"{blob_name}{file_name}"
    blob = bucket.blob(destination_blob_name)
    blob.upload_from_filename(file_name)
    print("the end")

def download_file(bucket_name, blob_name, file_name):
    client: Client = init_storage_client()
    bucket = client.bucket(bucket_name)

    blob = bucket.blob(blob_name)
    blob.download_to_filename(file_name)
    print("the end")

print("beg")
#upload_file("steveprobucket", "XXsteveproupload.txt", "steveprofolder")
#download_file("steveprobucket", "steveprofolder/", "steveproupload.txt")

bucket_name: str = "steveprobucket"
blob_name: str = "suzannefolder/"
file_name: str = "adriana.txt"
#download_file(bucket_name, blob_name, file_name)
upload_file(bucket_name, blob_name, file_name)
print("end")