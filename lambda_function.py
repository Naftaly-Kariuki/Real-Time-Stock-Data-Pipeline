import os
import json
import boto3
from datetime import datetime
from alpha_vantage.timeseries import TimeSeries

def lambda_handler(event, context):
    # Retrieve the API key from environment variables
    api_key = os.environ.get('V3JJB2KX50VZMQDN')

    if not api_key:
        return {
            'status': 'Error',
            'message': 'API key missing.'
        }

    # Initialize Alpha Vantage API
    ts = TimeSeries(key=api_key, output_format='json')

    # List of stock tickers
    tickers = ["AAPL", "NVDA", "005930.KS", "MSFT", "AMZN"]

    # Initialize S3 client
    s3 = boto3.client('s3')
    bucket_name = "financial-stock-data"

    # Iterate over the stock tickers
    for ticker in tickers:
        try:
            # Fetch stock data
            data, meta_data = ts.get_intraday(symbol=ticker, interval="1min", outputsize="full")
            
            # Prepare data for S3
            data_json = json.dumps(data)

            # Generate a unique filename
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            file_name = f"{ticker}_stock_{timestamp}.json"

            # Upload to S3
            s3.put_object(
                Bucket=bucket_name,
                Key=file_name,
                Body=data_json
            )
            print(f"Uploaded data for {ticker} as {file_name}")
        except Exception as e:
            print(f"Failed to fetch/upload data for {ticker}: {e}")

    return {"status": "Success", "message": "Stock data uploaded for all tickers"}
