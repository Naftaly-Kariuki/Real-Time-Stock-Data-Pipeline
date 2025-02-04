# Real-Time Stock Data Pipeline

## Overview
This project demonstrates how to build a **serverless data pipeline** to automate the retrieval, processing, and storage of real-time stock market data using **AWS cloud services**. I used the **Alpha Vantage API** to fetch intraday stock data and leveraged **AWS Lambda** for computation due to its scalability and seamless integration with AWS services. The data was then stored securely in **AWS S3**, allowing easy access through API calls from **Jupyter Notebooks** for analysis and visualization.

![Screenshot 2024-11-28 121407](https://github.com/user-attachments/assets/e7236437-beac-447d-84df-1c207fbdb51f)

## Technologies Used
- **Python** (for scripting and data processing)
- **Alpha Vantage API** (for stock data retrieval)
- **AWS Lambda** (serverless function execution)
- **AWS S3** (for secure and scalable data storage)
- **Boto3** (AWS SDK for Python)
- **Pandas** (for data manipulation)
- **Matplotlib & Seaborn** (for data visualization)

## Data Access and Security
To ensure secure and controlled access to cloud resources:
- **IAM roles and policies** were configured to grant AWS Lambda the necessary permissions to interact with Alpha Vantage and AWS S3.
- **Environment variables** were used to store sensitive credentials (such as API keys), reducing security risks.
- **AWS S3 access control** was implemented by blocking public access and enforcing fine-grained permissions via bucket policies.

![Screenshot 2024-11-28 120614](https://github.com/user-attachments/assets/406b02b7-e2bb-483b-be86-ecf613ccc144)

## Data Pipeline Workflow
### 1. Data Retrieval
- AWS Lambda invokes the **Alpha Vantage API** to fetch real-time intraday stock data.
- The data includes key attributes such as **open, high, low, close, and volume** for each minute interval.
- Error handling was implemented to address API rate limits and invalid responses, ensuring data reliability.

### 2. Data Storage
- The retrieved data is stored in an **AWS S3 bucket** in **JSON format**.
- Filenames are timestamped for traceability and systematic organization.
- AWS S3's **high durability** and **flexible storage capabilities** ensure long-term data availability.

 ![Screenshot 2024-11-28 122005](https://github.com/user-attachments/assets/40a4980d-55a4-4b7d-9cb6-71f2301896b3)

### 3. Data Analysis and Visualization
- A **local Jupyter Notebook** retrieves the stored data from AWS S3 using **Boto3**.
- The data is transformed into a **Pandas DataFrame** for further analysis.
- The dataset contains **21,068 rows and 5 columns**, representing stock data spanning 30 days in **one-minute intervals**.
- Stock price trends, **moving averages (SMA, EMA)**, and other insights are visualized using **Matplotlib and Seaborn**.

![Screenshot 2024-11-28 123107](https://github.com/user-attachments/assets/de981c79-d822-4d80-bde8-3d93374e7bf3)


![Screenshot 2024-11-28 125052](https://github.com/user-attachments/assets/a451ef7e-8155-46ab-921a-7eec276c133c)

## Key Insights
- The pipeline provides a **scalable and efficient** way to collect and analyze stock data in real-time.
- Financial institutions and startups can adopt this approach to **streamline stock data processing and analysis**.
- Controlled access via IAM roles ensures **data security** while allowing analysts to interact with the data effortlessly.

## Next Steps
To further enhance this project, I plan to:
- **Automate data retrieval** on a schedule using AWS EventBridge.
- **Implement database storage** (e.g., AWS DynamoDB or PostgreSQL) for structured querying.
- **Deploy dashboards** using **Streamlit or Dash** for real-time visualization.
