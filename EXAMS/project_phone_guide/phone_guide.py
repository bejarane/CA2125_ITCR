import re

filename = "requirements.txt"

filedata= open(filename,'r')

datalines = filedata.readlines()

captureddata = []

for line in datalines:
    captureddata += re.findall("\d{4}-?\d{4}",line)
    captureddata += re.findall("[^\(\-\d](\d{3})[^\)\-\d]",line)

print("Results")
for number in captureddata:
    print(number)
print()
total = len(captureddata)
print(f'Total phone numbers found: {total}')
    
