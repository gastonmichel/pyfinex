import pyfinex
import pytest
from decouple import config

API_KEY = config('API_KEY')
API_SECRET = config('API_SECRET')

def test_active():
    resp = pyfinex.v2.positions.active(API_KEY,API_SECRET)
def test_past_trades():
    resp = pyfinex.v2.historical.past_trades(API_KEY, API_SECRET, Symbol='tBTCUSD', limit=25)
    