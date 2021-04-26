import re

filename = "requirements.txt"

filedata= open(filename,'r')

datalines = filedata.readlines()

filedata.close()

captureddata = []

for line in datalines:
    captureddata += re.findall("\d{4}-?\d{4}",line)
    captureddata += re.findall("[^\(\-\d](\d{3})[^\)\-\d]",line)

print("Results")
fileoutput = open("output.txt",'w+')
for number in captureddata:
    fileoutput.write(number)
    fileoutput.write("\n")
    print(number)
print()
total = len(captureddata)
print(f'Total phone numbers found: {total}')
    
fileoutput.close()
