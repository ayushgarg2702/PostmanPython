import json
import requests
from requests.auth import HTTPBasicAuth

url = "https://url/"

headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json'
}

def hit_api(): 
    # Get 
    try:
        response = requests.request('GET',url, auth=HTTPBasicAuth('admin', 'Password'), headers=headers)
        data = response.json()
        data = data['result']                    
    except Exception as e:
        print("[ERROR]\t:\t"+ "\t:\t" +str(e))

    # Post
    try:
        payload_str={"Name":"AG"}
        response = requests.request('POST',url, auth=HTTPBasicAuth('admin', 'Password'), headers=headers, data=payload_str)
        data = response.json()
        data = data['result']                    
    except Exception as e:
        print("[ERROR]\t:\t"+ "\t:\t" +str(e))

    # Put
    try:
        payload_str={"Name":"A.G."}
        response = requests.request('PT',url, auth=HTTPBasicAuth('admin', 'Password'), headers=headers, data=payload_str)
        data = response.json()
        data = data['result']                    
    except Exception as e:
        print("[ERROR]\t:\t"+ "\t:\t" +str(e))


if __name__ == "__main__":
    hit_api()
