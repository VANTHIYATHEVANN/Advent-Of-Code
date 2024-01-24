f=open('inputfile.txt')
games = {}
for line in f:
    gp, sp = line.split(": ")
    gid = int(gp.split(" ")[1])
    data=[]        
    for val in sp.split('; '):
        dic={}
        for color in val.split(', '):
            dic[color.split(' ')[1]]=int(color.split(' ')[0])
        data.append(dic)
    games[gid] = data
max_red, max_green, max_blue = 12, 13, 14
su=0
for id in games.keys():
    flag=True
    for rd in games[id]:
        if ((rd.get('red')!=None and rd.get('red')>max_red) 
        or (rd.get('blue')!=None and rd.get('blue')>max_blue) 
        or (rd.get('green')!=None and rd.get('green')>max_green)):
            flag=False
    if flag:
        su+=int(id)
print("Sum is:", su)