def gcdOfStrings(str1: str, str2: str) -> str:
    str = []

    # print(str1[2:])

    if str1 + str2 != str2 + str1:
        return ""

    # if len(str1) > len(str2):
    #     return self.gcdOfStrings()
    if len(str1) > len(str2):
        return self.gcdOfStrings(str1[len(str2) :], str2)

    if str2 in str1:
        for i in range(len(str2)):
            str.append(str2[i])

        str = list(set(str))
        str = "".join(sorted(str))
    # str = "".join(str)
    return str


print(gcdOfStrings("ABCABC", "ABC"))
print(gcdOfStrings("ABABAB", "ABAB"))
print(gcdOfStrings("ABCDEF", "ABC"))
print(gcdOfStrings("ABC", "ABCABC"))
print(gcdOfStrings("LEET", "CODE"))
