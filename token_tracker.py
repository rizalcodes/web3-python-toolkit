import requests
from datetime import datetime

ETHERSCAN_API = "Your_Api_Key_Here"

# Contract address token populer
TOKENS = {
    "USDT": "0xdAC17F958D2ee523a2206206994597C13D831ec7",
    "USDC": "0xA0b86991c6218b36c1d19D4a2e9Eb0cE3606eB48",
    "SHIB": "0x95aD61b0a150d79219dCF64E1E6Cc01f0B64C4cE"
}

def get_token_balance(wallet, token_name, token_contract):
    url = "https://api.etherscan.io/v2/api"
    params = {
        "chainid": 1,
        "module": "account",
        "action": "tokenbalance",
        "contractaddress": token_contract,
        "address": wallet,
        "tag": "latest",
        "apikey": ETHERSCAN_API
    }

    response = requests.get(url, params=params)
    data = response.json()

    if data['status'] == '1':
        # USDT & USDC punya 6 desimal, SHIB 18 desimal
        decimals = 6 if token_name in ["USDT", "USDC"] else 18
        balance = int(data['result']) / (10 ** decimals)
        return balance
    return 0

def cek_semua_token(wallet):
    print(f"\n=== TOKEN TRACKER ===")
    print(f"Update : {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"Wallet : {wallet[:10]}...{wallet[-6:]}\n")

    for token_name, token_contract in TOKENS.items():
        balance = get_token_balance(wallet, token_name, token_contract)
        print(f"{token_name:<6}: {balance:,.2f}")

    print("-" * 30)

# Cek wallet Vitalik
cek_semua_token("0xd8dA6BF26964aF9D7eEd9e03E53415D37aA96045")
