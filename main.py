inp = open("input.txt", "r")
l1 = []
l2 = []
din = [[]]
def back(x, y, back_l1, back_l2, back_din, s):
    if x == -1 or y == -1:
        return s
    if back_l1[x] == back_l2[y]:
        s.append(back_l1[x])
        return back(x-1, y-1, back_l1, back_l2, back_din, s)
    if back_din[x-1][y] > back_din[x][y-1]:
        return back(x-1, y, back_l1, back_l2, back_din, s)
    else:
        return back(x, y-1, back_l1, back_l2, back_din, s)
s = inp.readline()
for i in s:
    if i >= '0' and i <= '9':
        l1.append(int(i))
s = inp.readline()
for i in s:
    if i >= '0' and i <= '9':
        l2.append(int(i))
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
ans = back(len(l1)-1, len(l2)-1, l1, l2, din, [])
ans.reverse()
print(l1)
print(l2)
print(din[len(l1)-1][len(l2)-1])
print(ans)