import os
import pickle
import boto3
import cv2 
import shutil

image_dir = 'D:\Raka\minio\Image\images'

with open('D:\Raka\minio\indices_test.pickle', 'rb') as f:
    indices = pickle.load(f)


for i in os.listdir(image_dir):
    if int(i[:-4]) in indices:
        test_dir = os.path.join('test_images', i)
        img_path = os.path.join(image_dir, i)
        shutil.copy(img_path,test_dir)
        print(i)
        
        
# s3 = boto3.client('s3',
#     aws_access_key_id='AKIA6FHPZ5V2ZQ5JVCES',
#     aws_secret_access_key='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')

# bucket_name = 'django-raka'

# for filename in os.listdir(image_dir):
#     # Construct the S3 key for the object
#     s3_key = f'django-raka/Images/{filename}'
    
#     # Check if the image_id is in indices (assuming indices is a list)
#     image_id = int(filename[:-4])
#     if image_id in indices:
#         # Open the file in binary read mode and upload it to S3
#         with open(os.path.join(image_dir, filename), 'rb') as file:
#             s3.upload_fileobj(file, bucket_name, s3_key)
#             print(f'Uploaded: {s3_key}')