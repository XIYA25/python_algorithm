def count_sorted(li, max_count=100):
    count = [0 for _ in range(max_count+1)]         #创建一个长度为max+1的列表，里面的值无论遍历多少次（_）都是0
    for val in li:
        count[val] += 1
    li.clear()
    for ind, val in enumerate(count):
        for i in range(val):
            li.append(ind)



import random
li = [random.randint(0, 100) for _ in range(1000)]
print(li)
count_sorted(li)
print(li)