import random
import time
def merge(left, right):
    result = []
    while len(left) and len(right):
        if (left[0] < right[0]):
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))
    result = result+left if len(left) else result+right
    return result

def mergeSort(array):
    if len(array) < 2:#當array小於2時直接跳出
        return array
    mid = len(array)//2 #取得list長度中間值
    leftArray = array[:mid]
    rightArray = array[mid:]

    return merge(mergeSort(leftArray),mergeSort(rightArray))

start = time.perf_counter()#開始時間
arr=[random.randrange(1,1000) for i in range(1, 1001)] #產生一千筆變數
n = len(arr) #計算arr長度
print("排序前:")
for i in range(n): #排序前的顯示
    if i<n-1:
        print("%s" % arr[i],end=' ')
    else:
        print("%s\n" % arr[i])
mergeSort(arr)
print("合併排列後:")
for i in range(n): #排序後的顯示
    if i<n-1:
        print("%s" % arr[i],end=' ')
    else:
        print("%s\n" % arr[i])

print("總使用時間:")
end = time.perf_counter()#結束時間
print(end - start)