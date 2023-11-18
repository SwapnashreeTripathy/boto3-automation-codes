import boto3

autoscaling_client = boto3.client('autoscaling')
cloudwatch_client = boto3.client('cloudwatch')

# autoscaling_group_name ='ASG_Frontend'
# launch_configuration_name = 'ST_Frntd_Template'  
# desired_capacity = 2
# min_capacity = 2
# max_capacity = 6

# autoscaling_client.create_auto_scaling_group(
#     AutoScalingGroupName=autoscaling_group_name,
#     LaunchConfigurationName=launch_configuration_name,
#     MinSize=min_capacity,
#     MaxSize=max_capacity,
#     DesiredCapacity=desired_capacity,
# )

autoscaling_group_name ='ASG_Frontend'
alarm_name = 'YourCPUAlarmName'
metric_name = 'CPUUtilization'
namespace = 'AWS/EC2'
comparison_operator = 'GreaterThanOrEqualToThreshold'
threshold = 50.0  # 50% CPU utilization
evaluation_periods = 1
period = 300  # 5-minute intervals
alarm_actions = [autoscaling_group_name]

cloudwatch_client.put_metric_alarm(
    AlarmName=alarm_name,
    AlarmDescription='Scale up when CPU utilization is high',
    ComparisonOperator=comparison_operator,
    EvaluationPeriods=evaluation_periods,
    MetricName=metric_name,
    Namespace=namespace,
    Period=period,
    Statistic='Average',
    Threshold=threshold,
    AlarmActions=alarm_actions,
)

autoscaling_client.put_notification_configuration(
    AutoScalingGroupName=autoscaling_group_name,
    NotificationTypes=['autoscaling:EC2_INSTANCE_TERMINATE'],
    TopicARN='arn:aws:sns:your-region:your-account:your-topic'
)

print("Auto Scaling Group and CloudWatch alarm configured successfully.")
