'''
Merge：
    2 5 7 8 9 | 1 3 4 6
    ↑           ↑
li = 1 2

    5 7 8 9 |  3 4 6
    ↑          ↑
li = 1 2 3

    5 7 8 9 |  4 6
    ↑          ↑
li = 1 2 3 4 5

    7 8 9 |  6
    ↑        ↑
li = 1 2 3 4 5 6 7······

'''

def merge(li, low, mid, high):
    i = low
    j = mid + 1
    ltmp = []                                #拿出来的数
    while i <= mid and j <=high:            #只要左右两边都有数
        if li[i] < li[j]:
            ltmp.append(li[i])
            i += 1
        else:
            ltmp.append(li[j])
            j += 1
    #while 执行完，肯定有一部分没有数了
    while i <= mid:
        ltmp.append(li[i])
        i += 1
    while j <=high:
        ltmp.append(li[j])
        j += 1
        li[low:high+1] = ltmp

# li = [2, 4, 5, 7, 1, 3, 6, 8]               #low 和 high必须先排好序
# merge(li, 0, 3, 7)
# print(li)


'''
                    [10 4 6 3 8 2 5 7]                  ← 分解merge
            [10 4 6 3]               [8 2 5 7]
        [10 4]      [6 3]         [8 2]      [5 7]
   [10]   [4]    [6]     [3]    [8]   [2]  [5]   [7]
        [4 10]      [3 6]         [2 8]      [5 7]      ← 合并sort
            [3 4 6 10]                [2 5 7 8]
                    [2 3 4 5 6 7 8 10]
'''

def merge_sort(li, low, high):
    if low < high:      #至少有两个元素
        mid = (low + high)//2
        merge_sort(li, low, mid)
        merge_sort(li, mid+1, high)
        merge(li, low, mid, high)

# li = list(range(1000))
# import random
# random.shuffle(li)
# li = [7, 8, 2, 3, 4, 10, 6, 0, 1, 11, 5, 9, 13, 12]
# print(li)
# merge_sort(li, 0, len(li)-1)
# print(li)
#
# def merge_sort_test(li, low, high):
#     if low < high:      #至少有两个元素
#         mid = (low + high)//2
#         merge_sort(li, low, mid)
#         merge_sort(li, mid+1, high)
#         print(li[low:high+1])
#
# li = list(range(16))
# import random
# random.shuffle(li)
# print(li)
# merge_sort_test(li, 0, len(li)-1)
# print(li)
