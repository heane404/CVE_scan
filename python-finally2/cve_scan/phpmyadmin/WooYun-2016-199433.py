import requests
import yaml
def connect(ip):
    # 读取 YAML 文件
    url = f'{ip}'
    with open('/home/frost/桌面/python/cve_scan/phpmyadmin/WooYun-2016-199433.yml', 'r') as f:
        data = yaml.safe_load(f)
        payload='/scripts/setup.php'
        urls=url+payload
        # 发送请求
        response = requests.request(
            method=data['method'],
            url=urls,
            headers=data['headers'],
            data=data['data']
        )
        if 'sys:' in response.text:
            print('存在WooYun-2016-199433漏洞！')
if __name__=='__main__':
    url = 'http://192.168.122.219:8080'
    check(url)