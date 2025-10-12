def reverseWords(s: str) -> str:
    a = s.split()
    a.reverse()
    return " ".join(a)


print(reverseWords("the sky is blue"))
print(reverseWords("  hello world  "))
