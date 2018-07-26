import pyfinex
import pytest
from decouple import config
API_KEY = config('API_KEY')
API_SECRET = config('API_SECRET')

def test_active():
    resp = pyfinex.v1.positions.active(API_KEY,API_SECRET)
    # resp[0]['id']
