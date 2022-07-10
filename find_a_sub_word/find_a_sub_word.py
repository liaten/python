# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
def find_a_sub_word(_n,_seq,_q,_query):
    n = _n
    seq = _seq
    q = _q
    query = _query
    regex = re.compile('[a-zA-Z0-9_]+'+query+'[a-zA-Z0-9_]+')
    res = re.findall(regex,seq)
    print(len(res))
find_a_sub_word(1, 'existing pessimist optimist this is', 1, 'is')