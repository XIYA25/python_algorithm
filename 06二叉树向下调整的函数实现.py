def sift(li, low, high):        #low 堆的节点位置     high 堆的最后一个元素
    i = low                     #i最开始指向根节点
    j = 2 * i + 1               #j开始时左孩子
    tmp = li[low]               #把堆的顶存起来
    while  j <= high:           #循环极限 如果j > high， 则j越界
        if li[j + 1] > li[j] and j + 1<= high:   #判断右边孩子是不是比左边大, 且至必须有一个右孩子
            j = j + 1           #如果是就把指针指向右孩子
        if li [j] > tmp:
            li[i] = li[j]
            i = j               #i往下去一层
            j = 2 * i + 1       #j往下去一层
        else:                   #tmp更大，把tmp放在i的位置上
            li[i] = tmp         #把tmp放到某一级的领导位置上
            break
    else:
        li[i] = tmp             # 把tmp放到叶子节点上


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


li =[i for i in range(100)]
import random
random.shuffle(li)
print(li)

heap_sort(li)
print(li)