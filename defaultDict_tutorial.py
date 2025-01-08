from collections import defaultdict

n, m = map(int, input().split())
group_A = defaultdict(list)

for i in range(1, n + 1):
    word = input()
    group_A[word].append(i)

for _ in range(m):
    word = input()
    if word in group_A:
        print(' '.join(map(str, group_A[word])))
    else:
        print(-1)
