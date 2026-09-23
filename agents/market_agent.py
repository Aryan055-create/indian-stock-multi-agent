# Market Data Agent
# Connects the system to Groww API

import os
from dotenv import load_dotenv
from growwapi import GrowwAPI

load_dotenv()


def get_groww_client():
    access_token = os.getenv("GROWW_ACCESS_TOKEN")

    if not access_token:
        raise ValueError("GROWW_ACCESS_TOKEN is not configured")

    return GrowwAPI(access_token)


def get_stock_quote(symbol):
    groww = get_groww_client()

    quote = groww.get_quote(
        exchange=groww.EXCHANGE_NSE,
        segment=groww.SEGMENT_CASH,
        trading_symbol=symbol
    )

    return quote


def market_agent(symbol="RELIANCE"):
    return get_stock_quote(symbol)
