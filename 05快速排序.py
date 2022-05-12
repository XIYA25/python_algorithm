def partition(li, left, right):
    tmp = li[left]
    while left < right:
        while left < right and li[right] >= tmp:            #找从右边比tmp小的数
            right -= 1                  #往左走一部
        li[left] = li[right]            #把右边的值写在左边上
        print(li, 'right')
        while left < right and li[left] <= tmp:
            left += 1
        li[right] = li[left]            #把左边的值写在右边上
        print(li, 'left')
    li[left] = tmp                      #把tmp归位
    return left


li = [5, 7, 4, 6, 3, 1, 2, 9, 8]
print(li)
partition(li, 0, len(li) - 1)
print(li)

