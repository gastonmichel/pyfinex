# TODO!


# Import Built-Ins
import base64
import hashlib
import hmac
import json
import requests
import time

# HTTPS Streaming
class Streamer:
    """ Provides functionality for HTTPS Streaming """
    # TODO: WS stream reader
    def __init__(self, symbol, environment='live', heartbeat=1.0):
        """ Instantiates an instance of BitfinexPy's streaming API wrapper. """

        self.connected = False

        if environment == 'live':
            self.api_url = 'https://api.bitfinex.com/v1/pubticker/' + symbol
        else:
            # for future, access to a demo account.
            pass

        self.heartbeat = heartbeat

        self.client = requests.Session()

    def start(self, **params):
        """ Starts the stream with the given parameters """
        keys = ['last_price', 'bid', 'volume', 'ask', 'low', 'high']

        self.connected = True
        request_args = {}
        content_ = {k: None for k in keys}

        while self.connected:
            response = self.client.get(self.api_url, **request_args)
            content = response.content.decode('ascii')
            content = json.loads(content)

            if response.status_code != 200:
                self.on_error(content)

            # when the tick is updated
            if any([content.get(k) != content_.get(k) for k in keys]):
                self.on_success(content)
                content_ = content

            time.sleep(self.heartbeat)

    def on_success(self, content):
        """ Called when data is successfully retrieved from the stream """
        print(content)
        return True

    def on_error(self, content):
        """ Called when stream returns non-200 status code
        Override this to handle your streaming data.
        """
        self.connected = False
        print(content)
        return
