f=open("calibration.txt","r")
su=0
for line in f:
    first_d=''
    second_d=''
    for ch in line:
        if ch.isdigit() and first_d=='':
            first_d=ch
        elif ch.isdigit() and not(first_d==''):
            second_d=ch
    if second_d=='':
        curr=int(first_d+first_d)
    else:
        curr=int(first_d+second_d)
    print(curr)
    su+=curr
print(su)