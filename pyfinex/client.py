# Import Homebrew
from pyfinex.v1 import V1
from pyfinex.v2 import V2

class Client(object):
    def __init__(self, environment='live', key=None, secret_key=None):
        """ Instantiates an instance of BitfinexPy's API wrapper """
        self.key = key
        self.secret_key = bytes(secret_key, 'utf-8')
        self.enviroment = environment
        self.v1 = V1(environment=self.enviroment, key=self.key, secret_key=self.secret_key)
        self.v2 = V2(environment=self.enviroment, key=self.key, secret_key=self.secret_key)