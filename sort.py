
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


a =[55,32,3435,767,1,31]
insert_sort(a)
print(a)

