from binance.client import Client
import time

api_key = '...'
api_secret = '...'

client = Client(api_key, api_secret)

def find_best_trading_pair():
    ticker_price = client.get_symbol_ticker(symbol="BTCUSDT")
    bitcoin_price = float(ticker_price['price'])
    
    ticker_price = client.get_symbol_ticker(symbol="ETHUSDT")
    ethereum_price = float(ticker_price['price'])
    
    ticker_price = client.get_symbol_ticker(symbol="BTCETH")
    btc_eth_price = float(ticker_price['price'])
    
    btc_eth_arbitrage = bitcoin_price - (btc_eth_price * ethereum_price)

    if btc_eth_arbitrage > 0:
        return 'BTCUSDT'
    else:
        return 'BTCETH'

def main():
    while True:
        try:
            trading_pair = find_best_trading_pair()
            print(f"Лучшая торговая пара сейчас: {trading_pair}")
        except Exception as e:
            print(f"Произошла ошибка: {e}")
        time.sleep(60)

if __name__ == '__main__':
    main()
