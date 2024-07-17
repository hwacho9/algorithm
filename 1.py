def max_square(segments):
    segments.sort(reverse=True)
    for i in range(len(segments)):
        if sum(segments[i:]) >= segments[i] * 4:
            return segments[i]
    return 0


print(max_square([3, 3, 3, 2, 1, 1]))  # Output: 3
print(max_square([2, 2, 2, 2, 2, 10, 10, 10]))  # Output: 10
print(max_square([5, 4, 3, 2, 1, 10]))  # Output: 0
