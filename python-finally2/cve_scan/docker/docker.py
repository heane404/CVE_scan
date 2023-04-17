#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :dockercve.py
# @Time      :2023/4/4 12:15
# @Author    :Raink
import re

import requests

if __name__ == "__main__":
    run_code = 0
def connect(ip):
  url=f"{ip}/version"
  try:
    res = requests.get(url)
    code=res.status_code
    if code==200:
         print("存在docker-unauthoriun-rce漏洞!")
  except:
      pass

# upload("http://192.168.114.120:2375/version")