from web3 import Web3
from datetime import datetime
import requests

rpc = "https://ethereum-rpc.publicnode.com"
w3 = Web3(Web3.HTTPProvider(rpc))

def get_transactions(address, limit=5):
    print(f"\n=== TRANSACTION TRACKER ===")
    print(f"Update  : {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"Wallet  : {address[:10]}...{address[-6:]}\n")

    # Ambil block terbaru
    latest_block = w3.eth.block_number
    print(f"Scanning dari block {latest_block - 100} sampai {latest_block}...\n")

    count = 0
    for block_num in range(latest_block, latest_block - 100, -1):
        if count >= limit:
            break

        block = w3.eth.get_block(block_num, full_transactions=True)

        for tx in block.transactions:
            if count >= limit:
                break

            # Cek apakah wallet terlibat
            tx_from = tx['from'].lower()
            tx_to = tx['to'].lower() if tx['to'] else None
            addr = address.lower()

            if tx_from == addr or tx_to == addr:
                nilai_eth = w3.from_wei(tx['value'], 'ether')
                arah = "SEND →" if tx_from == addr else "← RECEIVE"

                print(f"TX Hash  : {tx['hash'].hex()[:20]}...")
                print(f"Arah     : {arah}")
                print(f"Nilai    : {nilai_eth:.6f} ETH")
                print(f"Block    : {block_num}")
                print("-" * 45)
                count += 1

    if count == 0:
        print("Tidak ada transaksi dalam 100 block terakhir")

# Cek wallet Ethereum Foundation
# Ganti wallet ke Vitalik - lebih aktif
get_transactions("0xd8dA6BF26964aF9D7eEd9e03E53415D37aA96045", limit=5)