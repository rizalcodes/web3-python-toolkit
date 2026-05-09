import requests
from datetime import datetime

ETHERSCAN_API = "AW8AJ3TQV79VTM1WM9KY7W9H5ICZZ1WUYT"

def get_transactions(address, limit=5):
    print(f"\n=== TRANSACTION TRACKER ===")
    print(f"Update : {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"Wallet : {address[:10]}...{address[-6:]}\n")

    url = "https://api.etherscan.io/api"
    params = {
        "module": "account",
        "action": "txlist",
        "address": address,
        "startblock": 0,
        "endblock": 99999999,
        "page": 1,
        "offset": limit,
        "sort": "desc",
        "apikey": ETHERSCAN_API
    }

    response = requests.get(url, params=params)
    data = response.json()

    if data['status'] == '1':
        txs = data['result']
        print(f"Ditemukan {len(txs)} transaksi terbaru:\n")

        for tx in txs:
            nilai_eth = int(tx['value']) / 10**18
            arah = "SEND →" if tx['from'].lower() == address.lower() else "← RECEIVE"
            timestamp = datetime.fromtimestamp(int(tx['timeStamp']))

            print(f"TX Hash : {tx['hash'][:20]}...")
            print(f"Arah    : {arah}")
            print(f"Nilai   : {nilai_eth:.6f} ETH")
            print(f"Waktu   : {timestamp}")
            print("-" * 45)
    else:
        print("Tidak ada data atau API error")

# Wallet Vitalik
get_transactions("0xd8dA6BF26964aF9D7eEd9e03E53415D37aA96045", limit=5)