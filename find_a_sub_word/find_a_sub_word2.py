# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
f = open("input01.txt","r")
n = int(f.readline())
seq = [f.readline().strip() for i in range(n)]
q = int(f.readline())
query = [f.readline().strip() for i in range(q)]
reg = [(re.compile('[a-zA-Z0-9_]+'+query[i]+'[a-zA-Z0-9_]+')) for i in range(q)]
# print(reg)
results = [0 for i in range(q)]
for i in range(q):
    # print(reg[i])
    for seq_child in seq:
        results[i]+=len(re.findall(reg[i], seq_child))
for result in results:
    print(result)