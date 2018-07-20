# Import Built-Ins
import base64
import hashlib
import hmac
import json
import requests
import time

API_URL = 'https://api.bitfinex.com/'

# TODO: evaluate Bitfinex 400BadRequest error handling

def public_get(version:int, endpoint:str, params=None):
    """Return the response from a GET request to the api
    
    Arguments:
        version {int} -- api version
        endpoint {str} -- api endpoint 
    
    Keyword Arguments:
        params {dict} -- parameters to pass to the request, usually query params (default: {None})
    
    Returns:
        dict -- content
    """
    api_path = f'v{version}/{endpoint}'
    response = requests.get(API_URL + api_path, params=params)
    content = response.json()
    return content

# TODO: evaluate public post for v2/calc
def public_post():
    pass

def auth_post(key, secret_key, version:int, endpoint:str, params=None):
    """Return the response from a POST request to the api with authentification
    
    Arguments:
        key {str} -- api key
        secret_key {str} -- api secret key
        version {int} -- api version
        endpoint {str} -- api endpoint
    
    Keyword Arguments:
        params {dict} -- parameters to pass to the body and the payload (default: {None})
    
    Returns:
        dict -- content
    """
    api_path = f'v{version}/{endpoint}'
    nonce = _nonce()
    payload = _payload(version, api_path, nonce, params)
    header =  _headers(version, nonce, payload)
    response = request.post( API_URL + api_path, header=header, data=params)
    content = response.json()
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
        payload = base64.b64encode(bytes(json.dumps(payload_object), "utf-8"))
    elif version == 2:
        payload = '/api/' + api_path + nonce + json.dumps(params)
    else:
        raise NotImplementedError
    return payload

def _headers(key, version, nonce, payload):
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
    header['accept'] = 'application/json'
    if version == 1:
        header['X-BFX-APIKEY'] = key
        header['X-BFX-PAYLOAD'] = payload
        header['X-BFX-SIGNATURE'] = _sign(payload)
    elif version == 2:
        header['bfx-nonce'] = nonce
        header['bfx-apikey'] = key
        header['bfx-signature'] = _sign(payload) 
    else:
        raise NotImplementedError
    return header  

def _sign(secret_key, payload):
    """Signs the payload with SHA384 algorithm
    
    Arguments:
        secret_key {str} -- secret api key
        payload {str} -- payload
    
    Returns:
        str -- signature
    """
    return hmac.new(secret_key, msg=payload, digestmod=hashlib.sha384).hexdigest()
