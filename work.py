dimension = int(input())
array = [float(a) for a in input().split()]
zero = 0
for a in range(1, dimension):
    if (array[a] >= array[zero]):
        zero = a
for a in range (zero + 1, dimension):
    array[a] = 0
print(array)