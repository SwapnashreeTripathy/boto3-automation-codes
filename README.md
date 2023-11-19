# boto3-automation-codes
Develop a system that automatically manages the lifecycle of a web application hosted on EC2 instances, monitors its health, and reacts to changes in traffic by scaling resources. Furthermore, administrators receive notifications regarding the infrastructure's health and scaling events.
Web Application Deployment

## Table of Contents

1. **[Web Application Deployment](#web-application-deployment)**
    - Launching EC2 Instances with `boto3`
    - Configuring EC2 instances as Nginx web servers
    - Deploying the web application onto EC2 instances
    - Code snippets for launching instances: [boto3S3LaunchFE.py](https://github.com/sayanalokesh/DynamicWebApplication/blob/main/boto3S3LaunchFE.py), [boto3S3LaunchBE.py](https://github.com/sayanalokesh/DynamicWebApplication/blob/main/boto3InstanceBE.py).

2. **[Load Balancing with ELB](#load-balancing-with-elb)**
    - Deploying an Application Load Balancer (ALB) using `boto3`
    - Registering EC2 instances with the ALB
    - Code snippet for Load Balancing: [LoadBalancing.py](https://github.com/sayanalokesh/DynamicWebApplication/blob/main/LoadBalancing.py)

3. **[Auto Scaling Group (ASG) Configuration](#auto-scaling-group-asg-configuration)**
    - Creating an ASG with deployed EC2 instances as templates
    - Configuring scaling policies based on metrics
    - Code snippet for ASG configuration: [asgConfiguration.py](https://github.com/sayanalokesh/DynamicWebApplication/blob/main/asgConfiguration.py)

4. **[Lambda-based Health Checks & Management](#lambda-based-health-checks--management)**
    - Developing a Lambda function for health checks
    - Handling failing instances and notifications through SNS
    - Screenshots related to the code

5. **[S3 Logging & Monitoring](#s3-logging--monitoring)**
    - Content related to S3 Logging and monitoring (not provided in the given information)


    
### Web Application Deployment

During this phase, specific tasks are executed elegantly:
- Using `boto3`, I launched two EC2 instances (Frontend and Backend), configuring them as Nginx web servers. Subsequently, I deployed the web application onto these EC2 instances.
The code sequence involves instance launching, downloading Git dependencies, cloning files from the [repository](https://github.com/UnpredictablePrashant/TravelMemory.git)", navigating to TravelMemory, installing NodeJS and NPM, setting up reverse proxy, and executing the application on port 80.
Kindly refer to the codes for launching instances:
![image](https://github.com/SwapnashreeTripathy/boto3-automation-codes/assets/139486876/eb1b9892-daf0-4701-a9d7-f519f435cb8c)
![image](https://github.com/SwapnashreeTripathy/boto3-automation-codes/assets/139486876/f7191c10-a4b6-4893-84b9-dd62574afefb)
![image](https://github.com/SwapnashreeTripathy/boto3-automation-codes/assets/139486876/9a805acd-c434-4394-a933-d7dca9a510d1)
![image](https://github.com/SwapnashreeTripathy/boto3-automation-codes/assets/139486876/502ca636-ecb8-4f2d-a5e1-0b436470c290)
![image](https://github.com/SwapnashreeTripathy/boto3-automation-codes/assets/139486876/900ef934-5f0e-44eb-803c-9519c076c1c5)
![image](https://github.com/SwapnashreeTripathy/boto3-automation-codes/assets/139486876/ed478576-097a-474f-b244-7f00c708a9c0)
![image](https://github.com/SwapnashreeTripathy/boto3-automation-codes/assets/139486876/bd738205-0170-48f6-b45e-d7d82a8c0aa0)
![image](https://github.com/SwapnashreeTripathy/boto3-automation-codes/assets/139486876/4029f5fe-9ee3-489d-9ae2-86dcc5a322c2)
![image](https://github.com/SwapnashreeTripathy/boto3-automation-codes/assets/139486876/d774fe3d-2cd7-46a8-b92a-8ae3de4e4686)
![image](https://github.com/SwapnashreeTripathy/boto3-automation-codes/assets/139486876/c1433530-3173-4033-b630-fb503283b4fb)

   

