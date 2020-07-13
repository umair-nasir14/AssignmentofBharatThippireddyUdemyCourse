import re

str = 'I am 20-11-2020 completing a 100 day coding challenge. I 200 have to go 3-6-1990 about one day at a time'

result = re.search(r'c\w\w',str)
print(result.group())

result = re.findall(r'o\w\w',str)
print(result)

result = re.match(r'I\s\w',str)
print(result.group())

result = re.split(r'\d+',str)
print(result)

result = re.sub(r'one','two',str)
print(result)

result = re.findall(r'o\w*',str) #+ for 1 or more iteration, * for ) or more, ? for 0 or 1, {m} for m repetitions and {m,n} min minimum and n max number of iterations  
print(result)

result = re.findall(r'\d{1,2}-\d{1,2}-\d{4}',str)
print(result)

result = re.search(r'^I\w*',str)
print(result.group())