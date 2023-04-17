#############################主机扫描#############################
import nmap
def connect(hosts):
    nm = nmap.PortScanner()
    nm.scan(hosts=hosts, arguments='-n -sP -PE')
    hosts_list = [(x, nm[x]['status']['state']) for x in nm.all_hosts()]
    for host, status in hosts_list:
        print("host : " + host + "   status : " + status)
if __name__ == '__main__':
 hosts='192.168.122.0/24'
 scanhost(hosts)
