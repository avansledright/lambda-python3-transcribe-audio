#!/usr/bin/python3
from __future__ import print_function
import boto3
import json
import time
import urllib
from urllib.parse import unquote_plus


s3 = boto3.client('s3')
transcribe = boto3.client('transcribe')

def lambda_handler(event,context):
    sourcebucket = event['Records'][0]['s3']['bucket']['name']
    key = unquote_plus(event['Records'][0]['s3']['object']['key'])
    print('Source Bucket '+ sourcebucket)
    print('Printing Key '+ key)

    try:
        print("Transcribing the file")
        timestr = time.strftime("%Y%m%d-%H%M%S")
        job_name = 'filetranscription'+timestr
        job_uri = 's3://'+sourcebucket+'/'+key
        transcribe.start_transcription_job(
            TranscriptionJobName=job_name ,
            Media = {'MediaFileUri': job_uri},
            LanguageCode='en-US'
        )
    except Exception as e:
        print(e)
        print('Error getting object {} from bucket {} make sure they exist and your bucket name is correct')
        raise e
