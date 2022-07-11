#TODO:NOT_SOLVED
import re,pathlib
def detect_the_domain_name(input_addr, output_addr, N):
    f = open(input_addr,"r")
    n = int(f.readline())
    lines = [f.readline().strip() for i in range(n)]
    regex = re.compile(r"(?:http(s)?):\/\/(?:(ww(w|2))\.)?([\w\.]*\.[\w\.]*)")
    results = []
    for line in lines:
        match = re.search(regex, line)
        if(match):
            results.append(match.groups()[-1])
    results = list(set(results))
    results.sort()
    r_str = ';'.join(results)
    f.close()
    f = open(output_addr,"r")
    expected = f.readlines()[0]
    if(r_str==expected):
        print(f'{N}: VALID')
    else:
        print(f'{N}: INVALID\nEXPECTED:\t{expected.split(";")}\nGOT:\t\t{r_str.split(";")}')
    f.close()
current_path = str(pathlib.Path(__file__).parent.resolve())
for i in range(1):
    detect_the_domain_name(current_path + f"/input0{i}.txt", current_path + f"/output0{i}.txt",i)