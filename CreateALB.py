import boto3
# Initializing a client for the AWS service
client=boto3.client('elbv2')

# Create the load balancer
response_LB = client.create_load_balancer(
    Name='Swapna-LB',
    Subnets=['subnet-0ea24e054cba9cad2','subnet-054d138c719f3f355','subnet-0ea185273ead71a27'],
    SecurityGroups=['sg-05c7242e0a0f43019']
)

# Attach an existing target group to the load balancer
load_balancer_arn = response_LB['LoadBalancers'][0]['LoadBalancerArn']
# Type=['response_LB'][0]['Type']
Target_Group_ARNs=['arn:aws:elasticloadbalancing:ap-south-1:295397358094:targetgroup/Swapna-TG/76cf154f0ffb628b']

# elbv2_client = boto3.client('autoscaling')

# attach_TG_TOLB = elbv2_client.aattach_load_balancer_target_group(
#     AutoScalingGroupName='my-auto-scaling-group',
#     TargetGroupARNs=Target_Group_ARNs
# )

#Create a Lister & Attach Target Group to LB
create_listener = client.create_listener(
    DefaultActions=[
        {
            'TargetGroupArn': 'arn:aws:elasticloadbalancing:ap-south-1:295397358094:targetgroup/Swapna-TG/76cf154f0ffb628b',
            'Type': 'forward',
        },
    ],
    LoadBalancerArn=load_balancer_arn,
    Port=80,
    Protocol='HTTP',
)

# Print the ARN of the created load balancer
print("Load Balancer Created and LB ARN is: ", load_balancer_arn)