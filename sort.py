
def bubble_sort(alist):
    n = len(alist)
    for j in range(n-1):
        count = 0
        for i in range(n-1-j):
            if alist[i] > alist[i+1]:
                alist[i],alist[i+1] = alist[i+1],alist[i]
                count += 1
        if count == 0:
            return

def select_sort(alist):
    n = len(alist)
    for j in range(n-1):
        min_index = j
        for i in range(j+1,n):
            if alist[min_index] > alist[i]:
                min_index = i
        alist[j],alist[min_index] = alist[min_index], alist[j]

def insert_sort(alist):
    n = len(alist)
    for j in range(1,n):
        cur_index = j
        while cur_index > 0:
            if alist[cur_index] < alist[cur_index-1]:
                alist[cur_index],alist[cur_index-1] = alist[cur_index-1],alist[cur_index]
                cur_index -= 1
            else:
                break


def quick_sort(alist,first,last):
    mid_value = alist[first]
    low = first
    high = last
    if first >= last:
        return
    while low < high:
        while low < high and alist[high] >= mid_value:
            high -= 1
        alist[low] = alist[high]
        while low < high and alist[low] < mid_value:
            low += 1
        alist[high] = alist[low]
    alist[low] = mid_value
    quick_sort(alist, first, low-1)
    quick_sort(alist, low+1, last)



a =[55,32,3435,767,1,31]
quick_sort(a,0,len(a)-1)
print(a)

