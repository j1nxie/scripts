from dotenv import load_dotenv
import requests
import json
import sys
import os

load_dotenv()

class Result():
    def __init__(self, jsonrpc, result, id):
        self.jsonrpc = jsonrpc
        self.result = result
        self.id = id

def main():
    if len(sys.argv) < 4:
        print("Usage: python random.py <COUNT OF NUMBERS> <MIN VALUE> <MAX VALUE>")
        return

    payload = json.dumps({
        "jsonrpc": "2.0",
        "method": "generateIntegers",
        "params": {
            "apiKey": os.getenv("APIKEY"),
            "n": int(sys.argv[1]),
            "min": int(sys.argv[2]),
            "max": int(sys.argv[3])
        },
        "id": 727
    })

    headers = {
        "Content-Type": "application/json"
    }

    r = requests.post("https://api.random.org/json-rpc/4/invoke", headers=headers, data=payload)
    print(r.json()["result"]["random"]["data"])
    
if __name__ == "__main__":
    main()
