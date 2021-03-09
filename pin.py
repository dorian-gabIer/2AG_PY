a = int(input())
x = list(map(int, input().split()))
c = 0
maxi = 0
for tmp in x: 
    if tmp == 1: c = c+1
    else:
        if(maxi < c): maxi = c
        c = 0
if(maxi < c): maxi = c
print(maxi)
