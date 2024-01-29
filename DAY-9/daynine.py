def ep1(array):
    if array.count(0)==len(array):
        return 0
    deltas = []
    for i in range(len(array) - 1):
        x = array[i]
        y = array[i + 1]
        deltas.append(y-x)
    diff = ep1(deltas)
    return array[-1] + diff
def ep2(array):
    if array.count(0)==len(array):
        return 0
    deltas = []
    for i in range(len(array) - 1):
        x = array[i]
        y = array[i + 1]
        deltas.append(y-x)
    diff = ep2(deltas)
    return array[0] - diff

total1=0
total2=0
f=open('inputfile.txt')
for line in f:
    line=line.split()
    arr=[]
    for n in line:
        arr.append(int(n))
    total1+=ep1(arr)
    total2+=ep2(arr)
print("Part 1:",total1)
print("Part 2:",total2)