# Import Homebrew
from pyfinex.api import API

# EndpointsMixin provides a mixin for the API instance
class V2(API):
    def __init__(self, *args):
        super().__init__(*args)
        self.version = 2
    # REST PUBLIC ENDPOINTS ###################################################
    def platform_status(self, **params):
        """ Get the current status of the platform. Maintenance periods last for just few minutes and might be necessary 
        from time to time during upgrades of core components of our infrastructure.
        Docs: https://bitfinex.readme.io/v2/reference#rest-public-platform-status
        """
        endpoint = 'platform/status'
        return self.request(endpoint, method='GET', auth=False, params=params)

    # REST CALCULATION ENDPOINTS ##############################################

    # REST AUTHENTICATED ENDPOINTS ############################################

    



