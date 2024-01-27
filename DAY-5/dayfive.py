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
min=100000
for seed in seeds:
    loc=seed
    for val in all_maps:
        for destination, source, rangelen in val:
            if source <= loc < source + rangelen:
                loc = destination + (loc - source)
                break
    if loc<min:
        min=loc
print(min)