#############################详细扫描###############################
import nmap
def connect(ip):
    port=input('please input port : ')
    nm = nmap.PortScanner()
    nm.scan(ip,port)
    #print(nm.all_hosts())
    for host in nm.all_hosts():
        print(f"=================host: " '%s %s' % (host, nm[host].hostname()),"=========================")
        print('State : %s' % nm[host].state())

        for proto in nm[host].all_protocols():
            print('-----------------portdetalis-------------------------')
            print('Protocol : %s' % proto)
            lport = sorted(nm[host][proto].keys())
            for port in lport:
                print('port : %s\tstate : %s\tconnect : %s\tproduct : %s\tversion : %s\textrainfo : %s' % (port, nm[host][proto][port]['state'],nm[host][proto][port]['name'],nm[host][proto][port]['product'],nm[host][proto][port]['version'],nm[host][proto][port]['extrainfo']))

