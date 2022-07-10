# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
f = open("input00.txt","r")
n = int(f.readline())
sentences = [f.readline().strip() for i in range(n)]
t = int(f.readline())
words = [f.readline().strip() for i in range(t)]
results = [0 for i in range(t)]
for i in range(t):
    for sent_child in sentences:
        sent_split = (re.split('[\W\b]', sent_child))
        for word in sent_split:
            if(re.fullmatch(words[i], word)):
                results[i]+=1
for result in results:
    print(result)