from sys import stdin

n = int(stdin.readline())

for _ in range(n):
    num = int(stdin.readline())

    # Convert the number to binary
    # [2:] is used to remove the '0b' prefix
    binary = bin(num)[2:]

    # Reverse the binary number and print the index of '1'
    for i in range(len(binary)):
        if binary[::-1][i] == "1":
            print(i, end=" ")
