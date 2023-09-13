import boto3

def get_csv_to_s3(bucket_name, s3_key, file_name):
    s3 = boto3.client('s3')
    try:
        s3.download_file(bucket_name, s3_key, file_name)
        print("File download successfully to S3")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

bucket_name = 'test1-2409'
file_name = 'data.xlsx'
s3_key = 'stat1.xlsx'

get_csv_to_s3(bucket_name, s3_key, file_name)





