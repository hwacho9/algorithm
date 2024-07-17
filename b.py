# Enter your code here. Read input from STDIN. Print output to STDOUT

import sys

input_csv = sys.stdin

sums = None

for i, line in enumerate(input_csv):
    # 一列は文字列ですので出力する
    if i == 0:
        sys.stdout.write(line)
        continue

    numbers = list(map(int, line.split(",")))

    if sums is None:
        sums = [0] * len(numbers)

    for i, number in enumerate(numbers):
        sums[i] += number

averages = [round(i / len(sums)) for i in sums]

sys.stdout.write(",".join(map(str, averages)))
