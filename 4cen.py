s = input()
s2 = ""
n = int(input())
for i in range(len(s)):
    w = ord(s[i])
    s2 += chr(w + n)
s2 = s2[:-1]
print(s2)
