def unique_no(a):
    for i in range(len(a)):
        dict = {}
        val = 0
        for j in str(a[i]):
            if j in dict.keys():
                val = 1
                break
            else:
                dict[j] = 1
        if val == 0:
            print(a[i],end=" ")



n = int(input("enter length of the array"))
a = []
for i in range(n):
    a.append(int(input("enter array values:")))

unique_no(a)