#!/usr/bin/python3
import requests
import csv
import os

# Configs #####################################################################
# NOTE: apikey must have ELECTRONIC read/write permissions.
collection_id = 'COLLECTION_ID_HERE'
service_id = 'SERVICE_ID_HERE'
spreadsheet_directory = 'c:\\users\\user\Downloads\\'
apikey = os.environ['ALMA_APIKEY']

# Open CSV spreadsheet and process
with open(f'{spreadsheet_directory}\\Kanopy video expiration report.csv', encoding='utf-8') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    next(csv_reader) # skip header
    for row in csv_reader:
        # parse
        portfolio_id = row[0]
        mms_id = row[1]
        title = row[2]
        expiration_date = row[3]
        
        # delete portfolio
        # NOTE: bib parameter is either "delete" or "retain".
        r = requests.delete(f'https://api-na.hosted.exlibrisgroup.com/almaws/v1/electronic/e-collections/{collection_id}/e-services/{service_id}/portfolios/{portfolio_id}?bib=delete&apikey={apikey}')
        
        # check for errors
        # API returns 204 NO CONTENT if successful
        if r.status_code != 204:
            status = f"ERRORS FOUND!: {r.text}"
        else:
            status = "SUCCESS!"
            
        # output
        print(f"MMS_ID: {mms_id}", flush=True)
        print(f"PORTFOLIO_ID: {portfolio_id}", flush=True)
        print(f"TITLE: {title}", flush=True)
        print(f"STATUS: {status}", flush=True)
        print("--------------------------------------------------------------")
        
print("Finished.")