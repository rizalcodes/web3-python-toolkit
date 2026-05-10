import requests
import time
from datetime import datetime

TELEGRAM_TOKEN = "isi_token_bot_kamu"
CHAT_ID = "1024188205"

ALERTS = {
    "bitcoin": {"above": 90000, "below": 75000},
    "ethereum": {"above": 2500, "below": 2000},
    "solana": {"above": 100, "below": 80},
}

def send_telegram(pesan):
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    params = {"chat_id": CHAT_ID, "text": pesan, "parse_mode": "Markdown"}
    requests.post(url, params=params)

def get_prices():
    try:
        url = "https://api.coingecko.com/api/v3/simple/price"
        params = {"ids": "bitcoin,ethereum,solana", "vs_currencies": "usd"}
        headers = {"User-Agent": "Mozilla/5.0"}
        r = requests.get(url, params=params, headers=headers, timeout=15)
        data = r.json()
        return {
            "bitcoin": data['bitcoin']['usd'],
            "ethereum": data['ethereum']['usd'],
            "solana": data['solana']['usd']
        }
    except:
        print("Gagal ambil harga, skip...")
        return {}

def check_alerts():
    print(f"\n=== PRICE ALERT BOT ===")
    print(f"Update: {datetime.now().strftime('%H:%M:%S')}\n")

    prices = get_prices()

    if not prices:
        return

    for coin, price in prices.items():
        alert = ALERTS.get(coin, {})
        print(f"{coin.upper():<12}: ${price:,.2f}")

        if alert.get('above') and price >= alert['above']:
            pesan = (
                f"🚀 *PRICE ALERT — {coin.upper()}*\n\n"
                f"💰 Price  : `${price:,.2f}`\n"
                f"📈 Status : *ABOVE* ${alert['above']:,}\n"
                f"🕐 Time   : `{datetime.now().strftime('%H:%M:%S')}`"
            )
            send_telegram(pesan)
            print(f"  ⚠️ ALERT SENT — above ${alert['above']:,}")

        elif alert.get('below') and price <= alert['below']:
            pesan = (
                f"📉 *PRICE ALERT — {coin.upper()}*\n\n"
                f"💰 Price  : `${price:,.2f}`\n"
                f"📉 Status : *BELOW* ${alert['below']:,}\n"
                f"🕐 Time   : `{datetime.now().strftime('%H:%M:%S')}`"
            )
            send_telegram(pesan)
            print(f"  ⚠️ ALERT SENT — below ${alert['below']:,}")

    print(f"\nRefresh dalam 60 detik...")

while True:
    check_alerts()
    time.sleep(60)