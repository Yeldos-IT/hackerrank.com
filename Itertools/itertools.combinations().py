from itertools import combinations
(s, k) = input().split()

for i in range(1, int(k)+1):
    [print(''.join(com)) for com in combinations(sorted(list(s)), i)]
