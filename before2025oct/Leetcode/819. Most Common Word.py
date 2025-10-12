import collections
import re


def mostCommonWord(paragraph: str, banned: [str]) -> str:
    words = [
        word
        for word in re.sub("[^\w]", " ", paragraph).lower().split()
        if word not in banned
    ]

    print(words)

    # counts = collections.defaultdict(int)
    # for word in words:
    #     counts[word] += 1
    # print(counts)

    counter = collections.Counter(words)
    print(counter.most_common(1)[0][0])


mostCommonWord(
    paragraph="Bob hit a ball, the hit BALL flew far after it was hit.", banned=["hit"]
)
