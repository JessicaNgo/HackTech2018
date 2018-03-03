# this file will query and parse data from the yelp API

import requests

def query_yelp_api(*args, **kwargs):
    # Parameters for query are found in docs here:r
    # https://www.yelp.com/developers/documentation/v3/business_search
    # some parameters of note to this api, "term", "location", "radius"

    # RETURN - json results
    #API KEY:
    # TODO: what should we do if there is no location provided from user? ie. no user location - use last location?

    API_KEY=""
    YELP_API_ENDPOINT="https://api.yelp.com/v3/businesses/search"
    query_string = ""
    pass
