f=open('inputfile.txt')
i=0
time=[]
distance=[]
for line in f:
    if i==0:
        temp=line.split(':')[1].split()
        for i in range(len(temp)):
            time.append(int(temp[i]))
    else:
        temp=line.split(':')[1].split()
        temp=line.split(':')[1].split()
        for i in range(len(temp)):
            distance.append(int(temp[i]))
    i+=1
ans = 1
for i in range(len(time)):
    low = 0
    high = time[i] // 2
    if high * (time[i] - high) <= distance[i]:
        temp=0
    else:
        while low + 1 < high:
            m = (low + high) // 2
            if m*(time[i]-m) > distance[i]:
                high = m
            else:
                low = m
        first = high
        last = int((time[i] / 2) + (time[i] / 2 - first))
        temp=last-first+1 
    ans*=temp
print("Answer is:",ans)