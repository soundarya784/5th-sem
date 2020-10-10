class disjoint:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.rank = [0] * n


    def find(self, a):
        if self.parent[a] != a:
            self.find(self.parent[a])

        return self.parent[a]

    def union(self, xset, yset):
        xset = self.find(xset)
        yset = self.find(yset)

        if xset == yset:
            return

        else:
            if self.rank[xset] > self.rank[yset]:
                self.parent[yset] = xset

            elif self.rank[xset] < self.rank[yset]:
                self.parent[xset] = yset

            elif self.rank[xset] ==  self.rank[yset]:
                self.parent[yset] = xset
                self.rank[xset] += 1
            else:
                return

def count_islands( arr):
    m = len(arr)
    n = len(arr[0])
    dis = disjoint(m*n)
    freq = [0] * m * n

    for i in range(m):
        for j in range(n):
            if arr[i][j] == 0:
                continue

            else:
                if j+1 < m and arr[i][j+1] == 1: #same row right element
                    dis.union(i*m+j, (i*m) + j + 1)
                elif i+1 < n and arr[i+1][j] == 1: #bottom row same element
                    dis.union(i*m+j, (i+1) * m + j)
                elif j+1 < m and i+1 < n and arr[i+1][j+1] == 1: #diagonal right bottom
                    dis.union(i * m + j, (i + 1) * m +(j+1))
                elif i+1 < m and j-1 >= 0 and arr[i+1][j-1] == 1:#diagonal left bottom
                    dis.union(i * m + j, (i + 1) * m + (j - 1))
                elif j-1 >= 0 and arr[i][j-1] == 1:#  left same row
                    dis.union(i * m + j, (i) * m + (j - 1))
                elif i-1 >= 0 and j-1 >= 0 and arr[i-1][j-1] == 1: #diagonal left up
                    dis.union(i * m + j, (i - 1) * m + (j - 1))
                elif i-1 >= 0 and arr[i-1][j] == 1: #same column above row
                    dis.union(i * m + j, (i - 1) * m + (j))
                elif i-1 >= 0 and j+1 < m and arr[i-1][j+1] == 1: #diagonal right up
                    dis.union(i * m + j, (i - 1) * m + (j+1))

    count = 0
    for i in range(m):
        for j in range(n):
            if arr[i][j] == 1:
                x = dis.find(i * m + j)

                if freq[x] == 0:
                    freq[x] += 1
                    count += 1 #increment if parent is not same
                else:
                    freq[x] += 1
    return count


arr = [[1, 1, 0, 0, 0],
     [0, 1, 0, 0, 1],
     [1, 0, 0, 1, 1],
     [0, 0, 0, 0, 0],
     [1, 0, 1, 0, 1]]

number = count_islands(arr)
print("number of islands : " + str(number))












