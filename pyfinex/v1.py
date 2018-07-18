# Import Built-Ins
import json

# Import Homebrew
from pyfinex.api import API

# EndpointsMixin provides a mixin for the API instance
class V1(API):
    def __init__(self, **kargs):
        super().__init__(**kargs)
        self.version = 1
    # REST PUBLIC ENDPOINTS ###################################################
    def ticker(self, **params):
        """ Gives innermost bid and asks and information on the most recent trade, as well as high, low and volume of the last 24 hours.
        Docs: https://docs.bitfinex.com/v1/reference#rest-public-ticker
        """
        symbol = params.pop('symbol')
        endpoint = 'pubticker/' + symbol
        return self.request(endpoint, method='GET', auth=False, params=params)

    def stats(self, **params):
        """ Various statistics about the requested pair.
        Docs: https://bitfinex.readme.io/v1/reference#rest-public-stats
        """
        symbol = params.pop('symbol')
        endpoint = 'stats/' + symbol
        return self.request(endpoint, method='GET', auth=False, params=params)

    def fundingbook(self, **params):
        """ Get the full margin funding book.
        Docs: https://bitfinex.readme.io/v1/reference#rest-public-fundingbook
        """
        symbol = params.pop('symbol')
        endpoint = 'lendbook/' + symbol
        return self.request(endpoint, method='GET', auth=False, params=params)

    def orderbook(self, **params):
        """ Get the full order book.
        Docs: https://bitfinex.readme.io/v1/reference#rest-public-orderbook
        """
        symbol = params.pop('symbol')
        endpoint = 'book/' + symbol
        return self.request(endpoint, method='GET', auth=False, params=params)

    def trades(self, **params):
        """ Get a list of the most recent trades for the given symbol.
        Docs: https://bitfinex.readme.io/v1/reference#rest-public-trades
        """
        symbol = params.pop('symbol')
        endpoint = 'trades/' + symbol
        return self.request(endpoint, method='GET', auth=False, params=params)

    def lends(self, **params):
        """ Get a list of the most recent funding data for the given currency: total amount lent and Flash Return Rate (in % by 365 days) over time.
        Docs: https://bitfinex.readme.io/v1/reference#rest-public-lends
        """
        symbol = params.pop('symbol')
        endpoint = 'lends/' + symbol
        return self.request(endpoint, method='GET', auth=False, params=params)

    def symbols(self, **params):
        """ Get a list of valid symbol IDs.
        Docs: https://bitfinex.readme.io/v1/reference#rest-public-symbols
        """
        endpoint = 'symbols'
        return self.request(endpoint, method='GET', auth=False, params=params)

    def symbol_details(self, **params):
        """ Get a list of valid symbol IDs and the pair details.
        Docs: https://bitfinex.readme.io/v1/reference#rest-public-symbol-details
        """
        symbol = params.pop('symbol')
        endpoint = 'symbols_details'
        return self.request(endpoint, method='GET', auth=False, params=params)

    # REST AUTHENTICATED ENDPOINTS ############################################
    # Account
    def account_fees(self, **params):
        """ Check the balance.
        Docs: https://bitfinex.readme.io/v1/reference#rest-auth-account-info
        """
        endpoint = 'account_infos'
        return self.request(endpoint, method='POST', payload_params=params)

    def account_infos(self, **params):
        """  See the fees applied to your withdrawals.
        Docs: https://bitfinex.readme.io/v1/reference#rest-auth-fees
        """
        endpoint = 'account_fees'
        return self.request(endpoint, method='POST', payload_params=params)

    def summary(self, **params):
        """  Returns a 30-day summary of your trading volume and return on margin funding.
        Docs: https://bitfinex.readme.io/v1/reference#rest-auth-summary
        """
        endpoint = 'summary'
        return self.request(endpoint, method='POST', payload_params=params)

    def deposit(self, **params):
        """ Return your deposit address to make a new deposit.
        Docs: https://bitfinex.readme.io/v1/reference#rest-auth-deposit
        """
        endpoint = 'deposit/new'
        return self.request(endpoint, method='POST', payload_params=params)

    def key_permissions(self, **params):
        """ Check the permissions of the key being used to generate this request.
        Docs: https://bitfinex.readme.io/v1/reference#auth-key-permissions
        """
        endpoint = 'key_info'
        return self.request(endpoint, method='POST', payload_params=params)
    
    def margin_information(self, **params):
        """ See your trading wallet information for margin trading.
        Docs: https://bitfinex.readme.io/v1/reference#rest-auth-margin-information
        """
        endpoint = 'margin_infos'
        return self.request(endpoint, method='POST', payload_params=params)
    
    def wallet_balances(self, **params):
        """ See your balances.
        Docs: https://bitfinex.readme.io/v1/reference#rest-auth-wallet-balances
        """
        endpoint = 'balances'
        return self.request(endpoint, method='POST', payload_params=params)

    def tansfer_between_wallets(self, **params):
        """ Allow you to move available balances between your wallets.
        Docs: https://bitfinex.readme.io/v1/reference#rest-auth-transfer-between-wallets
        """
        endpoint = 'transfer'
        return self.request(endpoint, method='POST', payload_params=params)

    def withdrawal(self, **params):
        """ Allow you to request a withdrawal from one of your wallet.
        Docs: https://bitfinex.readme.io/v1/reference#rest-auth-withdrawal
        """
        endpoint = 'withdraw'
        return self.request(endpoint, method='POST', payload_params=params)

    # Order
    def new_order(self, **params):
        """ Submit a new order.
        Docs: https://bitfinex.readme.io/v1/reference#rest-auth-orders
        """
        endpoint = 'order/new'
        return self.request(endpoint, method='POST', payload_params=params)

    def multiple_new_orders(self, **params): #TODECIDE: enforce params or not
        """ Submit several new orders at once.
        Docs: https://bitfinex.readme.io/v1/reference#rest-auth-multiple-new-orders
        """
        endpoint = 'order/new/multi'
        return self.request(endpoint, method='POST', payload_params=params)

    def cancel_order(self, **params):
        """ Cancel an order.
        Docs: https://bitfinex.readme.io/v1/reference#rest-auth-cancel-order
        """
        endpoint = 'order/cancel'
        return self.request(endpoint, method='POST', payload_params=params)

    def cancel_multiple_orders(self, **params):
        """ Cancel multiples orders at once.
        Docs: https://bitfinex.readme.io/v1/reference#rest-auth-cancel-multiple-orders
        """
        endpoint = 'order/cancel/multi'
        return self.request(endpoint, method='POST', payload_params=params)

    def cancel_all_orders(self, **params):
        """ Cancel multiples orders at once.
        Docs: https://bitfinex.readme.io/v1/reference#rest-auth-cancel-all-orders
        """
        endpoint = 'order/cancel/all'
        return self.request(endpoint, method='POST', payload_params=params)

    def replace_order(self, **params):
        """ Replace an orders with a new one.
        Docs: https://bitfinex.readme.io/v1/reference#rest-auth-replace-order
        """
        endpoint = 'order/cancel/replace'
        return self.request(endpoint, method='POST', payload_params=params)

    def order_status(self, **params):
        """ Get the status of an order. Is it active? Was it cancelled? To what extent has it been executed? etc.
        Docs: https://bitfinex.readme.io/v1/reference#rest-auth-order-status
        """
        endpoint = 'order/status'
        return self.request(endpoint, method='POST', payload_params=params)

    def active_orders(self, **params):
        """ View your active orders.
        Docs: https://bitfinex.readme.io/v1/reference#rest-auth-active-orders
        """
        endpoint = 'orders'
        return self.request(endpoint, method='POST', payload_params=params)
    
    def orders_history(self, **params):
        """ View your active orders.
        Docs: https://bitfinex.readme.io/v1/reference#rest-auth-orders-history
        """
        endpoint = 'orders/hist'
        return self.request(endpoint, method='POST', payload_params=params)

    # Positions
    def active_positions(self, **params):
        """ View your active positions.
        Docs: https://bitfinex.readme.io/v1/reference#rest-auth-active-positions
        """
        endpoint = 'positions'
        return self.request(endpoint, method='POST', payload_params=params)

    def claim_position(self, **params):
        """ A position can be claimed if:
        It is a long position:
            The amount in the last unit of the position pair that you have in your trading wallet AND/OR the realized profit of the position is greater or equal to the purchase amount of the position (base price * position amount) and the funds which need to be returned.
            For example, for a long BTCUSD position, you can claim the position if the amount of USD you have in the trading wallet is greater than the base price * the position amount and the funds used.
        It is a short position:
            The amount in the first unit of the position pair that you have in your trading wallet is greater or equal to the amount of the position and the margin funding used.
        Docs: https://bitfinex.readme.io/v1/reference#rest-auth-claim-position
        """
        endpoint = 'position/claim'
        return self.request(endpoint, method='POST', payload_params=params)

    # Historical Data
    def balance_history(self, **params):
        """ View all of your balance ledger entries.
        Docs: https://bitfinex.readme.io/v1/reference#rest-auth-balance-history
        """
        endpoint = 'history'
        return self.request(endpoint, method='POST', payload_params=params)

    def deposit_withdrawal_history(self, **params):
        """ View all of your balance ledger entries.
        Docs: https://bitfinex.readme.io/v1/reference#rest-auth-deposit-withdrawal-history
        """
        endpoint = 'history/movements'
        return self.request(endpoint, method='POST', payload_params=params)

    def past_trades(self, **params):
        """ View all of your balance ledger entries.
        Docs: https://bitfinex.readme.io/v1/reference#rest-auth-past-trades
        """
        endpoint = 'mytrades'
        return self.request(endpoint, method='POST', payload_params=params)

    # Margin Funding
    def new_offer(self, **params):
        """ Submit a new offer.
        Docs: https://bitfinex.readme.io/v1/reference#rest-auth-new-offer
        """
        endpoint = 'offer/new'
        return self.request(endpoint, method='POST', payload_params=params)

    def cancel_offer(self, **params):
        """ Cancel an offer.
        Docs: https://bitfinex.readme.io/v1/reference#rest-auth-cancel-offer
        """
        endpoint = 'offer/cancel'
        return self.request(endpoint, method='POST', payload_params=params)

    def offer_status(self, **params):
        """ Get the status of an offer. Is it active? Was it cancelled? To what extent has it been executed? etc.
        Docs: https://bitfinex.readme.io/v1/reference#rest-auth-offer-status
        """
        endpoint = 'offer/status'
        return self.request(endpoint, method='POST', payload_params=params)

    def active_credits(self, **params):
        """ View your funds currently taken (active credits).
        Docs: https://bitfinex.readme.io/v1/reference#rest-auth-active-credits
        """
        endpoint = 'credits'
        return self.request(endpoint, method='POST', payload_params=params)

    def offers(self, **params):
        """ View your active offers.
        Docs: https://bitfinex.readme.io/v1/reference#rest-auth-offers
        """
        endpoint = 'offers'
        return self.request(endpoint, method='POST', payload_params=params)

    def offers_hist(self, **params):
        """ View your latest inactive offers. Limited to last 3 days and 1 request per minute.
        Docs: https://bitfinex.readme.io/v1/reference#rest-auth-offers-hist
        """
        endpoint = 'offers/hist'
        return self.request(endpoint, method='POST', payload_params=params)

    def mytrades_funding(self, **params):
        """ View your past trades.
        Docs: https://bitfinex.readme.io/v1/reference#rest-auth-mytrades-funding
        """
        endpoint = 'mytrades_funding'
        return self.request(endpoint, method='POST', payload_params=params)

    def active_funding_used_in_a_margin_position(self, **params):
        """ View your funding currently borrowed and used in a margin position.
        Docs: https://bitfinex.readme.io/v1/reference#rest-auth-active-funding-used-in-a-margin-position
        """
        endpoint = 'taken_funds'
        return self.request(endpoint, method='POST', payload_params=params)

    def active_funding_not_used_in_a_margin_position(self, **params):
        """ View your funding currently borrowed and not used (available for a new margin position).
        Docs: https://bitfinex.readme.io/v1/reference#rest-auth-active-funding-not-used-in-a-margin-position
        """
        endpoint = 'unused_taken_funds'
        return self.request(endpoint, method='POST', payload_params=params)

    def total_taken_funds(self, **params):
        """ View the total of your active-funding used in your position(s).
        Docs: https://bitfinex.readme.io/v1/reference#rest-auth-total-taken-funds
        """
        endpoint = 'total_taken_funds'
        return self.request(endpoint, method='POST', payload_params=params)

    def close_margin_funding(self, **params):
        """ Allow you to close an unused or used taken fund
        Docs: https://bitfinex.readme.io/v1/reference#rest-auth-close-margin-funding
        """
        endpoint = 'funding/close'
        return self.request(endpoint, method='POST', payload_params=params)

    def basket_manage(self, **params):
        """ This endpoint is used to manage the creation or destruction of tokens via splitting or merging. For the moment, this is only useful for the bcc and bcu tokens.
        Docs: https://bitfinex.readme.io/v1/reference#basket-manage
        """
        endpoint = 'basket_manage'
        return self.request(endpoint, method='POST', payload_params=params)

    def close_position(self, **params):
        """ Closes the selected position with a market order.
        Docs: https://bitfinex.readme.io/v1/reference#close-position
        """
        endpoint = 'position/close'
        return self.request(endpoint, method='POST', payload_params=params)


