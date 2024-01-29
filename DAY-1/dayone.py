f=open("calibration.txt","r")
su=0
dic={'one':1,'two':2,'three':3,'four':4,'five':5,'six':6,'seven':7,'eight':8,'nine':9}
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
    #print(curr)
    su+=curr
print("Part 1:",su)
f=open("calibration.txt","r")
s=0
for line in f:
    p2_digits = []
    for i in range(len(line)):
        ch = line[i]
        if ch.isdigit():
            p2_digits+=ch
        for d in range(len(['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine'])):
            val = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine'][d]
            if line[i:].startswith(val):
                p2_digits+=str(d + 1)
    s += int(p2_digits[0] + p2_digits[-1])

print("Part 2:",s)
