import boto3

lambda_client=boto3.client('lambda')

# Define the ELB name and SNS topic ARN
elb_name = "arn:aws:elasticloadbalancing:ap-south-1:295397358094:targetgroup/Swapna-TG/76cf154f0ffb628b"  # Replace with your TG ARN
sns_topic_arn = "arn:aws:sns:ap-south-1:295397358094:ASG_Scaling_Email_SNS"  # Replace with your SNS topic ARN

# Initialize the ELB and SNS clients
elb_client = boto3.client('elbv2')
sns_client = boto3.client('sns')

# lambda_function_code= """
# import boto3

# def lambda_handler(event, context):
#    # Describe the target health of registered instances
#    response = elb_client.describe_target_health(TargetGroupArn=elb_name)

#    # Check if any instances are unhealthy
#    unhealthy_instances = [instance for instance in response['TargetHealthDescriptions'] if instance['TargetHealth']['State'] != 'healthy']

# """


#    if unhealthy_instances:
#        # Build a detailed message about unhealthy instances
#        message = "Unhealthy instances found in ELB:\n"
#        for instance in unhealthy_instances:
#            message += f"Instance ID: {instance['Target']['Id']}\n"
#            message += f"Description: {instance['TargetHealth']['Description']}\n"
       
    #    # Publish the message to the SNS topic
    #    sns_client.publish(
    #        TopicArn=sns_topic_arn,
    #        Message=message,
    #        Subject="ELB Unhealthy Instances Alert"
    #    )

with open('index.py.zip','rb')as file:
    xyz=file.read()

# Create the Lambda function
response = lambda_client.create_function(
    FunctionName='lambda_Instance_Health_check',
    Runtime='python3.11',  
    Role='arn:aws:iam::295397358094:role/Boto3-swapna-lambda-role',
    Handler='index.lambda_handler',  # Assuming your code is in a file named 'index.py'
    Code={'ZipFile': xyz},
    Timeout=15,  
    MemorySize=128  
)   