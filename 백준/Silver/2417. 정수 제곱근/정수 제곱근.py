n = int(input())

q = 0
t = n

while q <= t:
    mid = (q + t) // 2
    if mid ** 2 < n:
        q = mid + 1
    else:
        t = mid - 1

print(q)