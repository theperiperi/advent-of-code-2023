input = open("C:\\Users\\pri\\Desktop\\sample.txt").read().strip()
lines = input.splitlines()
rows = [list(map(int, line.split())) for line in lines]

part1 = 0
part2 = 0

for i,_ in enumerate(rows):
    new_last_num = rows[i][len(rows[i])-1]
    all_first_nums = [rows[i][0]]
    while True:
        new_row = []
        all_zero = True
        for j in range(1, len(rows[i])):
            diff = rows[i][j] - rows[i][j-1]
            new_row.append(diff)
            if diff != 0:
                all_zero = False

        all_first_nums.append(new_row[0])
        new_last_num += new_row[len(new_row)-1]
        rows[i] = new_row

        if all_zero:
            break

    part1 += new_last_num

    while len(all_first_nums) > 1:
        two = all_first_nums.pop()
        one = all_first_nums.pop()
        all_first_nums.append(one - two)

    part2 += all_first_nums[0]

print(part1)
print(part2)