import boto3

lambda_client=boto3.client('lambda')

# Define the ELB name and SNS topic ARN
elb_name = "arn:aws:elasticloadbalancing:ap-south-1:295397358094:targetgroup/Swapna-TG/76cf154f0ffb628b"  # Replace with your TG ARN
sns_topic_arn = "arn:aws:sns:ap-south-1:295397358094:ASG_Scaling_Email_SNS"  # Replace with your SNS topic ARN

# Initialize the ELB and SNS clients
elb_client = boto3.client('elbv2')
sns_client = boto3.client('sns')

lambda_function_code= """


def lambda_handler(event, context):
   # Describe the target health of registered instances
   response = elb_client.describe_target_health(TargetGroupArn=elb_name)

   # Check if any instances are unhealthy
   unhealthy_instances = [instance for instance in response['TargetHealthDescriptions'] if instance['TargetHealth']['State'] != 'healthy']

"""
