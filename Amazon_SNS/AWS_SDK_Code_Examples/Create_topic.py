import json
import logging
import time
import boto3
from botocore.exceptions import ClientError

logger = logging.getLogger(__name__)

class SnsWrapper:
    """Encapsulates Amazon SNS topic and subscription functions."""
    def __init__(self, sns_resource):
        """
        :param sns_resource: A Boto3 Amazon SNS resource.
        """
        self.sns_resource = sns_resource

    def create_topic(self, name):
        """
        Creates a notification topic.

        :param name: The name of the topic to create.
        :return: The newly created topic.
        """
        try:
            topic = self.sns_resource.create_topic(Name=name)
            logger.info("Created topic %s with ARN %s.", name, topic.arn)
        except ClientError:
            logger.exception("Couldn't create topic %s.", name)
            raise
        else:
            return topic

def sns_example():
    sns_wrapper = SnsWrapper(boto3.resource('sns'))

    topic_name  = f'sns-an2-lsj-dev-test-{time.time_ns()}'
    topic       = sns_wrapper.create_topic(topic_name)
    print(f"Created Topic Name : {topic}")

if __name__ == '__main__':
    sns_example()