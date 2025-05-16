from google.cloud import storage


def list_buckets():
    client = storage.Client()
    buckets = client.list_buckets()
    for bucket in buckets:
        print(bucket)


def list_folders():
    bucket_name = "steveprobucket"
    folder_name = "steveprofolder"

    client = storage.Client()
    blobs = client.list_blobs(bucket_or_name=bucket_name, delimiter="/", prefix=folder_name)

    for blob in blobs:
        print(blob.name)


if __name__ == '__main__':
    list_folders()
    #list_buckets()


