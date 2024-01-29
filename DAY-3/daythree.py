lines = open('inputfile.txt').read().splitlines()
cs = set()
for r in range(len(lines)):
    for c in range(len(lines[r])):
        if lines[r][c].isdigit() or lines[r][c]=='.':
            continue
        for cr in range(r-1,r+2):
            for cd in range(c-1,c+2):
                if cr < 0 or cr >= len(lines) or cd < 0 or cd >= len(lines[cr]) or not lines[cr][cd].isdigit():
                    continue
                while cd > 0 and lines[cr][cd - 1].isdigit():
                    cd -= 1
                cs.add((cr, cd))
ns = []
for r, c in cs:
    s = ""
    while c < len(lines[r]) and lines[r][c].isdigit():
        s += lines[r][c]
        c += 1
    ns.append(int(s))
tot1=0
for val in ns:
    tot1+=val
print("Part 1:",tot1)
tot2=0
for r in range(len(lines)):
    for c in range(len(lines[r])):
        if lines[r][c] != "*":
            continue

        cs = set()
        
        for cr in [r - 1, r, r + 1]:
            for cc in [c - 1, c, c + 1]:
                if cr < 0 or cr >= len(lines) or cc < 0 or cc >= len(lines[cr]) or not lines[cr][cc].isdigit():
                    continue
                while cc > 0 and lines[cr][cc - 1].isdigit():
                    cc -= 1
                cs.add((cr, cc))
                
        if len(cs) != 2:
            continue

        ns = []

        for cr, cc in cs:
            s = ""
            while cc < len(lines[cr]) and lines[cr][cc].isdigit():
                s += lines[cr][cc]
                cc += 1
            ns.append(int(s))
        
        tot2 += ns[0] * ns[1]

print("Part 2:",tot2)
