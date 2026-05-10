import requests
from datetime import datetime

def get_defi_protocols():
    """Ambil data top DeFi protocols dari DeFiLlama API"""
    url = "https://api.llama.fi/protocols"
    response = requests.get(url)
    protocols = response.json()

    print(f"\n=== DeFi PROTOCOL TRACKER ===")
    print(f"Update: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
    print(f"{'Rank':<5} {'Name':<20} {'TVL':>15} {'Chain':<15}")
    print("-" * 60)

    # Tampilkan top 10
    for i, p in enumerate(protocols[:10], 1):
        tvl = p.get('tvl', 0)
        name = p.get('name', 'N/A')[:18]
        chain = p.get('chain', 'Multi')[:13]

        # Format TVL
        if tvl >= 1_000_000_000:
            tvl_str = f"${tvl/1_000_000_000:.2f}B"
        else:
            tvl_str = f"${tvl/1_000_000:.2f}M"

        print(f"{i:<5} {name:<20} {tvl_str:>15} {chain:<15}")

def get_protocol_detail(protocol_slug):
    """Ambil detail TVL sebuah protocol"""
    url = f"https://api.llama.fi/protocol/{protocol_slug}"
    response = requests.get(url)
    data = response.json()

    print(f"\n=== PROTOCOL DETAIL ===")
    print(f"Name     : {data.get('name', 'N/A')}")
    print(f"Category : {data.get('category', 'N/A')}")
    print(f"Chain    : {data.get('chain', 'N/A')}")

    tvl = data.get('tvl', 0)
    if isinstance(tvl, list) and tvl:
        latest_tvl = tvl[-1].get('totalLiquidityUSD', 0)
        if latest_tvl >= 1_000_000_000:
            print(f"TVL      : ${latest_tvl/1_000_000_000:.2f}B")
        else:
            print(f"TVL      : ${latest_tvl/1_000_000:.2f}M")

    print(f"Desc     : {str(data.get('description', 'N/A'))[:80]}...")
    print("-" * 45)

def get_defi_summary():
    """Ambil total TVL semua DeFi"""
    url = "https://api.llama.fi/v2/historicalChainTvl"
    response = requests.get(url)
    data = response.json()

    if data:
        latest = data[-1]
        tvl = latest.get('tvl', 0)
        date = datetime.fromtimestamp(latest.get('date', 0))
        print(f"\n=== TOTAL DeFi TVL ===")
        print(f"Date : {date.strftime('%Y-%m-%d')}")
        print(f"TVL  : ${tvl/1_000_000_000:.2f}B")
        print("-" * 45)

# Run semua
get_defi_summary()
get_defi_protocols()
get_protocol_detail("aave")  # cek detail Aave