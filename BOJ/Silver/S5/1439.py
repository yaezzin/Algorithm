import re

str = input()
pattern = r'0+|1+'

result = re.findall(pattern, str)

count_0 = sum(1 for i in result if '0' in i)
count_1 = sum(1 for i in result if '1' in i)

print(min(count_0, count_1))