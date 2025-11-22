import requests, time

def whale_tracker():
    print("Solana whale transaction tracker (> $500k)")
    seen = set()
    while True:
        r = requests.get("https://api.solscan.io/transfer?from=0&to=0&limit=20")
        for tx in r.json().get("data", []):
            txid = tx["txHash"]
            if txid in seen: continue
            seen.add(txid)
            amount = tx["amount"] / 1e9
            value = amount * float(tx.get("price", 0))
            if value > 500_000:
                print(f"WHALE MOVE ${value:,.0f}\n"
                      f"Token: {tx.get('symbol','SOL')}\n"
                      f"Amount: {amount:,.2f}\n"
                      f"From: {tx['source'][:8]}...\n"
                      f"To: {tx['destination'][:8]}...\n"
                      f"https://solscan.io/tx/{txid}\n"
                      f"{'-'*50}")
        time.sleep(3)

if __name__ == "__main__":
    whale_tracker()
