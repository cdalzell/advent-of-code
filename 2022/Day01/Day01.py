elf_calorie_totals = [0]
max_calories = 0
max_calorie_elf = 0

with open("input.txt","r") as input_file:
    for line in input_file:
        calories = line.strip()

        if calories != "":
            elf_calorie_totals[-1] += int(calories)
        else:
            elf_calorie_totals.append(0)

# Part One
for index, total in enumerate(elf_calorie_totals):
    if total > max_calories:
        max_calories = total
        max_calorie_elf = index

print(f"Elf carrying the most calories: {max_calorie_elf+1}")
print(f"Total calories carried: {max_calories}")

# Part Two
top_elf_count = 3
sorted_list = sorted(elf_calorie_totals, reverse=True)  # could also do elf_calorie_totals.sort here to save memory
top_calorie_total = sum(sorted_list[0:top_elf_count])

print(f"Calorie total for the top {top_elf_count} elves: {top_calorie_total}")
