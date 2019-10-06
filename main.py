inp = open("input.txt", "r")
l1 = []
l2 = []
s = inp.readline()
for i in s:
    if i >= '0' and i <= '9':
        l1.append(int(i))
s = inp.readline()
for i in s:
    if i >= '0' and i <= '9':
        l2.append(int(i))
din = [[]]
din.append([])
if l1[0] == l2[0]:
    din[0].append(1)
else:
    din[0].append(0)
for j in range(1,len(l2)):
    if din[0][j-1] == 1 or l2[j] == l1[0]:
        din[0].append(1)
    else:
        din[0].append(0)
for i in range(1, len(l1)):
    din.append([])
    if l1[i] == l2[0] or din[i-1][0] == 1:
        din[i].append(1)
    else:
        din[i].append(0)
    for j in range(1, len(l2)):
        if l1[i] == l2[j]:
            din[i].append(max(din[i-1][j-1]+1, din[i][j-1]))
        else:
            din[i].append(max(din[i-1][j], din[i][j-1]))
print(l1)
print(l2)
print(din[len(l1)-1][len(l2)-1])