f=open('inputfile.txt')
soi=0
sop=0
mav={'red':12,'green':13,'blue':14}
for line in f:
    flag = True
    line = line.split(':')
    idd=line[0]
    line=line[1]
    dic = {}
    for cube in line.split(';'):
        for b in cube.split(','):
            b = b.split()
            n=b[0]
            c=b[1]
            n = int(n)
            if c not in dic:
                dic[c]=0
            dic[c] = max(dic[c], n)
            if int(n) > {'red': 12, 'green': 13, 'blue': 14}.get(c, 0):
                flag = False
            if c not in mav:
                c=0
            else:
                va=mav[c]
                if int(n)>va:
                    flag=False
                
    count = 1
    for val in dic.values():
        count *= val
    sop += count
    if flag:
        soi += int(idd.split()[-1])
print("Part 1:",soi)
print("Part 2:",sop)
