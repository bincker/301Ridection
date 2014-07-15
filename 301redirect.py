from libmproxy.flow import Response
from netlib.odict import ODictCaseless

"""
This example shows two ways to redirect flows to other destinations.
"""

def request(context, flow):

    if flow.request.host.endswith("com"):
        resp = Response(flow.request,
                        [1,1],
                        301, "OK",
                        ODictCaseless([["Location","http://www.bbc.co.uk"]]),
                        "",
                        None)
        flow.request.reply(resp)
