import boto3
import sys



def upload_file_to_s3(local_file, bucket_name, s3_file):
    s3 = boto3.resource("s3",
                        region_name="us-east-2",
                        aws_access_key_id="aws_access key ",
                        aws_secret_access_key="aws_secret_access_key")
    bucket = s3.Bucket(bucket_name)
    bucket.upload_file(local_file, s3_file)
    
if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python script.py <local_file> <s3_file> <bucket_name>")
        sys.exit(1)
    local_file = sys.argv[1]  # First argument: local file path
    s3_file = sys.argv[2]   # Second argument: S3 file path
    bucket_name = sys.argv[3] # Or you can pass this as an argument too
    
    upload_file_to_s3(local_file, bucket_name, s3_file)