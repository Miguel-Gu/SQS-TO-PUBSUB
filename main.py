from google.cloud import pubsub_v1
import boto3
import json
import os


PROJECT_ID = os.getenv("PROJECT_ID")
AWS_ACCESS_KEY_ID = os.getenv("AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY = os.getenv("AWS_SECRET_ACCESS_KEY")
SQS_QUEUE = os.getenv("SQS_QUEUE")
PUBSUB_TOPIC = os.getenv("PUBSUB_TOPIC")

def handler(request):

    session = boto3.Session(
        aws_access_key_id = AWS_ACCESS_KEY_ID,
        aws_secret_access_key = AWS_SECRET_ACCESS_KEY,
        region_name='sa-east-1'
    )
    sqs = session.resource('sqs')
    publisher = pubsub_v1.PublisherClient()

    queue = sqs.get_queue_by_name(QueueName= SQS_QUEUE)
    topic_path = publisher.topic_path(PROJECT_ID, PUBSUB_TOPIC)

    more_messages = True
    while more_messages:

        messages = queue.receive_messages(
            AttributeNames=['All'],
            MessageAttributeNames=['All'],
            MaxNumberOfMessages=10,
            WaitTimeSeconds=5
        )

        if(len(messages) >= 2):
        
            for msg in messages:
                data = json.loads(msg.body)['Message']
                publisher.publish(topic_path, data.encode("utf-8"))
                msg.delete()

            more_messages = True
        
        else:
            more_messages = False

    return('executed')

handler("ok")