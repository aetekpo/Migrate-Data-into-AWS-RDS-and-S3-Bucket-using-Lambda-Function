# Migrate-Data-into-AWS-RDS-and-S3-Bucket-using-Lambda-Function
## Overview
In this project, I would like to create a Lambda function that will be triggered when data is retrieved from The Guardian News API, and then writes the data into an S3 bucket and an AWS MySQL RDS instance.
(Add project overview Image here)
## Step-by-Step Guide:
- **Step 1: Get the API Key**:

To get the API Key that will pull the data from the Guardian News website, you need to sign up to the following website:

Click 👉 [here](https://open-platform.theguardian.com/documentation/?form=MG0AV3)

Note the API key generated from the website in a secure place because it will to be used in the python code to pull the data

- **Step 2: MySQL RDS Databse Setup**:

When creating MySQL RDS instance in AWS console, make sure you take note of the Master username, Master password, Endpoint, Database name, Bucket name and save them in a secure place because you will need then later in other configurations.

- **Step 3: VPC inbound rules Setup for internet access**:

The inbound rules control the incoming traffic to your instances. They are rules that let data or clients into the security group.

- **Step 4: Test the connection between the AWS RDS and MySQL Workbench**:

The goal is to see if your AWS RDS instance is connected to MySQL Workbench where you will do the data manipulation.

- **Step 5: AWS S3 Bucket Setup**:

Configure S3 bucket in AWS console where the data will be stored.

- **Step 6: Lambda Function Setup**:

 We need to create a Lambda Function in AWS console that will Fetch the data and Store in S3 and MySQL RDS. Before we create the lambda function, we need to set up the IAM (Identity and Access Management) for the lambda function
   
  **a- Create role for the lambda function**: A lambda function needs an execution role so that it has access to the right resources in order to run. Give permissions policies to AmazonS3FullAccess, CloudWatchLogsFullAccess, AmazonRDSDataFullAccess, AWSLambdaBasicExecutionRole.

  **b- Create the Lambda function in AWS console**: When creating the lambda function, make sure you select the execution role you just created under existing role.

  **c- Write the python code for the lambda function**: Insert python code that will pull the data from Guardian News API and store it in S3 and RDS instance.

  **d- Add layers to the lambda function**: Why do we have to create a layers for the lambda function? We have to create layers (requests and pymysql) modules are not integrated in AWS. Packages for all dependencies were created and zip file was uploaded in AWS console. To watch video on how to create layers, click 👉 [here](https://www.youtube.com/watch?v=mTYp4lTWMAw). 

The Lambda function has the needed layers, right IAM role, now we need to configure the environment variables

   **e- Configure the environment variables and Test the Lambda function**: Why do we have to configure the environment variables? In the python code, we used environment variables for the API key, the bucket name, the guardian url, the RDS host, RDS user, RDS password, and RDS database. Add the required environment variables and test the function (ADD image.)

   **e- Schedule Lambda function with EventBridge**: Create a rule in Amazon EventBridge and define the schedule pattern on how the data will be pulled. For example, it can be every 15 or 30 minutes. 

   
  
  
  

  
 



  



  

  



