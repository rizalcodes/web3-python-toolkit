from web3 import Web3
from datetime import datetime

rpc = "https://ethereum-rpc.publicnode.com"
w3 = Web3(Web3.HTTPProvider(rpc))

def cek_wallet(address):
    print(f"\n=== WALLET TRACKER ===")
    print(f"Update: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"Address: {address}\n")

    # Cek balance
    balance_wei = w3.eth.get_balance(address)
    balance_eth = w3.from_wei(balance_wei, 'ether')

    # Ambil harga ETH dari CoinGecko
    import requests
    url = "https://api.coingecko.com/api/v3/simple/price"
    params = {"ids": "ethereum", "vs_currencies": "usd"}
    response = requests.get(url, params=params)
    eth_price = response.json()['ethereum']['usd']

    # Hitung nilai USD
    nilai_usd = float(balance_eth) * eth_price

    print(f"ETH Balance : {balance_eth:.4f} ETH")
    print(f"ETH Price   : ${eth_price:,.2f}")
    print(f"Total Value : ${nilai_usd:,.2f}")
    print(f"Block       : {w3.eth.block_number}")

# Cek wallet Ethereum Foundation
cek_wallet("0xde0B295669a9FD93d5F28D9Ec85E40f4cb697BAe")