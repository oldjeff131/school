import random
import time
def partition(arr, low, high):
    i = (low-1)        
    pivot = arr[high] #設定基準點的值
    for j in range(low, high):
        if arr[j] <= pivot:#找尋比基準點小的或相同的值
            i = i+1 
            arr[i], arr[j] = arr[j], arr[i]#兩數值互換
    arr[i+1], arr[high] = arr[high], arr[i+1]#兩數值互換
    return (i+1) #回傳基準點最後交換的位子
 
def quickSort(arr, low, high):#arr陣列,low開始位子,high結束位子
    if len(arr) == 1: #如果arr式的長度為1，直接回傳
        return arr
    if low < high: 
        pi = partition(arr, low, high)
        quickSort(arr, low, pi-1) #處理較小部分的子循環
        quickSort(arr, pi+1, high) #處理較大部分的子循環

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
print("快速排序後:")
for i in range(n): #排序後的顯示
    if i<n-1:
        print("%s" % arr[i],end=' ')
    else:
        print("%s\n" % arr[i])

print("快速排序總使用時間:")
end = time.perf_counter()#結束時間
print(end - start)


	
