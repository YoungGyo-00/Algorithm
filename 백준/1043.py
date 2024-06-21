n, m = map(int, input().split())
persons = set(input().split()[1:])
parties = []

for _ in range(m):
    parties.append(set(input().split()[1:]))

for _ in range(m):
    for party in parties:
        if party & persons:
            persons = persons.union(party)

cnt = 0
for party in parties:
    if party & persons:
        continue
    cnt += 1

print(cnt)
