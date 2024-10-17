import pandas as pd
import requests as rq

def get_eod_data(symbols, access_key):
    endpoint = f"http://api.marketstack.com/v1/eod/latest"
    query = {
        "access_key": access_key,
        "symbols": symbols
    }
    
    response = rq.get(endpoint, params=query)
    if response.status_code != 200:
        raise Exception(f"API request failed with status code {response.status_code}")
    
    data = response.json()
    if "data" not in data:
        raise Exception("Invalid response from API")
    
    return data["data"]

def generate_eod_data_table(company_data):
    open_close_data = {
        "Symbol": [],
        "Open": [],
        "Close": [],
        "Change": []
    }

    for company in company_data:
        symbol = company["symbol"]
        open_price = company["open"]
        close_price = company["close"]
        percent_change = round((((close_price / open_price) - 1) * 100), 2)
        
        open_close_data["Symbol"].append(symbol)
        open_close_data["Open"].append(open_price)
        open_close_data["Close"].append(close_price)
        open_close_data["Change"].append(percent_change)

    return open_close_data
