f=open('inputfile.txt')
gears=[]
for line in f:
    temp=[]
    for char in line:
        temp.append(char)
    gears.append(temp)
rows_no=len(gears)
cols_no=len(gears[0])
print(rows_no,' ',cols_no)
p1=0
coll={}
row_adj=[-1,0,1]
col_adj=[-1,0,1]
for row in range(len(gears)):
    gear=set()
    curr=0
    flag=False
    for col in range(len(gears[row])+1):
        if col<cols_no and gears[row][col].isdigit():
            curr=curr*10+int(gears[row][col])
            for ra in row_adj:
                for ca in col_adj:
                    if 0<=row+ra<rows_no and 0<=col+ca<cols_no:
                        char=gears[row+ra][col+ca]
                        if not char.isdigit() and char!='.':
                            flag=True
                        if char=='*':
                            gear.add((row+ra, col+ca))
        elif curr>0:
            for val in gear:
                if val not in coll:
                    coll[val] = []
                coll[val].append(curr)
            if flag:
                p1+=curr
            curr=0 
            flag=False
            gear=set()
print(p1)
p2=0 
for key in coll.keys():
    if len(coll[key])==2:
        p2+=key[0]*key[1]
print(p2)
            
            
