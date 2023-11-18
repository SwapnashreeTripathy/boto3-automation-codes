import boto3
autoscaling_client=boto3.client('autoscaling')
ec2_client=boto3.client('ec2')

instance_id='i-017dd7e6070022d98'

# Create an AMI of existing EC2
# create_ami=ec2_client.create_image(
#      InstanceId=instance_id,
#      Name='ST_Frntnd_AMI',
#     Description='AMI created from instance in Auto Scaling Group using Boto3',
#     NoReboot=True  # Set to True if you don't want the instance to reboot during the AMI creation process
# )

# print ("AMI created for frontend: ",create_ami['ImageId']) #ami-0a9d4e36933668b66





# print("Template has been configured!/n",response)

#Create Template EC2
# Launch_Template=ec2_client.create_launch_template(
#     LaunchTemplateName='ST_Frntd_Template',
#     VersionDescription='Version 1',
#     LaunchTemplateData={
#         'ImageId': 'ami-0a9d4e36933668b66',      
#         'InstanceType': 't2.micro',  
#         'KeyName': 'ST-keypair',  
#         'SecurityGroupIds': ['sg-05c7242e0a0f43019']  
#         }
# )
# print ("Template has been created: " , Launch_Template['LaunchTemplate']['LaunchTemplateId']) #lt-0447af12506e9c974



# launch_template_id='lt-0447af12506e9c974'                                         #Launch_Template['LaunchTemplate']['LaunchTemplateId']
# # Create auto scaling group
# create_ASG=autoscaling_client.create_auto_scaling_group(
#     AutoScalingGroupName='TG_ASG_Frontend',
#     LaunchTemplate= {
#         'LaunchTemplateName': 'ST_Frntd_Template',                                     #'ST_Frntd_Template', #LaunchConfigurationName
#         'Version': '$Default'  #$latest = can be used for latest version of Template
#     },                                              
    
#     MinSize=2,
#     MaxSize=4,
#     DesiredCapacity=2,
#     VPCZoneIdentifier='subnet-054d138c719f3f355, subnet-0ea24e054cba9cad2, subnet-0ea185273ead71a27',
#     TargetGroupARNs=[
#         'arn:aws:elasticloadbalancing:ap-south-1:295397358094:targetgroup/Swapna-TG/76cf154f0ffb628b',
#     ],

# )
# print("ASG created successfully.",create_ASG)


# Create scale out policy
scale_out_policy = autoscaling_client.put_scaling_policy(
    AutoScalingGroupName='TG_ASG_Frontend',
    PolicyName='TG_ASG_Frontend_POLICY', #name of the scaling policy.
    PolicyType='TargetTrackingScaling',
    TargetTrackingConfiguration={
        'PredefinedMetricSpecification': {
            'PredefinedMetricType': 'ASGAverageCPUUtilization', #When you create a target tracking scaling policy with a predefined metric type, you choose one metric from the list of predefined metrics. so from that list here we are using "verage CPU utilization of the Auto Scaling group.
        },
        'TargetValue': 50,
        # 'ScaleOutCooldown': 60,
        # 'ScaleInCooldown': 300, #after 5 mins Scale in when, AvergaeCPU utilization is below 50%
        }
    )