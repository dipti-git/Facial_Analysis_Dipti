import boto3
import base64
import json
import os

client = boto3.client('rekognition')
file = open('engineer.jpg', 'rb').read()

response = client.detect_faces(
    Image={
        'Bytes': file,
    },

    Attributes=['ALL']
)


for face in response['FaceDetails']:

    print('The detected face of the candidate is of ' +
          str(face['Gender']['Value']))

    print('The age of the candidate seems to be in between ' +
          str(face['AgeRange']['Low']) + ' and ' + str(face['AgeRange']['High']) + 'years old.')

    Sunglass = str(face['Sunglasses']['Value'])
    if Sunglass == 'True':
        print('The candidate is wearing Sunglasses.')

    else:
        print('The detected face is not wearing Sunglasses.')

    Mustaches = str(face['Mustache']['Value'])
    
    if Mustaches == 'True':
        print('The detected face has Mustache.')

    else:
        print('The detected face is of female, there is no mustache present. ')

    Smiles = str(face['Smile']['Value'])
    
    if Smiles == 'True':
        print('The candidate is smiling.')

    else:
        print('The candidate is not smiling. ')

    for emotion in face['Emotions']:
        print('The emotions within the picture includes ' +
              emotion['Type'] + ' with  '+ str(emotion['Confidence']) + ' confidence.')


