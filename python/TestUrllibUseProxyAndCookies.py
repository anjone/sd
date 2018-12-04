import urllib
import urllib.request
import http.cookiejar

PROXY_URL=""
PROXY_NAME=""
PROXY_PASS=""

def testProxy():
    proxy = urllib.request.ProxyHandler({"http": ""})
    opener = urllib.request.build_opener(proxy)
    urllib.request.install_opener(opener)
    resp = urllib.request.urlopen("http://www.bing.com")
    print(resp.read())

def testProxyAndCookies():
    proxy = urllib.request.ProxyHandler({"http": ""})
    opener = urllib.request.build_opener(proxy)
    urllib.request.install_opener(opener)

    cj = http.cookiejar.CookieJar()
    cookie_processor = urllib.request.HTTPCookieProcessor()
    cookie_opener = urllib.request.build_opener(cookie_processor)
    urllib.request.install_opener(cookie_opener)

    login_data = urllib.parse.urlencode({}).encode("utf-8")

    resp = urllib.request.urlopen("https://login.sina.com.cn/signup/signin.php?entry=sso", login_data)
    #print(resp.read().decode("gbk"))
    for cookie in cj:
        print("------First time cookie: %s --> %s" % (cookie.name, cookie.value))
    print("Headers: " % resp.headers)

    resp = urllib.request.urlopen("http://my.sina.com.cn/")
    print(resp.read().decode("utf-8"))

if __name__ == "__main__":
    testProxyAndCookies()