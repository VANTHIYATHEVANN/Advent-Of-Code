f=open('inputfile.txt')
su = 0
dic={}
i=0
for line in f:
    if i not in dic:
        dic[i]=0
    dic[i]+=1
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
    for j in range(count):
        if i+j+1 not in dic:
            dic[i+j+1]=0
        dic[i+j+1]+=dic[i]
    i+=1
print("Part 1:",su)
s=0
for key in dic.keys():
    s+=dic[key]
print("Part 2:",s)
