import urllib2

proxy_host = '10.228.110.21:8002'
proxy_handler = urllib2.ProxyHandler({'ftp': proxy_host})

proxy_auth_handler = urllib2.ProxyBasicAuthHandler()
proxy_auth_handler.add_password(None, proxy_host, 'jiangqizhou', 'Cpic123456')

opener_through_proxy = urllib2.build_opener(proxy_handler, proxy_auth_handler)

conn = opener_through_proxy.open('ftp://ftpuser:ftp_tai@2016#@58.250.152.93')

print(conn.read())