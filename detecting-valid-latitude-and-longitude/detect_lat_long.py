#TODO:NOT_SOLVED
import re,pathlib
def detect_the_domain_name(input_addr, output_addr, N):
    f = open(input_addr,"r")
    n = int(f.readline())
    lines = [f.readline().strip() for i in range(n)]
    regex = re.compile(r"\(\+?\-?(90(\.0+)?|[1-8]\d(\.\d+)?|\d(\.\d+)?), (\+?\-?(180(\.0+)?|1[1-7]\d(\.\d+)?|\d{1,2}(\.\d+)?))\)")
    results = []
    for line in lines:
        match = re.search(regex, line)
        if(match):
            print('Valid')
        else:
            print('Invalid')
    # f.close()
    # f = open(output_addr,"r")
    # expected = f.readlines()[0]
    # if(r_str==expected):
    #     print(f'{N}: VALID')
    # else:
    #     print(f'{N}: INVALID\nEXPECTED:\t{expected}\nGOT:\t\t{r_str}')
    # f.close()
current_path = str(pathlib.Path(__file__).parent.resolve())
for i in range(1):
    detect_the_domain_name(current_path + f"/input0{i}.txt", current_path + f"/output0{i}.txt",i)