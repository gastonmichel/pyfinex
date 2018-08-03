import base64
import hashlib
import hmac
import json
import requests
import time

API_URL = 'https://api.bitfinex.com'

def request(key=None, secret_key=None, version=1, endpoint=None, authenticate=False, method='GET', query_params=None, body_params=None):
    """Return the response from a request to the Bitfinex API
    
    Arguments:
        key {str} -- api key
        secret_key {str} -- api secret key
        version {int} -- api version
        endpoint {str} -- api endpoint
        authenticate {bool} -- auth or public request
        method {str} -- request method ("GET" or "POST")
        query_params {dict} -- query params to append to the URL 
        body_params {dict} -- params to pass to the body of the request 

    Keyword Arguments:
        params {dict} -- parameters to pass to the body and the payload (default: {None})
    
    Raises:
        ValueError
        BitfinexBadRequest

    Returns:
        object -- content
    """
    if endpoint:
        api_path = f'/v{version}/{endpoint}'
    else:
        raise(ValueError('No endpoint defined'))
    if authenticate:
        nonce = _nonce()
        payload = _payload(version, api_path, nonce, body_params)
        header =  _headers(key, secret_key, version, nonce, payload)
    else:
        header = {}

    response = requests.request(method, API_URL + api_path, headers=header, data=json.dumps(body_params), params=query_params, verify=True)
    content = response.json()

    if response.status_code >= 400:
        raise BitfinexBadRequest(response.status_code, content)
    else:
        return content

def _nonce():
    """Return a nonce.
    Used in authentication
    
    Returns:
        str -- timestamp in milliseconds
    """
    return str(int(round(time.time() * 1000)))

def _payload(version, api_path, nonce, params):
    """Return the header's payload based on version

    Arguments:
        version {int} -- api version either 1 or 2
        api_path {str} -- api path 
        nonce {str} -- nonce
        params {dict} -- parameters to include in the payload

    Raises:
        NotImplementedError -- version 1 and 2 supported

    Returns:
        [str] -- payload
    """
    if version == 1:
        payload_object = {}
        payload_object['request'] = api_path
        payload_object['nonce'] = nonce
        payload_object.update(params)
        payload = json.dumps(payload_object) 
    elif version == 2:
        payload = '/api' + api_path + nonce + json.dumps(params)
    else:
        raise NotImplementedError
    return payload

def _headers(key, secret_key, version, nonce, payload):
    """Return the request header based on version

    Arguments:
        version {int} -- api version either 1 or 2
        api_path {str} -- api path 
        nonce {str} -- nonce
        params {dict} -- parameters to include in the payload

    Raises:
        NotImplementedError -- version 1 and 2 supported

    Returns:
        [str] -- payload
    """    
    header = {}
    header['content-type'] = 'application/json'
    # header['accept'] = 'application/json'
    if version == 1:
        message = base64.b64encode(payload.encode('utf8'))
        header['X-BFX-APIKEY'] = key
        header['X-BFX-PAYLOAD'] = message
        header['X-BFX-SIGNATURE'] = _sign(version, secret_key, message)
    elif version == 2:
        message = payload.encode('utf8')
        header['bfx-nonce'] = nonce
        header['bfx-apikey'] = key
        header['bfx-signature'] = _sign(version, secret_key, message) 
    else:
        raise NotImplementedError
    return header  

def _sign(version, secret_key, message):
    """Signs the payload with SHA384 algorithm
    
    Arguments:
        secret_key {str} -- secret api key
        payload {str} -- payload
    
    Returns:
        str -- signature
    """   
    signature = hmac.new(secret_key.encode('utf8'), msg=message, digestmod=hashlib.sha384)
    return signature.hexdigest()

class BitfinexBadRequest(Exception):
    """ Catches bitfinex response errors

    Atributes:
        status_code {} -- status code of the request
        message {} -- message from server
    """
    def __init__(self, status_code, message):
        """Initialice an instance of BitfinexBadRequest
        
        Arguments:
            status_code {} -- status code of the request
            message {} -- message from server
        """
        self.status_code = status_code
        self.message = message
        super().__init__(f'BITFINEX API returned {status_code} Bad Request: {message}')