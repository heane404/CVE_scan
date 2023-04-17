#############################端口扫描###############################
import nmap
def connect(ip):
    nm = nmap.PortScanner()
    nm.scan(ip, '1-65535')
    for host in nm.all_hosts():
        for proto in nm[host].all_protocols():
            print('-----------------portstatue----------------------')
            print('Protocol : %s' % proto)
            lport = sorted(nm[host][proto].keys())
            for port in lport:
                print('port : %s\tstate : %s' % (port, nm[host][proto][port]['state']))
#if __name__=='__main__':
#ip='192.168.122.219'
#scanip(ip)
