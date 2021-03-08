import logging
import boto3
from pprint import pprint
from botocore.exceptions import ClientError
import requests


from rekognition_objects import (
    RekognitionFace, show_bounding_boxes, show_polygons)

logger = logging.getLogger(__name__)

class RekognitionImage:
    def __init__(self, image, image_name, rekognition_client):
        self.image = image
        self.image_name = image_name
        self.rekognition_client = rekognition_client
    
    @classmethod
    def readingFile(cls, image_file_name, rekognition_client, image_name=None):
        with open(image_file_name, 'rb') as img_file:
            image = {'Bytes': img_file.read()}
        name = image_file_name if image_name is None else image_name
        return cls(image, name, rekognition_client)
    
    def detect_faces(self):
        try:
            response = self.rekognition_client.detect_faces(
                Image=self.image, Attributes=['ALL'])
            faces = [RekognitionFace(face) for face in response['FaceDetails']]
            logger.info("Detected %s faces.", len(faces))
        except ClientError:
            logger.exception("Couldn't detect faces in %s.", self.image_name)
            raise
        else:
            return faces


def emotioner():
    face_img = "test.jpg"
    rekognition_client = boto3.client('rekognition')
    face_img_usable = RekognitionImage.readingFile(
        face_img, rekognition_client)
    faces = face_img_usable.detect_faces()
    for face in faces[:3]:
        pprint(face.to_dict())


if __name__ == '__main__':
    emotioner()
