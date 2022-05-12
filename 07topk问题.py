'''
堆排序--topk问题
'''
'''
·现在有N个数， 设计算法得到前K大的数。（k<n）
解决思路：
-排序后切片 O（nlog）
-排序LowB三人组 O（mn）
-堆排序
    ·取列表前K个元素建立一个小根堆。堆顶就是目前第K大的数
    ·一次向后遍历源列表，对于列表中的元素，并且对堆进行一次调整；
    ·遍历列表所有元素后，倒叙弹出堆顶
'''

def sift(li, low, high):
    i = low
    j = 2 * i + 1
    tmp = li[low]
    while  j <= high:
        if j + 1<= high and li[j + 1] < li[j]:   #li[j + 1] < li[j]
            j = j + 1
        if li [j] < tmp:                         #li [j] < tmp
            li[i] = li[j]
            i = j
            j = 2 * i + 1
        else:
            li[i] = tmp
            break
    else:
        li[i] = tmp


def topk(li, k):
    heap = li[0:k]
    for i  in range((k-2)//2, -1, -1):
        sift(heap, i, k-1)
        #1.建堆
        for i in range(k,len(li)):
            if li[i] > heap[0]:
                heap[0] = li[i]
                sift(heap, 0, k-1)
        #2.遍历
        for i in range(k-1, -1, -1):
            heap[0], heap[i] = heap[i], heap[0],
            sift(heap, 0, i-1)
        #3.出数
        return heap

import random
li = list(range(1000))
random.shuffle(li)

print(topk(li, 10))


def heap_sort(li):              #堆排序
        n = len(li)
        for i in range((n-2)//2, -1, -1):
            # i表示建堆的时候调整的部分的根的下标
            sift(li, i, n-1)
            #建堆完成
        for i in range(n-1, -1, -1):
            # i 指向当前堆的最后一个元素
            li[0],li[i] = li[i], li[0]
            sift(li, 0, i -1)   #i-1是新的high
