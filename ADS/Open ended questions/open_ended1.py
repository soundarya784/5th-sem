def biggest_nos(a):
    a.sort()
    for i in range(len(a) - 2):
        print(a[i])

n = int(input("enter length of the array"))
a = []
for i in range(n):
    a.append(int(input("enter array values:")))

biggest_nos(a)