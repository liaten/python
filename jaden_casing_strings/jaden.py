import re
def to_jaden_case(string):
   
    for result in re.finditer(r"(?:(?<! )|(?<!^))[A-Z]", string):
        index = result.start()
        replaced = result[0].lower()
        string = string[:index] + replaced + string[index + 1:]

    for result in re.finditer(r"(?:(?<=[^a-zA-Z'])|(?<=^))(?=([a-z]))(.)", string):
        index = result.start()
        replaced = result[0].upper()
        string = string[:index] + replaced + string[index + 1:]

    return string
print(to_jaden_case("How can mirrors be real if our eyes aren't real?"))
print(to_jaden_case("MOST TREES are blue"))