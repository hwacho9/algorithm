# Two Pointers


def reverseVowels(s: str) -> str:
    vowels = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]

    s = list(s)

    left = 0
    right = len(s) - 1

    while left < right:
        if s[left] in vowels and s[right] in vowels:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1

        elif s[left] not in vowels:
            left += 1

        else:
            right -= 1

    return "".join(s)


print(reverseVowels("hello"))

# for i in "hello":
#     if i == "e":
#         print(i)

# a = list("Hello")
# a.reverse()
# print(a)
