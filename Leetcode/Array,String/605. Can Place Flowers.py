def canPlaceFlowers(flowerbed: list[int], n: int) -> bool:
    if flowerbed[n - 1] == 1 or flowerbed[n + 1] == 1:
        return True
    else:
        return False


print(canPlaceFlowers([1, 0, 0, 0, 1], 1))
