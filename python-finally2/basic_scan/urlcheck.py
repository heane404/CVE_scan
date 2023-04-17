#############################ssh爆破###############################
import requests
txt = open('/home/frost/桌面/python/basic_scan/dit3.txt', "r")
open_url = []
all_url = []
def search_url(url,txt):
    with open('/home/frost/桌面/python/basic_scan/dit3.txt', "r") as f:
        for each in f:
            each = each.replace('\n', '')
            urllist = url + each
            all_url.append(urllist)
            handle_url(urllist)
def handle_url(urllist):
    # print("查找：" + urllist + '\n')
    try:
        req = requests.get(urllist)
        if req.status_code == 200:
            open_url.append(urllist)
        if req.status_code == 301:
            open_url.append(urllist)
    except:
        pass
def connect(ip):
    url=f"http://{ip}:8080/"
    search_url(url, txt)
    if open_url:
        print("后台地址：")
        for each in open_url:
            print("[+]" + each)
    else:
        print("没有找到网站后台")


