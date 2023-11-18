import boto3
sns=boto3.client('sns',region_name='ap-south-1')
asg=boto3.client('autoscaling')


#Create SNS Topic
# create_sns_topic=sns.create_topic(
#     Name='ASG_Scaling_Email_SNS'
# )
# topic_arn=create_sns_topic['TopicArn']          #arn:aws:sns:ap-south-1:295397358094:ASG_Scaling_Email_SNS
# print('SNS Topic Created: ARN =', topic_arn)

#Create Subscription for above SNS 
# subscription_Email=sns.subscribe(
#     TopicArn=topic_arn,
#     Protocol='email',                           # Change as per the protocol--'http'/'https'/'email'/'sms'..etc.
#     Endpoint='kline.jacques@forkshape.com'
# )
# print("Subscription ARN:", subscription_Email['SubscriptionArn'])


# Update the Auto Scaling Group's Scaling Policy with SNS Topic ARN
response = asg.put_notification_configuration(
    AutoScalingGroupName='TG_ASG_Frontend',  
    NotificationTypes=['autoscaling:EC2_INSTANCE_LAUNCH', 'autoscaling:EC2_INSTANCE_TERMINATE'],
    TopicARN='arn:aws:sns:ap-south-1:295397358094:ASG_Scaling_Email_SNS'                                                      #the ARN of the SNS topic 
)
print(response)


