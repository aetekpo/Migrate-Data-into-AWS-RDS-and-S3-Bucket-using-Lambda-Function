"""
Date: 02/17/2025
Author: Asserewou Etekpo
Description: This is a lambda function that is triggered by a CloudWatch event rule. 
The function will call the Guardian API to get the latest news and send it to the S3 and RDS.
"""
import os
import json
import boto3
import requests
import pymysql
from datetime import datetime

# Configuration
GUARDIAN_API_KEY = os.environ['GUARDIAN_API_KEY']
GUARDIAN_API_URL = "https://content.guardianapis.com/search"
S3_BUCKET_NAME = os.environ['S3_BUCKET_NAME']
RDS_HOST = os.environ['RDS_HOST']
RDS_USER = os.environ['RDS_USER']
RDS_PASSWORD = os.environ['RDS_PASSWORD']
RDS_DB = os.environ['RDS_DB']

def lambda_handler(event, context):
    try:
        # Step 1: Fetch data from Guardian News API
        params = {
            'api-key': GUARDIAN_API_KEY,
            'page-size': 10  # Adjust as needed
        }
        response = requests.get(GUARDIAN_API_URL, params=params)
        data = response.json()

        if response.status_code != 200:
            raise Exception(f"API request failed: {data}")

        articles = data.get('response', {}).get('results', [])

        # Step 2: Store data in S3
        s3_client = boto3.client('s3')
        timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
        s3_key = f"guardian-news/{timestamp}.json"
        s3_client.put_object(
            Bucket=S3_BUCKET_NAME,
            Key=s3_key,
            Body=json.dumps(articles)
        )

        # Step 3: Load data into MySQL RDS
        connection = pymysql.connect(
            host=RDS_HOST,
            user=RDS_USER,
            password=RDS_PASSWORD,
            database=RDS_DB
        )
        cursor = connection.cursor()

        # Create table if it doesn't exist
        create_table_query = """
        CREATE TABLE IF NOT EXISTS guardian_articles (
            id INT AUTO_INCREMENT PRIMARY KEY,
            title VARCHAR(255),
            section_name VARCHAR(255),
            web_url VARCHAR(512),
            publication_date DATETIME
        );
        """
        cursor.execute(create_table_query)

        # Insert articles into the table
        for article in articles:
            insert_query = """
            INSERT INTO guardian_articles (title, section_name, web_url, publication_date)
            VALUES (%s, %s, %s, %s);
            """
            cursor.execute(insert_query, (
                article.get('webTitle'),
                article.get('sectionName'),
                article.get('webUrl'),
                article.get('webPublicationDate')
            ))

        connection.commit()
        cursor.close()
        connection.close()

        return {
            'statusCode': 200,
            'body': json.dumps('Data fetched, stored in S3, and loaded into RDS successfully!')
        }

    except Exception as e:
        print(f"Error: {e}")
        return {
            'statusCode': 500,
            'body': json.dumps(f"Error: {str(e)}")
        }