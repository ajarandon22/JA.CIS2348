# Jarandon Adams - 1812590

numbers_list = input().split()
Output = []

for num in numbers_list:
    num = int(num)

    if num > 0:
        Output.append(num)

Output.sort()

for num in Output:
    print(num, end=' ')
