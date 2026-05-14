from web3 import Web3
from datetime import datetime
import requests

# Connect ke Ethereum
rpc = "https://ethereum-rpc.publicnode.com"
w3 = Web3(Web3.HTTPProvider(rpc))

print(f"Connected: {w3.is_connected()}")

# =====================
# ABI minimal untuk ERC-20 token
# =====================
ERC20_ABI = [
    {
        "constant": True,
        "inputs": [],
        "name": "name",
        "outputs": [{"name": "", "type": "string"}],
        "type": "function"
    },
    {
        "constant": True,
        "inputs": [],
        "name": "symbol",
        "outputs": [{"name": "", "type": "string"}],
        "type": "function"
    },
    {
        "constant": True,
        "inputs": [],
        "name": "decimals",
        "outputs": [{"name": "", "type": "uint8"}],
        "type": "function"
    },
    {
        "constant": True,
        "inputs": [],
        "name": "totalSupply",
        "outputs": [{"name": "", "type": "uint256"}],
        "type": "function"
    },
    {
        "constant": True,
        "inputs": [{"name": "_owner", "type": "address"}],
        "name": "balanceOf",
        "outputs": [{"name": "balance", "type": "uint256"}],
        "type": "function"
    }
]

def read_token_contract(contract_address, wallet=None):
    """Baca data dari ERC-20 smart contract"""
    
    # Checksum address
    address = Web3.to_checksum_address(contract_address)
    
    # Load contract
    contract = w3.eth.contract(address=address, abi=ERC20_ABI)
    
    print(f"\n=== SMART CONTRACT READER ===")
    print(f"Update  : {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"Address : {address}\n")
    
    # Baca data dari contract
    name = contract.functions.name().call()
    symbol = contract.functions.symbol().call()
    decimals = contract.functions.decimals().call()
    total_supply = contract.functions.totalSupply().call()
    
    # Format total supply
    total_supply_formatted = total_supply / (10 ** decimals)
    
    print(f"Name         : {name}")
    print(f"Symbol       : {symbol}")
    print(f"Decimals     : {decimals}")
    print(f"Total Supply : {total_supply_formatted:,.2f} {symbol}")
    
    # Cek balance wallet kalau ada
    if wallet:
        wallet_address = Web3.to_checksum_address(wallet)
        balance = contract.functions.balanceOf(wallet_address).call()
        balance_formatted = balance / (10 ** decimals)
        print(f"Wallet Balance: {balance_formatted:,.4f} {symbol}")
    
    print("-" * 45)
    return {
        "name": name,
        "symbol": symbol,
        "decimals": decimals,
        "total_supply": total_supply_formatted
    }

def get_contract_bytecode(contract_address):
    """Cek apakah address adalah smart contract"""
    address = Web3.to_checksum_address(contract_address)
    bytecode = w3.eth.get_code(address)
    
    if bytecode and bytecode != b'':
        print(f"\n✅ {address} adalah Smart Contract")
        print(f"Bytecode size: {len(bytecode)} bytes")
    else:
        print(f"\n❌ {address} bukan Smart Contract (EOA wallet)")

# =====================
# Test dengan token populer
# =====================

# USDT Contract
print("\n📋 Reading USDT Contract...")
read_token_contract(
    "0xdAC17F958D2ee523a2206206994597C13D831ec7",
    wallet="0xd8dA6BF26964aF9D7eEd9e03E53415D37aA96045"  # Vitalik wallet
)

# USDC Contract  
print("\n📋 Reading USDC Contract...")
read_token_contract(
    "0xA0b86991c6218b36c1d19D4a2e9Eb0cE3606eB48"
)

# SHIB Contract
print("\n📋 Reading SHIB Contract...")
read_token_contract(
    "0x95aD61b0a150d79219dCF64E1E6Cc01f0B64C4cE"
)

# Cek apakah address adalah contract
print("\n🔍 Contract Verification:")
get_contract_bytecode("0xdAC17F958D2ee523a2206206994597C13D831ec7")  # USDT
get_contract_bytecode("0xd8dA6BF26964aF9D7eEd9e03E53415D37aA96045")  # Vitalik wallet