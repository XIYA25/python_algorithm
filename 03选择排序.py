def select_sort_simple(li):
    li_new = []
    for i  in range (len(li)):
        min_val = min(li)
        li_new.append(min_val)
        li.remove(min_val)
        return li_new

def select_sort(li):
    for i in range(len(li) - 1):                #i是第几趟
        min_loc = i                             #最小数出现位置（无序区的第一个位置）
        for j in range(i + 1, len(li)):         #无序区
            if li[j] < li[min_loc]:
                min_loc = j
        li[i], li[min_loc] = li[min_loc] ,li[i] #li[i] 是无序区的第一个位置
        print(li)



li = [3, 6, 9, 5, 4, 7, 8, 1, 2]
print(select_sort(li))
# print(li)