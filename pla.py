ssize = 0
n = 0
k = 0
result = 0
nth = 0
n = int(input())
stos = [0] * n
for i in range(n):
    nth, k = [int(x) for x in input().split()] 
    while ssize > 0 and stos[ssize-1] > k: ssize = ssize - 1
    if ssize == 0 or stos[ssize-1] < k:
        result = result + 1
        stos[ssize] = k
        ssize = ssize + 1
print(result)
