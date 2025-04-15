import os
import yfinance as yf
import pandas as pd
from minio import Minio

# Load credentials from environment variables
minio_client = Minio(
    "localhost:9000",
    access_key=os.getenv("MINIO_ACCESS_KEY"),  
    secret_key=os.getenv("MINIO_SECRET_KEY"),  
    secure=False
)

# Download stock data
data = yf.download("AAPL", period="1d", interval="1h")

# Define local file path
local_file_path = "stock_data.csv"

# Save data to CSV
data.to_csv(local_file_path)
print(f"Stock data saved locally as {local_file_path}")

# Define MinIO bucket and object name
bucket_name = "stock-data-bucket"
object_name = "stock_data.csv"

# Create bucket if it doesn't exist
if not minio_client.bucket_exists(bucket_name):
    minio_client.make_bucket(bucket_name)
    print(f"Bucket '{bucket_name}' created")
else:
    print(f"Bucket '{bucket_name}' already exists")

# Upload file to MinIO
minio_client.fput_object(bucket_name, object_name, local_file_path)
print(f"File '{local_file_path}' uploaded to MinIO bucket '{bucket_name}' as '{object_name}'")
