def kidsWithCandies(candies: list[int], extraCandies: int) -> list[bool]:
    ans = []
    for i in candies:
        ans.append(i + extraCandies >= max(candies))

    return ans


print(kidsWithCandies([2, 3, 5, 1, 3], 3))
