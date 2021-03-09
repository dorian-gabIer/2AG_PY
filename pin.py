a = int(input())
x = input()
x = x.replace(' ', '')
c = 0
maxi = 0
for i in x:
    if i == '1': c = c+1
    else:
        if(maxi < c): maxi = c
        c = 0
if(maxi < c): maxi = c
print(maxi)
