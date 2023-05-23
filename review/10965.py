prime = [2]
for i in range(3, int(10000000 ** 0.5), 2):
    for p in prime:
        if not i % p: break
    else:
        prime.append(i)

ans = []
T = int(input())
for tc in range(1, T + 1):
    A = int(input())
    B = 1
    if A ** 0.5 != int(A ** 0.5):
        for p in prime:
            cnt = 0
            while not A % p:
                A //= p
                cnt += 1
            if cnt % 2:
                B *= p
            if A == 1 or p > A:
                break
        if A > 1:
            B *= A
    ans.append('#{} {}'.format(tc, B))
for n in ans:
    print(n)