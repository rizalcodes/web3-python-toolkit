import requests
import time
from datetime import datetime

# Config — isi dengan data kamu
ETHERSCAN_API = "AW8AJ3TQV79VTM1WM9KY7W9H5ICZZ1WUYT"
TELEGRAM_TOKEN = "8660442841:AAGIG5Rf89llvH0W985Zj2e4E-AbfyonJ5o"
CHAT_ID = "1024188205"
MIN_ETH = 100  # alert kalau transaksi > 100 ETH

def send_telegram(pesan):
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    params = {
        "chat_id": CHAT_ID,
        "text": pesan,
        "parse_mode": "Markdown"
    }
    requests.post(url, params=params)

def get_latest_txs():
    url = "https://api.etherscan.io/v2/api"
    params = {
        "chainid": 1,
        "module": "account",
        "action": "txlist",
        "address": "0x00000000219ab540356cBB839Cbe05303d7705Fa",  # ETH2 deposit contract
        "startblock": 0,
        "endblock": 99999999,
        "page": 1,
        "offset": 20,
        "sort": "desc",
        "apikey": ETHERSCAN_API
    }
    response = requests.get(url, params=params)
    return response.json().get('result', [])

def check_whales():
    print(f"\n🐋 WHALE ALERT BOT RUNNING")
    print(f"Monitoring transaksi > {MIN_ETH} ETH")
    print(f"Update: {datetime.now().strftime('%H:%M:%S')}\n")

    txs = get_latest_txs()
    whale_count = 0

    for tx in txs:
        nilai_eth = int(tx['value']) / 10**18

        if nilai_eth >= MIN_ETH:
            whale_count += 1
            arah = "📤 SEND" if tx['from'] else "📥 RECEIVE"
            timestamp = datetime.fromtimestamp(int(tx['timeStamp']))

            pesan = (
                f"🐋 *WHALE ALERT!*\n\n"
                f"💰 Amount: `{nilai_eth:.2f} ETH`\n"
                f"📤 From: `{tx['from'][:10]}...`\n"
                f"📥 To: `{tx['to'][:10]}...`\n"
                f"🕐 Time: `{timestamp}`\n"
                f"🔗 TX: `{tx['hash'][:20]}...`"
            )

            print(f"🐋 WHALE FOUND: {nilai_eth:.2f} ETH")
            send_telegram(pesan)

    if whale_count == 0:
        print("Tidak ada whale transaction ditemukan")

    print(f"\nRefresh dalam 60 detik...")

# Run setiap 60 detik
while True:
    check_whales()
    time.sleep(60)