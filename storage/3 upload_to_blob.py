import os
from azure.identity import DefaultAzureCredential
from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient
from azure.core.exceptions import ResourceExistsError, AzureError

# Retrieve environment variables
account_url = "https://<your-storage-account-name>.blob.core.windows.net"
container_name = "blobuploadcontainer"
files_to_upload = ["DALL·E 2024-06-11 19.40.20 - A detailed visualization of neural activation.webp", 
                   "DALL·E 2024-06-11 19.41.34 - A highly abstract visualization of neural activation.webp", 
                   "DALL·E 2024-06-11 19.42.35 - A completely abstract visualization of neural activation in an artificial intelligence model.webp"]  # List of files to upload

try:
    # Authenticate
    credential = DefaultAzureCredential()
    blob_service_client = BlobServiceClient(account_url=account_url, credential=credential)

    # Create a container if it doesn't exist
    container_client = blob_service_client.get_container_client(container_name)
    try:
        container_client.create_container()
        print(f"Container '{container_name}' created successfully.")
    except ResourceExistsError:
        print(f"Container '{container_name}' already exists.")

    # Upload each file
    for local_file_name in files_to_upload:
        blob_name = os.path.basename(local_file_name)
        blob_client = blob_service_client.get_blob_client(container=container_name, blob=blob_name)

        with open(local_file_name, "rb") as data:
            blob_client.upload_blob(data, overwrite=True)
            print(f"File '{local_file_name}' uploaded to blob '{blob_name}' successfully.")

except AzureError as e:
    print(f"An error occurred: {e}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
