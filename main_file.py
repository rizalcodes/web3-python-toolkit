from web3 import Web3

rpc = "https://ethereum-rpc.publicnode.com"

w3 = Web3(Web3.HTTPProvider(rpc))

print("Connected:", w3.is_connected())
# Cek block terbaru
block = w3.eth.block_number
print(f"Latest Block: {block}")

# Cek ETH balance sebuah wallet
wallet = "0xde0B295669a9FD93d5F28D9Ec85E40f4cb697BAe"  # wallet Ethereum Foundation
balance_wei = w3.eth.get_balance(wallet)
balance_eth = w3.from_wei(balance_wei, 'ether')
print(f"Wallet Balance: {balance_eth} ETH")