n = int(input())

country_stamps = set()

for _ in range(n):
    country = input().strip()
    country_stamps.add(country)

print(len(country_stamps))
