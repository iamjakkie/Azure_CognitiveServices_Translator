import os, requests, uuid, json 

_SUBSCRIPTION_KEY = "e763db208b394e67abcf391be6be562c"
_LOCATION = "westeurope"

def get_translation(text_input, language_output):
    base_url = 'https://api.cognitive.microsofttranslator.com'
    path = '/translate?api-version=3.0'
    params = '&to=' + language_output
    constructed_url = base_url + path + params

    headers = {
        'Ocp-Apim-Subscription-Key': _SUBSCRIPTION_KEY,
        'Ocp-Apim-Subscription-Region': _LOCATION,
        'Content-type': 'application/json',
        'X-ClientTraceId': str(uuid.uuid4())
    }

    body = [{
        'text' : text_input
    }]
    response = requests.post(constructed_url, headers=headers, json=body)
    return response.json()