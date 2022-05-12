def insert_sort(li):
    for i  in range(1, len(li)):
        tmp = li[i]
        j = i - 1
        while j >= 0 and li[j] > tmp:
            li[j + 1] = li[j]
            j -= 1
        li[j + 1] = tmp
        print(li)


li = [3, 2, 4, 1, 5, 7, 9, 6, 8]
insert_sort(li)
print(li)