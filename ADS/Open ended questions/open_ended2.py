def unique_no(l,r):
    for i in range(l,r+1):
        dict = {}
        val = 0
        for j in str(i):
            if j in dict.keys():
                val = 1
                break
            else:
                dict[j] = 1
        if val == 0:
            print(i,end=" ")



n = int(input("enter length of the array: "))
l = int(input("enter the value of l: "))
r = int(input("enter the value of r: "))

unique_no(l,r)