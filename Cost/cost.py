from datetime import datetime, timedelta
import boto3

today_datetime = datetime.now()
starting_date = (today_datetime - timedelta(days=90)).strftime('%Y-%m-%d')

ending_date = (today_datetime).strftime('%Y-%m-%d')

print(f"Duration from {starting_date} - {ending_date}")

ce_client = boto3.client('ce')

analyze = ce_client.get_cost_and_usage(
    TimePeriod = {
        'Start': 'starting_date',
        'End' : 'ending_date'
    }, 
    Granularity = "DAILY", 
    Metrics = [
        'UnblendedCost'
    ]
)

