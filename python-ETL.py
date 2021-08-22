#Display output

import pandas as pd pd.read_json('test.json')

pd.merge(left, right, how='inner', on=None, left_on=None, right_on=None, 
left_index=False, right_index=False, sort=True)

from xplenty import XplentyClient account_id ="MyAccountID" api_key = 
"V4eyfgNqYcSasXGhzNxS" client = XplentyClient(account_id,api_key)

cluster_id = 83 package_id = 782 variables = {} 
variables['OUTPUTPATH']="test/job_vars.csv" variables['Date']="09-10-2020"
     job = client.add_job(cluster_id, package_id, variables)
     
#For further reference
#https://www.xplenty.com/blog/building-an-etl-pipeline-in-python/
