import boto3

# Create a key pair
# ec2 = boto3.client('ec2')
# key_pair_response = ec2.create_key_pair(KeyName='KeyPair67')
# key_material = key_pair_response['KeyMaterial']

# # # Save the key to a file "KeyPair1.pem"
# with open('KeyPair67.pem', 'w') as key_file:
#         key_file.write(key_material)


# Initialize a session using Amazon EC2
ec2_resource = boto3.resource('ec2')
#or, ec2_resource = boto3.resource('ec2', region_name='ap-south-1')  # You can set your desired region

# Create an EC2 instance
instances = ec2_resource.create_instances(
        ImageId="ami-0287a05f0ef0e9d9a",
        MinCount=1,
        MaxCount=1,
        InstanceType="t2.micro",
        KeyName='ST-keypair',
        SecurityGroupIds=['sg-05c7242e0a0f43019'],  # Ensure the security group exists and allows appropriate traffic
        # Placement={'AvailabilityZone': 'ap-south-1b'},  # Specify the desired availability zone
        UserData='''#!/bin/bash
                sudo apt-get update -y
                sudo apt-get install -y nginx
                curl -s https://deb.nodesource.com/setup_18.x | sudo -E bash -
                sudo apt install -y nodejs
                cd /home/ubuntu/
                git clone https://github.com/SwapnashreeTripathy/Deploy_MERNapp_onAWS_EC2Server.git
                cd /home/ubuntu/Deploy_MERNapp_onAWS_EC2Server/frontend/
                sudo npm install
                sudo systemctl start nginx
                sudo lsof -t -i tcp:80 -s tcp:listen | sudo xargs kill
                npm start''',
        TagSpecifications=[
        {
            'ResourceType': 'instance',
            'Tags': [
                {
                    'Key': 'Name',
                    'Value': 'swapna-Frontend'
                }
            ]
        }
    ]
)



# Wait for the instance to be running
for instance in instances:
    instance.wait_until_running()
    # or , ec2.get_waiter('instance_running').wait(InstanceIds=[instance_id])
    print(f" {instance.id} : Instance is now created ")










