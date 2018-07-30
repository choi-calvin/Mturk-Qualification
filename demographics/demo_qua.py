# Documentation and guide can be found at
# https://github.com/hyun20005/Mturk-Qualification

import os
import boto3

AWS_ACCESS_KEY = ''
AWS_SECRET_KEY = ''
IS_SANDBOX = True

NAME = 'Name of the qualification'
DESCRIPTION = 'Description for the qualification.'
KEYWORDS = 'separated,by,commas'
TEST_DURATION_IN_SECONDS = 300

############################
# DO NOT CHANGE CODE BELOW #
############################

dir_name = os.path.dirname(__file__)
questions = open(os.path.join(dir_name, 'demo_qs.xml')).read()
answers = open(os.path.join(dir_name, 'demo_ans.xml')).read()

if IS_SANDBOX:
    endpoint_url = 'https://mturk-requester-sandbox.us-east-1.amazonaws.com'
else:
    endpoint_url = 'https://mturk-requester.us-east-1.amazonaws.com'

mturk = boto3.client('mturk',
                     aws_access_key_id=AWS_ACCESS_KEY,
                     aws_secret_access_key=AWS_SECRET_KEY,
                     region_name='us-east-1',
                     endpoint_url=endpoint_url)

qual_response = mturk.create_qualification_type(
    Name=NAME,
    Description=DESCRIPTION,
    Keywords=KEYWORDS,
    QualificationTypeStatus='Active',
    Test=questions,
    AnswerKey=answers,
    TestDurationInSeconds=TEST_DURATION_IN_SECONDS)
