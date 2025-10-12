N = int(input())
numbers = list(map(int, input().split()))

prime = 0
for num in numbers:
    notPrime = 0
    if num > 1:
        for i in range(2, num):
            if num % i == 0:
                notPrime += 1

        if notPrime == 0:
            prime += 1

print(prime)
