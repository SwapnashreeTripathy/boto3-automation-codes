import boto3

# Initialize a session using Amazon EC2
client=boto3.client('elbv2')

response_TG = client.create_target_group(
    Name='Swapna-TG',
    Port=80,
    Protocol='HTTP',
    VpcId='vpc-0c5a8881cff1146d8',
    TargetType='instance'  # or 'ip' or 'lambda', can mention Instance ID or IP Address here
)

# target_group_arn = response_TG['TargetGroups'][0]['TargetGroupArn']

# print (response_TG['TargetGroups'][0]['TargetGroupArn'])
target_group_arn = (response_TG['TargetGroups'][0]['TargetGroupArn'])
# print (target_group_arn)

attach_instances=client.register_targets(
    TargetGroupArn=target_group_arn,
    Targets=[
        {
            'Id': 'i-017dd7e6070022d98',  #frontend
        },
        {
            'Id': 'i-0954f458460698169',   #backend
        }
    ]
)


TG_health_check_status=client.describe_target_health(
    TargetGroupArn=target_group_arn
    )

#or TG_health_check_status = client.describe_target_health(TargetGroupArn = target_group_arn)

for each_instance in TG_health_check_status['TargetHealthDescriptions']:
    print("Instance ID: ", each_instance['Target']['Id'])
    print ("Health check Status: ",each_instance['TargetHealth']['State'])
print (target_group_arn)