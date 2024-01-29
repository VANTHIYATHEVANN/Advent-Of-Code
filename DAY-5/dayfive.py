import math
f=open('inputfile.txt')
almanac=[]
for line in f:
    almanac.append(line.strip())
seeds = list(map(int, almanac[0].split(" ")[1:]))
all_maps = []
process_line = False
def func(temp):
    temp = line.split()
    destination = int(temp[0])
    source = int(temp[1])
    rangelen = int(temp[2])
    return((destination, source, rangelen))
for line in almanac[2:]:
    if process_line:
        if line == "":
            process_line = False
        else:
            all_maps[-1].append(func(line))
    else:
        if line != "" and 'map' not in line:
            all_maps.append([])
            temp = line.split()
            all_maps[-1].append(func(line))
            process_line = True
mi=1000000000000000000000
for seed in seeds:
    loc=seed
    for val in all_maps:
        for destination, source, rangelen in val:
            if source <= loc < source + rangelen:
                loc = destination + (loc - source)
                break
    if loc<mi:
        mi=loc
print("Part 1:",mi)

file_content = open('inputfile.txt').read()
sections = file_content.split("\n\n")
inputs = sections[0]
blocks = sections[1:]
inputs = list(map(int, inputs.split(":")[1].split()))
seeds = []
for i in range(0, len(inputs), 2):
    seeds.append((inputs[i], inputs[i] + inputs[i + 1]))
for block in blocks:
    ranges = []
    for line in block.splitlines()[1:]:
        temp=[]
        for num in line.split():
            temp.append(int(num))
        ranges.append(temp)
    new_seeds = []
    while len(seeds) > 0:
        s, e = seeds.pop()      
        for a, b, c in ranges:
            os = max(s, b)
            oe = min(e, b + c)
            if os < oe:
                new_seeds.append((os - b + a, oe - b + a))
                if os > s:
                    seeds.append((s, os))
                if e > oe:
                    seeds.append((oe, e))
                break
        else:
            new_seeds.append((s, e))
    seeds = new_seeds
print("Part 2:",min(seeds)[0])
