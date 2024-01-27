f=open('inputfile.txt')
su = 0
N = {}
i=0
for line in f:
    matches = line.split('|')
    first_match=matches[0].split(':')
    first = [int(x) for x in first_match[1].split()]
    second = [int(x) for x in matches[1].split()]
    count=0
    common=[]
    for num in first:
        if num in second and num not in common:
            common.append(num)
    count = len(common)
    if count > 0:
        su += 2**(count-1)
print(su)