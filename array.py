import random


def pl(t):
    for i in t:
        print(*i)


x = int(input())
y = int(input())


l1 = [[0 for j in range(y)] for i in range(x)]
l2 = [[0 for j in range(y)] for i in range(x)]
l3 = [[0 for j in range(y)] for i in range(x)]


for i in range(y):
    for j in range(x):
        l1[i][j] = random.randrange(-100, 100)
        l2[i][j] = random.randrange(-100, 100)
        l3[i][j] = l1[i][j] + l2[i][j]


print('matrix_1 = ')
pl(l1)
print('matrix_2 = ')
pl(l2)
print('sum = ')
pl(l3)


