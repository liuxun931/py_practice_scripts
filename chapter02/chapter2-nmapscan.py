import optparse
import socket
import threading
import os
import nmap3

port_list = [22,80,257,443,4434,8080,8088,19009]
socket.setdefaulttimeout(1)
screenLock = threading.Semaphore(value = 1)
os.system('ulimit -n 65535')

nmap = nmap3.Nmap()
nmapss = nmap3.NmapScanTechniques()

host = "10.100.100.59"


def connScan(ip, port):
    pass


def main(host=host, port_list=port_list):
    ss = nmapss.nmap_syn_scan(target=host)
    st = nmapss.nmap_tcp_scan(target=host)
    sf = nmapss.nmap_fin_scan(target=host)
    sp = nmapss.nmap_ping_scan(target=host)
    sl = nmapss.nmap_idle_scan(target=host)
    print(ss.get(host).get('ports'))
    print(st.get(host).get('ports'))
    print(sf)
    print(sp)
    print(sl)
    
    
if __name__ == "__main__":
    main()

'''
'nmap_detect_firewall'
'nmap_dns_brute_script'
'nmap_list_scan'
'nmap_os_detection'
'nmap_stealth_scan'
'nmap_subnet_scan'
'nmap_version'
'nmap_version_detection'
'nmaptool'
'''

