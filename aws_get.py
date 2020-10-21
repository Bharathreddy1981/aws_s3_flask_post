import boto3
from botocore.client import Config
import aws_url_image
def mat(name):
    ACCESS_KEY_ID = "AKIAZNN5NBT72GR3NKP7"
    ACCESS_SECRET_KEY = "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"
    BUCKET_NAME = "flask121"

    k=name
    data = open(k, "rb")
    s3 = boto3.resource(
        "s3",
        aws_access_key_id=ACCESS_KEY_ID,
        aws_secret_access_key=ACCESS_SECRET_KEY,
        config=Config(signature_version="s3v4")
    )
    s3.Bucket(BUCKET_NAME).put_object(Key=k, Body=data)

    print("Done")
    url = aws_url_image.fun()
    # print(url)

    file_name = k
    final_url = url + file_name

    return {"final": final_url}

