import boto3
from botocore.exceptions import NoCredentialsError, ClientError

class StaticWebsiteHosting:
    def __init__(self, aws_access_key, aws_secret_key, region_name="us-east-1"):
        self.s3 = boto3.client(
            's3',
            aws_access_key_id=aws_access_key,
            aws_secret_access_key=aws_secret_key,
            region_name=region_name
        )

    def create_bucket(self, bucket_name):
        try:
            self.s3.create_bucket(
                Bucket=bucket_name,
                CreateBucketConfiguration={
                    'LocationConstraint': self.s3.meta.region_name
                }
            )
            print(f"Bucket {bucket_name} created successfully!")
        except ClientError as e:
            print(f"Error: {e}")

    def enable_static_hosting(self, bucket_name, index_document="index.html", error_document="error.html"):
        try:
            self.s3.put_bucket_website(
                Bucket=bucket_name,
                WebsiteConfiguration={
                    'IndexDocument': {'Suffix': index_document},
                    'ErrorDocument': {'Key': error_document}
                }
            )
            print(f"Static website hosting enabled for {bucket_name}")
        except ClientError as e:
            print(f"Error: {e}")

    def upload_files(self, bucket_name, directory):
        import os
        for root, _, files in os.walk(directory):
            for file in files:
                full_path = os.path.join(root, file)
                s3_path = os.path.relpath(full_path, directory)
                try:
                    self.s3.upload_file(full_path, bucket_name, s3_path)
                    print(f"Uploaded {file} to {bucket_name}/{s3_path}")
                except NoCredentialsError:
                    print("Credentials not available")
