from pyfinex.client import Client

myClient = Client()

myClient.v1.account.account_fees()
myClient.v2.books()