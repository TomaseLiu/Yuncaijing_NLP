# -*- coding: utf-8 -*-

# Scrapy settings for yuncaijing project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#     http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#     http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'yuncaijing'

SPIDER_MODULES = ['yuncaijing.spiders']
NEWSPIDER_MODULE = 'yuncaijing.spiders'


ITEM_PIPELINES = {
    'yuncaijing.pipelines.YuncaijingNewsPipeline': 300,
}


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'yuncaijing (+http://www.yourdomain.com)'

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS=32

# Configure a delay for requests for the same website (default: 0)
# See http://scrapy.readthedocs.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
DOWNLOAD_DELAY=0.3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN=16
#CONCURRENT_REQUESTS_PER_IP=16

# Disable cookies (enabled by default)
COOKIES_ENABLED=False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED=False

# Override the default request headers:
#DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
#}

# Enable or disable spider middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'yuncaijing.middlewares.MyCustomSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    'yuncaijing.middlewares.MyCustomDownloaderMiddleware': 543,
#}


DOWNLOADER_MIDDLEWARES = {
#    'cnblogs.middlewares.MyCustomDownloaderMiddleware': 543,
#    'yuncaijing.middlewares.RandomUserAgent': 1, #随机user agent
    #'scrapy.contrib.downloadermiddleware.httpproxy.HttpProxyMiddleware': 110, #此API已经弃用
    'scrapy.downloadermiddlewares.httpproxy.HttpProxyMiddleware': 110, #代理需要用到
    'yuncaijing.middlewares.ProxyMiddleware': 100,
    #'cnblogs.middlewares.ProxyMiddleware': 100, #代理需要用到
#    'scrapy_crawlera.CrawleraMiddleware': 600, #crawlera代理用到
#    'yuncaijing.middlewares.RandomUserAgent': 1,
#    'scrapy.contrib.downloadermiddleware.httpproxy.HttpProxyMiddleware': 110,
#    #'scrapy.downloadermiddlewares.httpproxy.HttpProxyMiddleware': 110,
#    'yuncaijing.middlewares.ProxyMiddleware': 100,
}

RETRY_TIMES=2
#DOWNLOADER_MIDDLEWARES = {
    #'scrapy.contrib.downloadermiddleware.httpproxy.HttpProxyMiddleware': 110,
#    'scrapy_crawlera.CrawleraMiddleware': 600, #crawlera代理用到
    #'yuncaijing.middlewares.ProxyMiddleware': 100,
#}
# Enable or disable extensions
# See http://scrapy.readthedocs.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See http://scrapy.readthedocs.org/en/latest/topics/item-pipeline.html
#ITEM_PIPELINES = {
#    'yuncaijing.pipelines.SomePipeline': 300,
#}

