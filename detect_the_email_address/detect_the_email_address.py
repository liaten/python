#TODO:NOT_SOLVED
# Enter your code here. Read input from STDIN. Print output to STDOUT
import re,pathlib
def detect_the_email_address(input_addr, output_addr, N):
    f = open(input_addr,"r")
    n = int(f.readline())
    lines = [f.readline().strip() for i in range(n)]
    regex = re.compile(r"(\w+\.)*\w+@(\w+\.)+\w+")
    result = [re.findall(regex, line) for line in lines]
    results = []
    for line in lines:
        result = re.search(regex, line)
        if(isinstance(result, re.Match)):
            results.append(result.group(0))
    results = list(set(results))
    results.sort()
    r_str = ';'.join(results)
    f.close()
    f = open(output_addr,"r")
    expected = f.readlines()[0]
    if(r_str==expected):
        print(f'{N}: VALID')
    else:
        print(f'{N}: INVALID\nEXPECTED:\t{expected}\nGOT:\t\t{r_str}')
    f.close()
current_path = str(pathlib.Path(__file__).parent.resolve())
for i in range(4):
    detect_the_email_address(current_path + f"/input0{i}.txt", current_path + f"/output0{i}.txt",i)