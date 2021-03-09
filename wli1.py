def prime(n):
    if(n < 2): return 0
    if(n == 2): return 1
    for i in range(2, int(n**0.5)+1):
        if n%i == 0: return 0
    return 1

c = 0
maxi = 99
mini = 100001
for i in range(5000):
    tmp = int(input())
    if(prime(tmp) == 1):
        c = c+1
        if(maxi < tmp): maxi = tmp
        if(mini > tmp): mini = tmp
print(c)
print(maxi)
print(mini)