# Enable and configure the AutoThrottle extension (disabled by default)
# See http://doc.scrapy.org/en/latest/topics/autothrottle.html
# NOTE: AutoThrottle will honour the standard settings for concurrency and delay
#AUTOTHROTTLE_ENABLED=True
# The initial download delay
#AUTOTHROTTLE_START_DELAY=5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY=60
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG=False
#USER_AGENTS = [
#    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; AcooBrowser; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
#    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0; Acoo Browser; SLCC1; .NET CLR 2.0.50727; Media Center PC 5.0; .NET CLR 3.0.04506)",
#    "Mozilla/4.0 (compatible; MSIE 7.0; AOL 9.5; AOLBuild 4337.35; Windows NT 5.1; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
#    "Mozilla/5.0 (Windows; U; MSIE 9.0; Windows NT 9.0; en-US)",
#    "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 2.0.50727; Media Center PC 6.0)",
#    "Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 1.0.3705; .NET CLR 1.1.4322)",
#    "Mozilla/4.0 (compatible; MSIE 7.0b; Windows NT 5.2; .NET CLR 1.1.4322; .NET CLR 2.0.50727; InfoPath.2; .NET CLR 3.0.04506.30)",
#    "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN) AppleWebKit/523.15 (KHTML, like Gecko, Safari/419.3) Arora/0.3 (Change: 287 c9dfb30)",
#    "Mozilla/5.0 (X11; U; Linux; en-US) AppleWebKit/527+ (KHTML, like Gecko, Safari/419.3) Arora/0.6",
#    "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.2pre) Gecko/20070215 K-Ninja/2.1.1",
#    "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN; rv:1.9) Gecko/20080705 Firefox/3.0 Kapiko/3.0",
#    "Mozilla/5.0 (X11; Linux i686; U;) Gecko/20070322 Kazehakase/0.4.5",
#    "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.8) Gecko Fedora/1.9.0.8-1.fc10 Kazehakase/0.5.6",
#    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11",
#    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_3) AppleWebKit/535.20 (KHTML, like Gecko) Chrome/19.0.1036.7 Safari/535.20",
#    "Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; fr) Presto/2.9.168 Version/11.52",
#]
'''
PROXIES = [
"124.88.67.24:81",
"124.88.67.30:80",
"101.231.46.34:8000",
"120.132.52.202:8888",
"42.96.174.136:9001",
"42.96.128.150:9001",
"120.24.166.128:9001",
"120.24.80.249:9001",
"120.24.172.184:9001",
"120.24.89.108:9001",
"120.24.74.152:9001",
"124.88.67.24:81",
"124.88.67.30:80",
"124.88.67.53:80",
"101.226.249.237:80",
"101.231.46.34:8000",
"120.132.52.207:8888",
"120.132.52.206:8888",
"120.132.52.8:8888",
"120.132.52.228:8888",
"120.132.52.11:8888",
"120.132.52.207:8888",
"120.24.81.130:9001",
"182.90.39.102:80",
"49.74.170.123:8080",
"171.37.109.0:8090",
"117.67.43.239:18186"
]'''


#CRAWLERA_ENABLED = True
#CRAWLERA_USER = '563e8be2c71d4ab5acb430896c38e875'
#CRAWLERA_PASS = 'tom722099'

