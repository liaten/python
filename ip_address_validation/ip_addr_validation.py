# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
f = open("input00.txt","r")
n = int(f.readline())
ips = [f.readline().strip() for i in range(n)]
regex_ipv4 = re.compile(r'^((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$')
regex_ipv6 = re.compile(r'([0-9a-f]{1,4}:){7}([0-9a-f]{1,4})')
for ip in ips:
    is_ipv4 = re.fullmatch(regex_ipv4, ip)
    is_ipv6 = re.fullmatch(regex_ipv6, ip)
    if(is_ipv4):
        print('IPv4')
    elif(is_ipv6):
        print('IPv6')
    else:
        print('Neither')