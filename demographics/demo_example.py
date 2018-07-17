"""
Example of creating a HIT with the 'object' qualification.
Created by Calvin Choi, 7/14/2018
Written in Python 3.6.4
Requires Amazon's Boto3 SDK
"""

import boto3

# Constants for developer credentials and client information
# Information found on
# https://docs.aws.amazon.com/general/latest/gr/aws-sec-cred-types.html#access-keys-and-secret-access-keys
ACCESS_ID = ''
SECRET_KEY = ''
IS_PRODUCTION = False  # If false, uses sandbox

# Constants for the HIT
REWARD = '0.01'
LIFE_TIME_IN_SECONDS = 3600
ASSIGNMENT_DURATION_IN_SECONDS = 600
MAX_ASSIGNMENT = 9
TITLE = 'The title of the HIT'
DESCRIPTION = 'The description of the HIT.'
KEYWORDS = 'the,keywords,of,the,HIT'
AUTO_APPROVAL_DELAY_IN_SECONDS = 0
QUALIFICATION_TYPE_ID = ''  # See qua file for more information
# In this HIT, the worker needs a score of 100% on the qualification test


region_name = 'us-east-1'
aws_access_key_id = ACCESS_ID
aws_secret_access_key = SECRET_KEY

if IS_PRODUCTION:
    endpoint_url = 'https://mturk-requester.us-east-1.amazonaws.com'
else:
    endpoint_url = 'https://mturk-requester-sandbox.us-east-1.amazonaws.com'

client = boto3.client(
    'mturk',
    endpoint_url=endpoint_url,
    region_name=region_name,
    aws_access_key_id=aws_access_key_id,
    aws_secret_access_key=aws_secret_access_key,
)

# This will return $10,000.00 in the MTurk Developer Sandbox
# Uncomment to see account balance
# print(client.get_account_balance()['AvailableBalance'])

hit = client.create_hit(
    Reward=REWARD,
    LifetimeInSeconds=LIFE_TIME_IN_SECONDS,
    AssignmentDurationInSeconds=ASSIGNMENT_DURATION_IN_SECONDS,
    MaxAssignments=MAX_ASSIGNMENT,
    Title=TITLE,
    Description=DESCRIPTION,
    Keywords=KEYWORDS,
    AutoApprovalDelayInSeconds=AUTO_APPROVAL_DELAY_IN_SECONDS,
    QualificationRequirements=[{'QualificationTypeId': QUALIFICATION_TYPE_ID,
                                'Comparator': 'EqualTo',
                                'IntegerValues': [100]}]
)
