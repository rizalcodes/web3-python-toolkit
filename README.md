# 🔗 Web3 Python Toolkit

A comprehensive collection of Python tools for interacting with the Ethereum blockchain in real-time.

## 🛠️ Tools Included

| File | Description |
|------|-------------|
| `main_file.py` | Connect to Ethereum & check wallet balance |
| `wallet_tracker.py` | Track ETH balance + USD value in realtime |
| `multi_wallet_tracker.py` | Monitor multiple wallets simultaneously |
| `etherscan_tracker.py` | Fetch transaction history via Etherscan API v2 |
| `token_tracker.py` | Check ERC-20 token balances (USDT, USDC, SHIB) |
| `tx_tracker.py` | On-chain transaction scanner |
| `gas_tracker.py` | Realtime Ethereum gas fee monitor (Slow/Normal/Fast) |
| `nft_tracker.py` | NFT collection tracker + floor price via OpenSea API |
| `whale_alert.py` | Telegram bot alert for large ETH transactions (Whale Alert) |
| `defi_tracker.py` | DeFi protocol TVL tracker via DeFiLlama API |
| `price_alert.py` | Crypto price alert bot with Telegram notifications |

## ⚙️ Tech Stack

- Python 3.x
- web3.py
- Etherscan API v2
- OpenSea API v2
- DeFiLlama API
- CoinGecko API
- Telegram Bot API
- requests, datetime, time

## 🚀 Features

- ✅ Realtime ETH & ERC-20 token balance tracking
- ✅ Multi-wallet monitoring with USD value
- ✅ Transaction history lookup via Etherscan
- ✅ Live gas fee tracker (Slow / Normal / Fast)
- ✅ NFT collection info & floor price monitor
- ✅ Whale alert — Telegram notif for large transactions
- ✅ DeFi protocol TVL tracker (Top 10 protocols)
- ✅ Price alert bot — notif when price above/below target
- ✅ Auto-refresh every 30-60 seconds

## 📦 Installation

```bash
pip install web3 requests python-dotenv
```

## 🔑 Setup

Create your API keys and add them to each file:

```python
ETHERSCAN_API = "your_etherscan_api_key"
OPENSEA_API = "your_opensea_api_key"
TELEGRAM_TOKEN = "your_telegram_bot_token"
CHAT_ID = "your_telegram_chat_id"
```

## 📊 Example Output

=== MULTI WALLET TRACKER ===
ETH Price : $2,316.10
Update    : 09:58:31
Address : 0xde0B2956...697BAe
Balance : 10774.4523 ETH
Value   : $24,954,708.98


## 👨‍💻 Author

**Rizal** — Python & Web3 Developer
- GitHub: [@rizalcodes](https://github.com/rizalcodes)
- Fiverr: [@izall7](https://fiverr.com/izall7)
- LinkedIn: [@Rizal](https://www.linkedin.com/in/rizal-ical-b01789407/)
- X/Twitter: [@ClipXDaily](https://x.com/ClipXDaily)
