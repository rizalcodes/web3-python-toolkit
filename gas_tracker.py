import requests
from datetime import datetime
import time

ETHERSCAN_API = "Your_Api_Key_here"

def get_gas_price():
    url = "https://api.etherscan.io/v2/api"
    params = {
        "chainid": 1,
        "module": "gastracker",
        "action": "gasoracle",
        "apikey": ETHERSCAN_API
    }

    response = requests.get(url, params=params)
    data = response.json()

    if data['status'] == '1':
        result = data['result']
        print(f"\n=== GAS FEE TRACKER ===")
        print(f"Update : {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        print(f"🟢 Slow   : {result['SafeGasPrice']} Gwei")
        print(f"🟡 Normal : {result['ProposeGasPrice']} Gwei")
        print(f"🔴 Fast   : {result['FastGasPrice']} Gwei")
        print(f"\nBase Fee  : {result['suggestBaseFee']} Gwei")
        print("-" * 30)
    else:
        print(f"Error: {data['message']}")

# Auto refresh setiap 30 detik
while True:
    get_gas_price()
    print("Refresh dalam 30 detik...")
    time.sleep(30)
