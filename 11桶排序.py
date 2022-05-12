'''
在大范围比如从一到一亿的排序中需要用到桶排序
首先把列表li分成个个小段列表（桶）中进行排序
每一个桶有自己的标号且拥有相同的容量
'''

def bucket_sort(li, n=100, max_num=10000):              #n 多少个桶 max——num通的范围
    buckets = [[] for _ in range(n)]                    #创建n个空的桶
    for var in li:                                      #遍历列表里的数
        i = min(var // (max_num //n), n-1)              #i 表示var放到几号桶里，maxnum//n 一个桶里装里装个数， var//...代表分配到几号桶里，min 区分如果出现一万的情况，把一万分配到99号桶里
        buckets[i].append(var)                          #把var放到对应编号i的桶里
        #保持同理的顺序
        for j in range(len(buckets[i])-1, 0,-1):        #在列表元素放入桶中的同时从后往前（遍历）对桶进行排序，j为桶的插入排序标号的指针
            if buckets[i][j] < buckets[i][j-1]:         #判断两个相邻的桶号大小，如果前边的桶号（j-1）小于后面的（j）
                buckets[i][j],buckets[i][j-1] = buckets[i][j-1],buckets[i][j]  #两个通的位置交换
            else:
                break                                   #假如遍历到负数时break
    sorted_li = []                                      #桶的列表（卡车）
    for buc in buckets:                                 #把所有排好序的桶装进buc（集装箱）里
        sorted_li.extend(buc)                           #extend（）在列表后面进行添加，把buc（集装箱）装进依次装进桶的列表（卡车）
    return sorted_li

import random
li = [random.randint(0, 10000) for i in range(100000)]
print(li)
li = bucket_sort(li)
print('\n', li)

