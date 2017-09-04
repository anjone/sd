import urllib
import urllib.request

def sendWxMessage(url, param):
    data = urllib.parse.urlencode(param)
    req = urllib.request.Request(url, data.encode(encoding='UTF8'))
    response = urllib.request.urlopen(req)
    the_page = response.read()
    print(the_page.decode('utf8'))


if __name__ == '__main__':
    url = 'http://112.91.153.120/common'
    param = {}
    param['loginName'] = 'tempnotices'
    param['pwd'] = '6817bad65a300a6dc788d9d6458b2475'
    param['openid'] = 'ogFACuAJJJtj4G0KVqwqknBT2hLE'
    #param["id"] = ""
    #param["typeId"] = ""
    cnt = '{"data":{"first":{"color":"#0A0A0A","value":"亲爱的江启洲，您好!"},"keyword1":{"color":"#173177","value":"阿尔法保险"},"keyword2":{"color":"#173177","value":"黑科技来袭！太保原创人工智能产品“阿尔法”保险顾问，邀您试算保险身价！\\n保险给谁买？买什么？买多少？快来点击测试一下>>"},"remark":{"color":"#cccccc","value":"请点击“详情”了解具体信息。"}},"template_id":"5m5tRSEZltMG_gAnuOf0ii5UGrLI0uNAUQ0brHwE_vI","topcolor":"#FF0000","touser":"ogFACuAJJJtj4G0KVqwqknBT2hLE","url":"http://ai.cpic.com.cn/cta/aiweb/index.html"}'
    param['cnt'] = cnt
    sendWxMessage(url, param)
    
