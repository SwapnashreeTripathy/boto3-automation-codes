import boto3
import zipfile

# File names
function_code_file = 'lambda.py'
zip_file = 'lambda.zip'

# Zip the Lambda function code
with zipfile.ZipFile(zip_file, 'w') as z:
    z.write(function_code_file)

# Read the zipped Lambda function code
with open(zip_file, 'rb') as file:
    lambda_code = file.read()

# Initialize the boto3 clients
lambda_client = boto3.client('lambda')
events_client = boto3.client('events')

# Define your Lambda function name and existing role ARN
function_name = 'lambda_Instance_Health_check'
role_arn = 'arn:aws:lambda:ap-south-1:295397358094:function:lambda_Instance_Health_check'  # Replace with your existing IAM role ARN

# Create the Lambda function
response = lambda_client.create_function(
    FunctionName=function_name,
    Runtime='python3.11',
    Role=role_arn,
    Handler='backup.lambda_handler',  # Replace 'backup' with your script's filename (without the extension)
    Code={
        'ZipFile': lambda_code,
    }
)

# Extract the ARN from the response
# Get information about the Lambda function
response1 = lambda_client.get_function(FunctionName=function_name)

# Extract the ARN from the response
lambda_arn = response1['Configuration']['FunctionArn']

print(f"The ARN of the Lambda function '{function_name}' is: {lambda_arn}")

# Create a rule to trigger the Lambda function every 10 minutes
response = events_client.put_rule(
    Name='TriggerLambdaEvery10Minutes',
    ScheduleExpression='rate(10 minutes)',
    State='ENABLED'
)

rule_arn = response['RuleArn']
print(f'The ARN of the created rule is: {rule_arn}')

# Add permission to the rule to trigger the Lambda function
response1 = lambda_client.add_permission(
    FunctionName='lambda_Instance_Health_check',
    StatementId='AllowCloudWatchToInvokeLambda',
    Action='lambda:InvokeFunction',
    Principal='events.amazonaws.com',
    SourceArn=response['RuleArn']
)

# Connect the rule to the Lambda function
response = events_client.put_targets(
    Rule='TriggerLambdaEvery10Minutes',
    Targets=[
        {
            'Id': '1',
            'Arn': lambda_arn,  # Use the variable containing the rule ARN
            'Input': '{}'
        }
    ]
)

