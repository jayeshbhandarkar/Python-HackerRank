n, x = map(int, input().split())

totals = [0] * n

for _ in range(x):
    marks = list(map(float, input().split()))
    for i in range(n):
        totals[i] += marks[i]

for total in totals:
    print(f"{total / x:.1f}")
