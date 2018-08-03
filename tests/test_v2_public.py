import pytest

import pyfinex

def test_ticker():
    resp = pyfinex.v2.public.ticker()

def test_failed_ticker():
    with pytest.raises(pyfinex.api.BitfinexBadRequest):
        resp = pyfinex.v2.public.ticker(Symbol='btcusd')
def test_stats():
    resp = pyfinex.v2.public.stats()

def test_lendbook():
    resp = pyfinex.v2.public.books(Symbol='fUSD')

def test_orderbook():
    resp = pyfinex.v2.public.books(Symbol='tBTCUSD')
