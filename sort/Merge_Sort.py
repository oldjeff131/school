import random
import time
def merge(left, right):
    result = []
    while len(left) and len(right):
        if (left[0] < right[0]):#判斷哪個比較小，小的放入result的list的第一位
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))
    result = result+left if len(left) else result+right #排入result的list 如果已經放入左方數值 則放入右方數字
    return result

def mergeSort(array):
    if len(array) < 2:#當array小於2時直接跳出
        return array
    mid = len(array)//2 #取得list長度中間值
    leftArray = array[:mid]#取得左邊arr的所有數值
    rightArray = array[mid:]#取得右邊arr的所有數值
    return merge(mergeSort(leftArray),mergeSort(rightArray))#切到左右邊個只剩下一個數值

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
print("合併排序後:")
for i in range(n): #排序後的顯示
    if i<n-1:
        print("%s" % arr[i],end=' ')
    else:
        print("%s\n" % arr[i])

print("合併排序總使用時間:")
end = time.perf_counter()#結束時間
print(end - start)