import re
s = "oNurzhigitSHdbhbkjSdjkndcjsouHUIUSSJn"

result = re.findall(r'[A-Z][a-z]+' , s)
print(result)