import boto3

# # Create a key pair
# ec2 = boto3.client('ec2')
# key_pair_response = ec2.create_key_pair(KeyName='KeyPair01')
# key_material = key_pair_response['KeyMaterial']

# # Save the key to a file "KeyPair1.pem"
# with open('KeyPair01.pem', 'w') as key_file:
#     key_file.write(key_material)

keyName1='KeyPair60'

# Create an EC2 instance
ec2_resource = boto3.resource('ec2')
instances = ec2_resource.create_instances(
        ImageId="ami-0287a05f0ef0e9d9a",
        MinCount=1,
        MaxCount=1,
        InstanceType="t2.micro",
        KeyName="keyName1",
        Placement={'AvailabilityZone': 'ap-south-1b'}  # Specify the desired availability zone
    )


# Wait for the instance to be running
instances[0].wait_until_running()
# or , ec2.get_waiter('instance_running').wait(InstanceIds=[instance_id])

# Get the instance ID
instance_id = instances[0].id

# Attach EBS volume
ec2 = boto3.resource('ec2')
volume = ec2.create_volume(
    AvailabilityZone='ap-south-1b', # Replace with your actual availability zone
    Size=20,
    VolumeType='gp2'
)

# Wait for the volume to be available
volume_id = volume['VolumeId']
# Wait for the volume to be available
ec2.get_waiter('volume_available').wait(VolumeIds=[volume_id])


# Attach the volume to the instance
ec2.attach_volume(
    Device='/dev/sda1', # Replace with appropriate device name
    InstanceId=instance_id,
    VolumeId=volume_id
)

print(f"EBS volume {volume_id} attached to the instance {instance_id} in the same availability zone.")






