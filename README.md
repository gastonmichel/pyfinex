pyfinex
======
Python wrapper for Bitfinex API.

Dependencies
======
Requests library is required.

Usage
======
Include the pyfinex module and use it as a toolbox. For trading, a key and a secret key must be provided.

	import pyfinex

    API_KEY = 'insert key'
    API_SECRET = 'insert secret'

	resp = pyfinex.v1.positions.active(key=API_KEY, secret_key=API_SECRET)
    resp = pyfinex.v1.public.ticker(symbol='btcusd')

Function names are organized for better coding

**Function names are referred in part to the api doc's html, which you can see [Bitfinex API web page](http://docs.bitfinex.com/).**
**Required params to build the request's url are coded in the function's args, other query params are to be added acording to api doc**

**BEWARE: some inputs varies from v1 to v2. Example: v1>> 'BTCUSD' v2>> 'tBTCUSD'**

All documented API calls are implemented!

Examples
======
### Get the latest BTCUSD price
	resp = pyfinex.v1.public.ticker(symbol='btcusd')
### View your active orders
    resp = pyfinex.v1.positions.active(API_KEY,API_SECRET)
### Get the BTCUSD order book
    resp = pyfinex.v1.public.order_book(symbol='btcusd')
### Get the last BTCUSD 1m candle 
    resp = pyfinex.v2.public.candles(Symbol='tBTCUSD', TimeFrame='1m', Section='last')

Note: in v2 the parameters are capital case.
### Submit a new order
For example, if you'd like to buy 0.001 BTC as 0.01 BTC/USD, you need to specify the parameters acording to the api doc. You may parse the response to get the order id for future use.

	resp = pyfinex.v1.orders.new(symbol="BTCUSD", amount=0.001, price=0.01, side='buy', type='market')

### In case there is a new call you can do it yourself!:
    pyfinex.api.request(authenticate=True, 
        key=API_KEY, 
        secret_key=API_SECRET, 
        version=1, 
        endpoint='new/api/call/here', 
        method='POST', 
        body_params={}, 
        query_params={})

Test
======
1. Replace your keys in .env.example file, and rename it to .env
1. Include your unit tests as functions in a test_vX_*.py file
    def test_ticker():
        resp = pyfinex.v1.public.ticker(symbol='btcusd')
        resp['mid']
1. Run the tests using pytest

Known Issues
======
- No

TODO
=====
- Test every endpoint


Contributing
======
1. Create an issue and discuss.
1. Create a feature branch containing only your fix or feature.
1. Add tests, please!!
1. Create a pull request.
1. Thanks!

References
======
- [https://github.com/scottjbarr/bitfinex](https://github.com/scottjbarr/bitfinex)
- [https://github.com/jimako1989/bitfinexpy](https://github.com/jimako1989/bitfinexpy)
- [Bitfinex official API wrapper for Ruby](https://github.com/bitfinexcom/bitfinex-api-rb)
- [Bitfinex v1 API doc](https://bitfinex.readme.io/v1/docs)
- [Bitfinex v2 API doc](https://bitfinex.readme.io/v2/docs)

Licence
======
The MIT License (MIT)

Copyright (c) 2018 faberquisque

See [LICENSE.md](LICENSE.md)