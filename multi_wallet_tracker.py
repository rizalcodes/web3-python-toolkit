from web3 import Web3
from datetime import datetime
import requests
import time

rpc = "https://ethereum-rpc.publicnode.com"
w3 = Web3(Web3.HTTPProvider(rpc))

def get_eth_price():
    try:
        # Pakai Binance API - lebih reliable
        url = "https://api.binance.com/api/v3/ticker/price?symbol=ETHUSDT"
        response = requests.get(url, timeout=10)
        return float(response.json()['price'])
    except:
        print("Gagal ambil harga, pakai harga terakhir...")
        return 2316.10

def cek_wallet(address, eth_price):
    balance_wei = w3.eth.get_balance(address)
    balance_eth = w3.from_wei(balance_wei, 'ether')
    nilai_usd = float(balance_eth) * eth_price
    print(f"Address : {address[:10]}...{address[-6:]}")
    print(f"Balance : {balance_eth:.4f} ETH")
    print(f"Value   : ${nilai_usd:,.2f}")
    print("-" * 45)

wallets = [
    "0xde0B295669a9FD93d5F28D9Ec85E40f4cb697BAe",
    "0xBE0eB53F46cd790Cd13851d5EFf43D12404d33E8",
]

while True:
    eth_price = get_eth_price()
    print(f"\n=== MULTI WALLET TRACKER ===")
    print(f"ETH Price : ${eth_price:,.2f}")
    print(f"Update    : {datetime.now().strftime('%H:%M:%S')}\n")

    for wallet in wallets:
        cek_wallet(wallet, eth_price)

    print("\nRefresh dalam 60 detik...")
    time.sleep(60)