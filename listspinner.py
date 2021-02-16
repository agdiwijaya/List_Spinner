List_awal = [[1, 2, 3, 4],
[5, 6, 7, 8],
[9, 10, 11, 12],
[13, 14, 15, 16]]

def counterClockwise(List_awal, N):
    result = [i[N] for i in List_awal]
    return result

     
# Use the Function
A = (counterClockwise(List_awal, 3)) , (counterClockwise(List_awal, 2)) , (counterClockwise(List_awal, 1)) , (counterClockwise(List_awal, 0))
Alist = list(A)
print(Alist)

