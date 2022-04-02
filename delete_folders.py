#!/usr/bin/env python3
import boto3

s3 = boto3.resource('s3')

#Modify the <Bucket Name> with S3 bucket name
#Script will get the values from current_year and previous_year scripts and will delete those folder in S3

bucket = s3.Bucket(<Bucket Name>)

def delete_folder(year,days):
    day=str(year)+"/"+str(days)+"/"
    for obj in bucket.objects.filter(Prefix=day):
        s3.Object(bucket.name,obj.key).delete()

