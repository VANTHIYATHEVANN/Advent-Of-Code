from math import gcd
with open('inputfile.txt', 'r') as file:
    lines = file.read().splitlines()
steps = None
rest = []
for i in range(len(lines)):
    if i == 0:
        steps = lines[i]
    elif i == 1:
        continue
    else:
        rest.append(lines[i])
network = {}
for l in rest:
    l = l.split(" = ")
    p=l[0]
    tar=l[1]
    network[p] = tar[1:-1].split(", ")
count = 0
curr = "AAA"
while curr != "ZZZ":
    count += 1
    curr = network[curr][0 if steps[0] == "L" else 1]
    steps = steps[1:] + steps[0]
print("Part 1:",count)

pl=[]
for k in network:
    if k.endswith('A'):
        pl.append(k)
cycles = []

for curr in pl:
    cycle = []
    curr_steps = steps
    count = 0
    first_z = None
    while True:
        while count == 0 or not curr.endswith("Z"):
            count += 1
            curr = network[curr][0 if curr_steps[0] == "L" else 1]
            curr_steps = curr_steps[1:] + curr_steps[0]
        cycle.append(count)
        if first_z is None:
            first_z = curr
            count = 0
        elif curr == first_z:
            break
    cycles.append(cycle)
nums=[]
for cycle in cycles:
    nums.append(cycle[0])
lcm = nums[0]

for num in nums:
    lcm = lcm * num // gcd(lcm, num)
print("Part 2:",lcm)
