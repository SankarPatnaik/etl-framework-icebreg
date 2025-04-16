import boto3
import pyarrow as pa
import pyarrow.parquet as pq
import uuid
import os
from dotenv import load_dotenv

load_dotenv()

def write_to_s3_iceberg(df, target_config):
    table = pa.Table.from_pandas(df)
    filename = f"{uuid.uuid4()}.parquet"
    local_path = f"/tmp/{filename}"
    bucket = target_config['bucket']
    s3_key = f"{target_config['table']}/{filename}"

    pq.write_table(table, local_path)

    s3 = boto3.client('s3')
    s3.upload_file(local_path, bucket, s3_key)

    os.remove(local_path)
    print(f"Uploaded to S3: s3://{bucket}/{s3_key}")
