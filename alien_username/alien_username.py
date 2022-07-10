# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
f = open("input00.txt","r")
n = int(f.readline())
usernames = [f.readline().strip() for i in range(n)]
regex = re.compile(r'^[_\.][0-9]+[a-zA-Z]*_?$')
for username in usernames:
    result = re.fullmatch(regex, username)
    if(result):
        print('VALID')
    else:
        print('INVALID')