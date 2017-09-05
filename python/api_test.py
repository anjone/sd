import urllib
import urllib.request

def getWeather(url, param):
    data = urllib.parse.urlencode(param, safe='|')
    #req = urllib.request.Request(url, data.encode(encoding='UTF8'))
    print(data)
    response = urllib.request.urlopen(url + '?' + data)
    the_page = response.read()
    print(the_page.decode('utf8'))


if __name__ == '__main__':
    url = 'http://api.weatherdt.com/common/'
    param = {}
    param['area'] = '101280601|101280301|101200101'
    param['type'] = 'alarm'
    param['key'] = 'f97952a95d4d7b6eb16e1a0dab3fc0d0'
    getWeather(url, param)
    
