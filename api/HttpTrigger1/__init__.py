import logging
import json
import random


import azure.functions as func



def main(req: func.HttpRequest, doc: func.DocumentList) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')
    

    # Initialize an empty list to hold the names
    names_list = []

    # Loop through each resume and append the name to the list
    for resume in doc:
        names_list.append(resume['name'])

    # Select a random value from the list
    random_value = random.choice(names_list)
    
    # Set the headers to allow cross-origin requests
    headers = {
        'Access-Control-Allow-Origin': '*',  # replace * with your domain name
        'Access-Control-Allow-Methods': 'GET',
        'Access-Control-Allow-Headers': 'Content-Type',
    }


    # Return the random value as an HTTP response
    return func.HttpResponse(random_value, headers=headers, status_code=200)



