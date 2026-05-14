import requests
import time
from datetime import datetime

# Config
TELEGRAM_TOKEN = "Your_Bot_Token_Here"
CHAT_ID = "1024188205"

# Paper trading state
balance_usd = 10000  # modal simulasi $10,000
balance_btc = 0
trade_history = []
prices = []

def send_telegram(pesan):
    try:
        url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
        params = {"chat_id": CHAT_ID, "text": pesan, "parse_mode": "Markdown"}
        requests.post(url, params=params, timeout=10)
    except:
        pass

def get_btc_price():
    try:
        url = "https://api.coingecko.com/api/v3/simple/price"
        params = {"ids": "bitcoin", "vs_currencies": "usd"}
        headers = {"User-Agent": "Mozilla/5.0"}
        r = requests.get(url, params=params, headers=headers, timeout=15)
        return float(r.json()['bitcoin']['usd'])
    except:
        return None

def calculate_sma(prices_list, period):
    """Simple Moving Average"""
    if len(prices_list) < period:
        return None
    return sum(prices_list[-period:]) / period

def calculate_rsi(prices_list, period=14):
    """Relative Strength Index"""
    if len(prices_list) < period + 1:
        return None
    
    gains = []
    losses = []
    
    for i in range(1, period + 1):
        diff = prices_list[-i] - prices_list[-i-1]
        if diff > 0:
            gains.append(diff)
            losses.append(0)
        else:
            gains.append(0)
            losses.append(abs(diff))
    
    avg_gain = sum(gains) / period
    avg_loss = sum(losses) / period
    
    if avg_loss == 0:
        return 100
    
    rs = avg_gain / avg_loss
    return 100 - (100 / (1 + rs))

def buy_btc(price, reason):
    global balance_usd, balance_btc
    
    if balance_usd < 100:
        return
    
    amount_usd = balance_usd * 0.5  # beli 50% dari balance
    amount_btc = amount_usd / price
    
    balance_usd -= amount_usd
    balance_btc += amount_btc
    
    trade = {
        "type": "BUY",
        "price": price,
        "btc": amount_btc,
        "usd": amount_usd,
        "time": datetime.now().strftime('%H:%M:%S'),
        "reason": reason
    }
    trade_history.append(trade)
    
    pesan = (
        f"🟢 *PAPER TRADE — BUY*\n\n"
        f"💰 Price  : `${price:,.2f}`\n"
        f"₿ BTC    : `{amount_btc:.6f}`\n"
        f"💵 USD    : `${amount_usd:,.2f}`\n"
        f"📊 Reason : {reason}\n"
        f"🕐 Time   : `{trade['time']}`\n\n"
        f"💼 Balance: `${balance_usd:,.2f}` + `{balance_btc:.6f} BTC`"
    )
    send_telegram(pesan)
    print(f"\n🟢 BUY at ${price:,.2f} — {reason}")

def sell_btc(price, reason):
    global balance_usd, balance_btc
    
    if balance_btc < 0.0001:
        return
    
    amount_btc = balance_btc * 0.5  # jual 50% BTC
    amount_usd = amount_btc * price
    
    balance_btc -= amount_btc
    balance_usd += amount_usd
    
    trade = {
        "type": "SELL",
        "price": price,
        "btc": amount_btc,
        "usd": amount_usd,
        "time": datetime.now().strftime('%H:%M:%S'),
        "reason": reason
    }
    trade_history.append(trade)
    
    total_value = balance_usd + (balance_btc * price)
    pnl = total_value - 10000
    
    pesan = (
        f"🔴 *PAPER TRADE — SELL*\n\n"
        f"💰 Price  : `${price:,.2f}`\n"
        f"₿ BTC    : `{amount_btc:.6f}`\n"
        f"💵 USD    : `${amount_usd:,.2f}`\n"
        f"📊 Reason : {reason}\n"
        f"🕐 Time   : `{trade['time']}`\n\n"
        f"💼 Balance: `${balance_usd:,.2f}` + `{balance_btc:.6f} BTC`\n"
        f"📈 P&L    : `${pnl:+,.2f}`"
    )
    send_telegram(pesan)
    print(f"\n🔴 SELL at ${price:,.2f} — {reason}")

def run_bot():
    global prices
    
    print("🤖 PAPER TRADING BOT STARTED")
    print(f"💵 Initial Balance: $10,000")
    print(f"📊 Strategy: SMA Crossover + RSI")
    print(f"⏱️ Interval: 30 seconds\n")
    
    send_telegram(
        "🤖 *PAPER TRADING BOT STARTED*\n\n"
        "💵 Balance: `$10,000`\n"
        "📊 Strategy: SMA + RSI\n"
        "🔄 Auto-trading simulation started!"
    )
    
    while True:
        price = get_btc_price()
        
        if not price:
            print("Gagal ambil harga, skip...")
            time.sleep(30)
            continue
        
        prices.append(price)
        
        # Hitung indicators
        sma_short = calculate_sma(prices, 5)   # SMA 5 periode
        sma_long = calculate_sma(prices, 10)   # SMA 10 periode
        rsi = calculate_rsi(prices, 10)
        
        total_value = balance_usd + (balance_btc * price)
        pnl = total_value - 10000
        
        print(f"\n{'='*45}")
        print(f"⏰ {datetime.now().strftime('%H:%M:%S')}")
        print(f"₿ BTC Price : ${price:,.2f}")
        print(f"📊 SMA5     : ${sma_short:,.2f}" if sma_short else "📊 SMA5     : Collecting...")
        print(f"📊 SMA10    : ${sma_long:,.2f}" if sma_long else "📊 SMA10    : Collecting...")
        print(f"📈 RSI      : {rsi:.1f}" if rsi else "📈 RSI      : Collecting...")
        print(f"💼 Balance  : ${balance_usd:,.2f} + {balance_btc:.6f} BTC")
        print(f"💰 Total    : ${total_value:,.2f} (P&L: ${pnl:+,.2f})")
        
        # Trading signals
        if sma_short and sma_long and rsi:
            # BUY signal: SMA short crosses above SMA long + RSI < 40
            if sma_short > sma_long and rsi < 40 and balance_usd > 100:
                buy_btc(price, f"SMA crossover + RSI={rsi:.1f}")
            
            # SELL signal: SMA short crosses below SMA long + RSI > 60
            elif sma_short < sma_long and rsi > 60 and balance_btc > 0.0001:
                sell_btc(price, f"SMA crossover + RSI={rsi:.1f}")
            
            else:
                print("⏳ HOLD — No signal")
        else:
            data_needed = max(0, 11 - len(prices))
            print(f"⏳ Collecting data... ({data_needed} more needed)")
        
        time.sleep(30)

# Run bot
run_bot()