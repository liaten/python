import re
def validate_pin(pin):
    return True if isinstance(re.fullmatch(r"\d{4}|\d{6}", pin), re.Match) else False
print(validate_pin("1234"))
print(validate_pin("12345"))
print(validate_pin("a123"))
print(validate_pin("123456"))