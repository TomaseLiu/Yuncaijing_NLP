import base64
from settings import PROXIES
import random




class ProxyMiddleware(object):
    
    def process_request(self, request, spider):
        proxy = random.choice(PROXIES)

        request.meta['proxy'] = "http://%s" % proxy

        proxy_user_pass = ""

        encoded_user_pass = base64.encodestring(proxy_user_pass)

        request.headers['Proxy-Authorization'] = 'Basic' + encoded_user_pass
        print proxy
