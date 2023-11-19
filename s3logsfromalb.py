import boto3

# Initialize the Boto3 clients
elbv2_client = boto3.client('elbv2')
s3_client = boto3.client('s3')

# Specify the ALB ARN and the S3 bucket name
load_balancer_arn = 'arn:aws:elasticloadbalancing:ap-south-1:295397358094:loadbalancer/app/Swapna-LB/1349774d2bb6b9d1'
bucket_name = 'S3-log-monitor'

# Enable access logs for the ALB
response = elbv2_client.modify_load_balancer_attributes(
    LoadBalancerArn=load_balancer_arn,
    Attributes=[
        {
            'Key': 'access_logs.s3.enabled',
             'Value': 'true'
        },
        {
            'Key': 'access_logs.s3.bucket',
            'Value': bucket_name
        },
        # Optionally, you can set a prefix for the log files within the bucket
        {
            'Key': 'access_logs.s3.prefix',
            'Value': 'logs'
        }
    ]
)

print("ALB access logs are configured to be stored in the specified S3 bucket.")
