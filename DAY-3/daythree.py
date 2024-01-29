f=open('inputfile.txt')
gears=[]
for line in f:
    temp=[]
    for char in line:
        temp.append(char)
    gears.append(temp)
rows_no=len(gears)
cols_no=len(gears[0])
#print(rows_no,' ',cols_no)
su=0
coll={}
row_adj=[-1,0,1]
col_adj=[-1,0,1]
for row in range(len(gears)):
    gear=set()
    curr=0
    flag=False
    ne=False
    for col in range(len(gears[row])):
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
            #ne=False
            if ne:
                curr*=-1
            for val in gear:
                if val not in coll:
                    coll[val] = []
                coll[val].append(curr)
            if flag:
                su+=curr
            curr=0 
            flag=False
            ne=False
            gear=set()
        else:
            ne=False
        if col<cols_no and gears[row][col]=='-':
            ne=True
print("Part 1",su)
s=0 
for key in coll.keys():
    if len(coll[key])==2:
        s+=key[0]*key[1]
print("Part 2",s)
            
            
