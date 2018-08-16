import requests



class Client(Session):
    def __init__(self, key, secret_key, **kwargs):
        self.key = key
        self.secret_key = secret_key
        self.v1 = V1()


class V1(object):
    def __init__(self, *args, **kwargs):
        self.version = 1
        self.public = Public()
class Public(object):
    def book():
        return 'book'
c = Client(123,123)
c.v1.public.book()
