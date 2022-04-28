import random
import time
def partition(arr, low, high):
    i = (low-1)        
    pivot = arr[high] 
    for j in range(low, high):
        if arr[j] <= pivot:
            i = i+1
            arr[i], arr[j] = arr[j], arr[i]
 
    arr[i+1], arr[high] = arr[high], arr[i+1]
    return (i+1)
 
def quickSort(arr, low, high):
    if len(arr) == 1: #如果arr式的長度為1，直接回傳
        return arr
    if low < high: 
        pi = partition(arr, low, high)
        quickSort(arr, low, pi-1)
        quickSort(arr, pi+1, high)

start = time.perf_counter()#開始時間
arr = [random.randrange(1,1000) for i in range(1, 1001)] #產生一千筆變數
n = len(arr) #計算arr長度
print("排序前:")
for i in range(n): #排序前的顯示
    if i<n-1:
        print("%s" % arr[i],end=' ')
    else:
        print("%s\n" % arr[i])
quickSort(arr, 0, n-1) #呼叫快速排序
print("快速排列後:")
for i in range(n): #排序後的顯示
    if i<n-1:
        print("%s" % arr[i],end=' ')
    else:
        print("%s\n" % arr[i])

print("This time is being calculated")
end = time.perf_counter()#結束時間
print(end - start)