# Enable and configure HTTP caching (disabled by default)
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED=True
#HTTPCACHE_EXPIRATION_SECS=0
#HTTPCACHE_DIR='httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES=[]
#HTTPCACHE_STORAGE='scrapy.extensions.httpcache.FilesystemCacheStorage'
PROXIES = [
"58.22.0.55:80",
"111.13.109.52:80",
"124.88.67.19:80",
"124.88.67.24:80",
"124.88.67.6:80",
"124.88.67.40:80",
"218.60.56.95:8080",
"124.88.67.40:82",
"124.88.67.40:83",
"58.83.190.104:80",
"58.211.23.161:8080",
"115.29.149.160:8888",
"124.88.67.40:81",
"124.88.67.40:843",
"120.132.52.228:8888",
"120.132.52.207:8888",
"120.132.52.206:8888",
"120.132.52.11:8888",
"120.132.52.3:8888",
"120.132.53.14:8888",
"120.132.52.28:8888",
"120.132.53.29:8888",
"120.132.52.172:8888",
"120.132.52.249:8888",
"120.132.52.202:8888",
"120.132.52.212:8888",
"120.132.53.30:8888",
"120.132.52.239:8888",
"120.132.52.213:8888",
"120.132.53.19:8888",
"120.132.52.192:8888",
"120.132.52.25:8888",
"120.132.52.124:8888",
"120.132.52.6:8888",
"120.132.52.10:8888",
"120.132.52.19:8888",
"120.132.52.14:8888",
"120.132.52.30:8888",
"120.132.53.24:8888",
"120.132.52.21:8888",
"115.29.33.89:8888",
"115.28.59.54:8888",
"120.24.165.204:8080",
"124.88.67.31:80",
"124.88.67.30:80",
"124.88.67.53:80",
"101.226.249.237:80",
"210.51.13.161:80",
"61.55.174.61:55336",
"58.20.114.88:55336",
"58.20.114.84:55336",
"58.20.114.85:55336",
"58.20.114.82:55336",
"58.20.114.86:55336",
"183.95.132.176:55336",
"123.134.35.86:9797",
"120.24.171.90:9001",
"120.24.89.175:9001",
"120.24.171.68:9001",
"120.24.172.177:9001",
"120.24.89.101:9001",
"120.24.80.249:9001",
"120.24.172.184:9001",
"120.24.80.99:9001",
"120.24.89.144:9001",
"120.24.166.128:9001",
"120.24.81.169:9001",
"120.24.89.146:9001",
"120.24.89.162:9001",
"120.24.172.203:9001",
"120.24.89.108:9001",
"120.24.168.142:9001",
"120.24.172.124:9001",
"120.24.89.171:9001",
"120.24.74.152:9001",
"120.24.81.130:9001",
"120.24.89.127:9001",
"120.24.81.163:9001",
"120.24.89.172:9001",
"120.24.89.126:9001",
"120.24.171.96:9001",
"120.24.172.180:9001",
"120.24.165.252:9001",
"120.24.172.205:9001",
"114.215.83.186:9001",
"121.42.146.205:9001",
"121.42.49.229:9001",
"121.42.148.69:9001",
"121.42.9.5:9001",
"114.215.83.216:9001",
"114.215.83.10:9001",
"121.42.12.163:9001",
"121.42.47.41:9001",
"114.215.83.190:9001",
"121.42.48.210:9001",
"121.42.47.81:9001",
"121.42.148.253:9001",
"121.42.49.211:9001",
"120.27.35.58:9001",
"121.42.9.65:9001",
"120.27.47.152:9001",
"114.215.83.14:9001",
"121.42.9.25:9001",
"42.96.128.150:9001",
"42.96.174.136:9001",
"42.96.128.204:9001",
"120.27.54.239:9001",
"42.96.185.105:9001",
"120.27.54.32:9001",
"120.27.54.120:9001",
"42.96.131.47:9001",
"120.27.44.105:9001",
"42.96.134.90:9001",
"42.96.174.23:9001",
"42.96.171.160:9001",
"120.27.54.3:9001",
"120.27.53.51:9001",
"42.96.135.115:9001",
"121.42.148.51:9001",
"120.27.33.43:9001",
"121.42.148.62:9001",
"42.96.135.128:9001",
"121.42.148.63:9001",
"42.96.169.9:9001",
"120.27.53.34:9001",
"42.96.173.74:9001",
"42.96.171.201:9001",
"42.96.128.170:9001",
"42.96.169.222:9001",
"42.96.135.118:9001",
"121.42.146.138:9001",
"120.27.53.129:9001",
"42.96.128.65:9001",
"42.96.175.239:9001",
"120.27.54.227:9001",
"42.96.170.171:9001",
"117.177.243.42:8082",
"117.177.243.42:8083",
"117.177.243.42:8080",
"183.111.169.204:3128",
"121.199.42.76:9001",
"114.215.238.221:9001",
"112.124.66.95:9001",
"112.124.66.6:9001",
"115.29.200.22:9001",
"121.199.44.197:9001",
"121.199.18.231:9001",
"114.215.238.50:9001",
"112.124.66.33:9001",
"115.29.200.18 :9001",
"114.215.238.73:9001",
"112.124.65.136:9001",
"115.29.200.191:9001",
"112.124.99.99:9001",
"112.124.18.245:9001",
"218.244.142.25:9001",
"121.199.13.98:9001",
"121.199.45.169:9001",
"115.29.33.234:9001",
"117.177.243.42:8085",
"117.21.184.56:55336",
"117.177.243.42:83",
"116.77.72.1:55336",
"58.20.114.81:55336",
"117.177.243.42:82",
"58.20.114.89:55336",
"58.20.114.83:55336",
"117.177.243.42:86",
"116.77.72.56:55336",
"58.20.114.90:55336",
"58.20.114.87:55336",
"117.177.243.42:81",
"117.177.243.42:85",
"220.202.123.38:55336",
"124.14.8.130:55336",
"124.14.12.176:55336",
"120.132.52.155:8888",
"119.253.252.29:3128",
"124.161.14.136:55336",
"117.177.243.57:82",
"180.97.185.35:10001",
"117.177.243.42:8084",
"117.177.243.46:8085",
"117.177.243.46:86",
"117.177.243.14:8083",
"117.177.243.57:8083",
"117.177.243.42:8086",
"117.177.243.46:84",
"222.73.217.7:8080",
"117.177.243.57:81",
"117.177.243.46:81",
"117.177.243.14:81",
"220.202.123.42:55336",
"220.202.123.34:55336",
"112.25.41.136:80",
"117.136.234.5:80",
"117.177.243.14:8082",
"117.177.243.57:8080",
"117.177.243.14:82",
"117.177.243.57:84",
"117.177.243.14:83",
"117.136.234.9:80",
"117.136.234.8:80",
"117.136.234.11:82",
"117.177.243.46:8080",
"117.136.234.12:82",
"117.136.234.6:82",
"117.136.234.8:81",
"119.71.191.115:808",
"117.136.234.10:82",
"94.103.47.250:8080",
"117.136.234.7:843",
"117.136.234.10:83",
"110.73.47.28:8123",
"117.177.243.14:8085",
"117.177.243.57:8082",
"117.177.243.46:8081",
"117.177.243.46:85",
"117.177.243.46:8083",
"117.177.243.57:86",
"117.177.243.57:85",
"117.177.243.14:85",
"117.177.243.57:83",
"117.177.243.14:84",
"120.198.231.21:80",
"111.205.46.26:8080",
"120.198.231.23:80",
"111.205.46.26:80",
"120.198.236.12:80",
"120.198.231.24:8080",
"182.90.24.19:80",
"60.175.139.4:8118",
"58.120.96.236:3128",
"113.30.102.91:3128",
"177.43.179.195:3128",
"171.83.129.18:18186",
"58.83.211.32:80",
"117.177.250.148:80",
"117.177.250.151:80",
"117.177.250.153:80",
"117.177.250.152:80",
"117.177.250.154:80",
"117.177.250.146:80",
"117.177.250.149:8080",
"117.177.250.147:8080",
"123.134.185.11:4040",
"117.177.250.151:8080",
"61.191.27.117:443",
"117.177.250.154:8080",
"117.177.250.148:8080",
"117.177.250.154:8081",
"60.206.253.241:3128",
"117.177.250.155:8080",
"117.177.250.153:8080",
"117.177.250.145:82",
"124.88.67.30:81",
"218.97.194.198:80",
"117.177.250.149:82",
"117.177.250.145:8080",
"124.88.67.19:81",
"124.88.67.39:80",
"119.188.115.26:80",
"119.188.115.27:80",
"124.88.67.39:81",
"117.177.250.155:82",
"117.177.250.148:82",
"117.177.250.147:81",
"117.177.250.151:81",
"124.88.67.24:843",
"117.177.250.146:82",
"117.177.250.152:8080",
"117.177.250.153:81",
"117.177.250.146:8080",
"117.177.250.145:81",
"124.88.67.31:843",
"117.177.250.151:84",
"117.177.250.153:8081",
"117.177.250.152:82",
"124.88.67.7:80",
"58.20.57.104:3128",
"124.88.67.39:843",
"221.10.102.202:80",
"58.22.0.53:80",
"183.223.137.85:8123",
"61.178.118.80:80",
"182.91.117.161:18186",
"60.169.234.34:18186",
"36.47.190.107:18186",
"111.76.197.130:18186",
"171.37.132.196:8123",
"113.248.44.197:18186",
"117.67.43.239:18186",
"171.37.109.0:8090",
"49.74.170.123:8080",
"182.90.39.102:80",
"106.36.16.41:8080",
"27.8.133.60:8080",
"27.21.10.80:18186",
"180.104.146.211:8080",
"60.167.180.74:18186",
"175.19.125.227:8080",
"121.31.87.156:8123",
"146.185.252.140:8888",
"125.82.100.113:18186"
]
