import boto3
import botocore

print("boto3:", boto3.__version__)
print("botocore:", botocore.__version__)

try:
    s3_client = boto3.client('s3')
    response = s3_client.list_buckets(
        MaxBuckets=123,
        ContinuationToken='',   # must be a real token or omit — empty string can misbehave
        Prefix='',
        BucketRegion='us-east-1'
    )
    print(response)
except botocore.exceptions.ParamValidationError as e:
    print("Version too old for these params:", e)
except botocore.exceptions.NoCredentialsError as e:
    print("No credentials configured:", e)
except botocore.exceptions.ClientError as e:
    print("AWS rejected the call (permissions/region):", e)