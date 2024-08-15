#import os
#from dotenv import load_dotenv
#import requests

#load_dotenv()
#ACCESS_TOKEN = os.getenv("ACCESS_TOKEN")

# import requests

#API_URL = "https://api-inference.huggingface.co/models/meta-llama/Meta-Llama-3.1-8B"
#headers = {"Authorization": f"Bearer {ACCESS_TOKEN}"}

#def query(payload):
#	response = requests.post(API_URL, headers=headers, json=payload)
#	return response.json()
	
#output = query({
#	"inputs": "Can you please let us know more details about your ",
#})

#print(output)
