import boto3
from botocore.client import Config
import aws_url_image
def cat():
    ACCESS_KEY_ID = "AKIAZNN5NBT7VXAFB64K"
    ACCESS_SECRET_KEY = "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"
    BUCKET_NAME = "flask121"

    #k=value["image"]
    #print(k)


    data = open("C:\Users\vanga\Desktop\nature.jpg","rb")

    s3 = boto3.resource(
        "s3",
        aws_access_key_id=ACCESS_KEY_ID,
        aws_secret_access_key=ACCESS_SECRET_KEY,
        config=Config(signature_version="s3v4")
    )
    s3.Bucket(BUCKET_NAME).put_object(Key="bharathreddy.jpg", Body=data)

    print("Done")



    url=aws_url_image.fun()
    #print(url)

    file_name="bharathreddy.jpg"
    final_url=url+file_name


    return {"final":final_url}





