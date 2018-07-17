import boto3

questions = open('demo_qs.xml').read()
answers = open('demo_ans').read()

mturk = boto3.client('mturk',
                     region_name='us-east-1',
                     endpoint_url='https://mturk-requester-sandbox.us-east-1.amazonaws.com')

qual_response = mturk.create_qualification_type(
    Name='Duncan Lab Test',
    Description='This is a qualification test required for participation in the Duncan task.',
    Keywords='test,qualification,duncan',
    QualificationTypeStatus='Active',
    Test=questions,
    AnswerKey=answers,
    TestDurationInSeconds=300)

# The QUALIFICATION_TYPE_ID required to use this qualification in a HIT
# This can also be found on the MTurk website in the page of this created qualification
# print(qual_response['QualificationType']['QualificationTypeId'])
