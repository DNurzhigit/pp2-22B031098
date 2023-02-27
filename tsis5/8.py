import re

s = "HowAreYou"

result = re.findall(r'[A-Z][^A-Z]*', s)
print(result)
