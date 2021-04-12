""" 
         .-.-.  .-.-.  .-.-.  .-.-.  .-.-.  .-.-.  .-.-.  .-.-.  .-.-.  .-.-.  .-.-.  .-.-. 
        ( E .' ( n .' ( g .' ( a .' ( g .' ( e .' ( m .' ( e .' ( n .' ( t .' ( A .' ( I .'
         `.(    `.(    `.(    `.(    `.(    `.(    `.(    `.(    `.(    `.(    `.(    `.(

Description : Code to call Amazon Rekognition API for Emotional analysis
Working directory: 
Input       : 

"""
# Import relevant libraries
import boto3
import json
import os
import argparse

# Import credentials files
credentials=json.load(open('../config/credentials.json','rb'))
access_key_id = credentials["Access key ID"]
secret_access_key = credentials["Secret access key"]

# Activate web services
client = boto3.client('rekognition', region_name='us-east-1', aws_access_key_id = access_key_id, aws_secret_access_key= secret_access_key)


def reko(imagePath,savePath):
    # Load image
    with open(imagePath ,'rb') as source_image:
        source_bytes = source_image.read()

    # Use web services
    response_face_emotion = client.detect_faces(Image={'Bytes':source_bytes},Attributes=['ALL']) # This part can be modify if user need to access the images from S3

    _, tail = os.path.split(imagePath) # To get the file name from path

    # Save response
    json.dump(response_face_emotion,open(savePath+tail.split(".")[0]+".json","w")) # Input file name and JSON file will be same

if __name__=="__main__":

    path = os.path.abspath(os.path.join(os.path.dirname(__file__), "./..")).replace("\\","/")

    # Get user supplied values
    parser=argparse.ArgumentParser(description='AWS rekognition service utilization tool')
    parser.add_argument("-i","--imagePath",type=str,default=path+'/db/input/images/frame33.jpg',help='Input image')
    parser.add_argument("-s","--savePath",type=str,default=path+'/out/',help='JSON output location')
    args=parser.parse_args()
    
    reko(args.imagePath,args.savePath)