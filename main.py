import boto3

#Using Amazon S3
class S3_Buckets:
    s3 = boto3.client('s3')
    lb = s3.list_buckets()
    data = open('./imgs/test.jpg', 'rb')

    def __init__(self, bucket=None):
        pass

    def show_buckets(self):
        print("\nAvailable buckets: ")
        print("~~~~~~~~~~~~~~~~~~\n")
        for bucket in self.lb['Buckets']:
            print(bucket['Name'])
        print("\n~~~~~~~~~~~~~~~~~~\n")

    def upload_to_bucket(self):
        print('uploading')
        self.s3.upload_file(Key="")



sb = S3_Buckets('passportcheck')
sb.show_buckets()
sb.upload_to_bucket()