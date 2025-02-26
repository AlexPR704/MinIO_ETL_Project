import yfinance as yf
import pandas as pd
from minio import Minio
import os

# Download stock data
data = yf.download("AAPL", period="1d", interval="1h")

# Define local file path
local_file_path = "stock_data.csv"

# Save data to CSV
data.to_csv(local_file_path)

print(f"Stock data saved locally as {local_file_path}")

# MinIO Configuration
minio_client = Minio(
    "localhost:9000",  # MinIO address
    access_key="user",  # Change to your MinIO username
    secret_key="password",  # Change to your MinIO password
    secure=False  # MinIO runs on HTTP, so this should be False
)

# Define MinIO bucket and object name
bucket_name = "stock-data-bucket"
object_name = "stock_data.csv"

# Create bucket if it doesn't exist
found = minio_client.bucket_exists(bucket_name)
if not found:
    minio_client.make_bucket(bucket_name)
    print(f"Bucket '{bucket_name}' created")
else:
    print(f"Bucket '{bucket_name}' already exists")

# Upload file to MinIO
minio_client.fput_object(bucket_name, object_name, local_file_path)
print(f"File '{local_file_path}' uploaded to MinIO bucket '{bucket_name}' as '{object_name}'")
