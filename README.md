# Migrate-Data-into-AWS-RDS-and-S3-Bucket-using-Lambda-Function
## Overview
In this project, I created a Lambda function that will request data from Guardian News API and when triggered, it will write the data into an AWS MySQL RDS instance and S3 Bucket.

![image_alt](https://github.com/aetekpo/Migrate-Data-into-AWS-RDS-and-S3-Bucket-using-Lambda-Function/blob/main/API%20Image.png?raw=true)

## Step-by-Step Guide for the project:
- **Step 1: Get the API Key**:

To get the API key that will pull the data from the Guardian News, click 👉 [here](https://open-platform.theguardian.com/documentation/?form=MG0AV3).

Note the API key generated from the website in a secure place because it will be needed in the python code to pull the data.

- **Step 2: Create MySQL RDS Database in AWS console**:

Follow the steps needed to create RDS in AWS console. When creating MySQL RDS instance in the console, make sure you take note of the variables such as Master username, Master password, Endpoint, Database name, Bucket name and save them in a secure place because you will need these variables later in other configurations.

- **Step 3: VPC inbound rules Setup for internet access**:

The inbound rules control the incoming traffic to your instances (MySQL RDS). They are rules that let data or clients into the security group. We have to set up the VPC for internet access.

![image_alt](https://github.com/aetekpo/Migrate-Data-into-AWS-RDS-and-S3-Bucket-using-Lambda-Function/blob/main/VPC_Image.png?raw=true)


- **Step 4: Test the connection between the AWS RDS and MySQL Workbench**:

After creating the RDS instance, we have to connect it to MySQL Workbench. The goal is to see if the RDS instance is connected to MySQL Workbench where we will do the data manipulation to see if the data is loaded in the database. 

![image_alt](https://github.com/aetekpo/Migrate-Data-into-AWS-RDS-and-S3-Bucket-using-Lambda-Function/blob/main/RDS%20Connection%20Image.png?raw=true)

- **Step 5: AWS S3 Bucket Setup**:

Follow the steps in AWS console on how to configure S3 bucket. The data will be stored in S3 bucket in AWS console.

![image_alt](https://github.com/aetekpo/Migrate-Data-into-AWS-RDS-and-S3-Bucket-using-Lambda-Function/blob/main/S3_Bucket_Image.png?raw=true)

- **Step 6: Lambda Function Setup**:

 We need to create a Lambda Function in AWS console that will fetch the data and Store in S3 and MySQL RDS. Before we create the lambda function, we need to set up the IAM (Identity and Access Management) for the lambda function.
   
  **a- Create role for the lambda function**: Every lambda function needs an execution role so that it has access to the right resources before it can run. After creating the role, we need to attach policies that grant permissions to the following services: AmazonS3FullAccess, CloudWatchLogsFullAccess, AmazonRDSDataFullAccess, AWSLambdaBasicExecutionRole.

 ![iamge_alt](https://github.com/aetekpo/Migrate-Data-into-AWS-RDS-and-S3-Bucket-using-Lambda-Function/blob/main/Roles_Policies_Image.png?raw=true)

  **b- Create the Lambda function in AWS console**: Follow the steps to create lambda function in AWS console. When creating the lambda function, make sure you select the execution role you just created under existing role.

  **c- Write the Python code for the lambda function**: Insert Python code that will pull the data from Guardian News API and store it in S3 and RDS instance.

  **d- Add layers to the lambda function**: Why do we have to create layers for the lambda function? In the python code, we have imported two modules (requests and pymysql) that are not integrated in AWS. In order for the code to run successfully, we have to create layer for each module. Packages for all dependencies were created and zip files were uploaded and attached to the function in AWS console. To watch video on how to create layers, click 👉 [here](https://www.youtube.com/watch?v=mTYp4lTWMAw). 
The Lambda function has the needed layers, the right IAM role, now we need to configure the environment variables.

  ![image_alt](https://github.com/aetekpo/Migrate-Data-into-AWS-RDS-and-S3-Bucket-using-Lambda-Function/blob/main/Layers.png?raw=true)

   **e- Configure the environment variables and Test the Lambda function**: Why do we have to configure the environment variables? In the Python code, we used environment variables for the API key, the bucket name, the guardian url, the RDS host, RDS user, RDS password, and RDS database. The required environment variables were created under the configuration setting. 

   ![image_alt](https://github.com/aetekpo/Migrate-Data-into-AWS-RDS-and-S3-Bucket-using-Lambda-Function/blob/main/Env_Variables_image.png?raw=true)

   **f- Deploy and test Lambda function**: After setting up the environment variables, the lambda function was deployed and tested.

   ![image_alt](https://github.com/aetekpo/Migrate-Data-into-AWS-RDS-and-S3-Bucket-using-Lambda-Function/blob/main/Test_Code.png?raw=true)

   **g- Schedule Lambda function with EventBridge**: The EventBridge trigger automatically invokes an AWS lambda function based on the defined schedule pattern. We created a rule in Amazon EventBridge and defined the schedule pattern on the frequency the data will be pulled. It was set to every 30 minutes. 

   **h- Check the data in MySQL WorkBench**: Log into MySQL Workbench and run MySQL Select statement. Data has been loaded successfully.

   ![image_alt](https://github.com/aetekpo/Migrate-Data-into-AWS-RDS-and-S3-Bucket-using-Lambda-Function/blob/main/MySQL_Image.png?raw=true)

   - **Step 7: Challenges faced while working on the project**:

     1- Try to figure out how to create layers for the lambda function. Refer to 👉 [here](https://www.youtube.com/watch?v=mTYp4lTWMAw).
     
     2- Try to configure the environment variables. Note that you don't have to provide the actual values of the variables in your code. They are just a placeholder. You have to provide them in the AWS console.

![image_alt](https://github.com/aetekpo/Migrate-Data-into-AWS-RDS-and-S3-Bucket-using-Lambda-Function/blob/main/Env_Variables_Code.png?raw=true).,

   

   
  
  
  

  
 



  



  

  



