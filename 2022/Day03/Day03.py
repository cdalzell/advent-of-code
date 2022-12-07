import string

priority_values = {}
letters = string.ascii_lowercase + string.ascii_uppercase
val = 1

for l in letters:
    priority_values[l] = val
    val += 1

rucksacks = []

with open("input.txt", "r") as input_file:
    for line in input_file:
        rucksacks.append(line.strip())

part_one_total = 0
part_two_total = 0

for r in rucksacks:
    total_items = len(r)
    compartment_1, compartment_2 = set(r[0:total_items//2]), set(r[total_items//2:])
    shared_item = list(compartment_1.intersection(compartment_2))[0] # exactly one item type per rucksack
    part_one_total += priority_values[shared_item]

for i in range(0, len(rucksacks), 3):
    r1, r2, r3 = set(rucksacks[i]), set(rucksacks[i+1]), set(rucksacks[i+2])
    badge = list(r1.intersection(r2).intersection(r3))[0]
    part_two_total += priority_values[badge]


print(f"Part One Total: {part_one_total}")
print(f"Part Two Total: {part_two_total}")
