import requests
from datetime import datetime

OPENSEA_API = "Your_Api_Key_Here"

def get_nft_collection(slug):
    """Ambil info & floor price sebuah NFT collection"""
    url = f"https://api.opensea.io/api/v2/collections/{slug}"
    headers = {
        "accept": "application/json",
        "x-api-key": OPENSEA_API
    }

    response = requests.get(url, headers=headers)
    data = response.json()

    print(f"\n=== NFT COLLECTION INFO ===")
    print(f"Update : {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
    print(f"Name        : {data.get('name', 'N/A')}")
    print(f"Description : {data.get('description', 'N/A')[:80]}...")
    print(f"Category    : {data.get('category', 'N/A')}")
    print(f"Total Supply: {data.get('total_supply', 'N/A')}")
    print(f"Contracts   : {data.get('contracts', 'N/A')}")
    print("-" * 45)

def get_floor_price(slug):
    """Ambil floor price collection"""
    url = f"https://api.opensea.io/api/v2/listings/collection/{slug}/best"
    headers = {
        "accept": "application/json",
        "x-api-key": OPENSEA_API
    }

    response = requests.get(url, headers=headers)
    data = response.json()

    listings = data.get('listings', [])
    if listings:
        price_wei = int(listings[0]['price']['current']['value'])
        price_eth = price_wei / 10**18
        print(f"Floor Price : {price_eth:.4f} ETH")
    else:
        print("Floor Price : No listings found")

def get_wallet_nfts(wallet_address):
    """Ambil NFT yang dimiliki sebuah wallet"""
    url = f"https://api.opensea.io/api/v2/chain/ethereum/account/{wallet_address}/nfts"
    headers = {
        "accept": "application/json",
        "x-api-key": OPENSEA_API
    }

    response = requests.get(url, headers=headers)
    data = response.json()

    print(f"\n=== WALLET NFT TRACKER ===")
    print(f"Wallet : {wallet_address[:10]}...{wallet_address[-6:]}\n")

    nfts = data.get('nfts', [])
    if nfts:
        print(f"Ditemukan {len(nfts)} NFT:\n")
        for nft in nfts[:5]:  # tampilkan 5 pertama
            print(f"Name       : {nft.get('name', 'Unnamed')}")
            print(f"Collection : {nft.get('collection', 'N/A')}")
            print(f"Token ID   : {nft.get('identifier', 'N/A')}")
            print("-" * 45)
    else:
        print("Tidak ada NFT di wallet ini")

# Test dengan Bored Ape Yacht Club
print("Fetching BAYC collection...")
get_nft_collection("boredapeyachtclub")
get_floor_price("boredapeyachtclub")

# Cek wallet Vitalik punya NFT apa
get_wallet_nfts("0xd8dA6BF26964aF9D7eEd9e03E53415D37aA96045")
