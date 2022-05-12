import  random

def bubble_sort(li):
    for i in range (len(li)-1):
        print('i is ',i )
        for j in range (len(li) - i - 1):
            print(' j is ',j)
            if li[j] > li[j + 1]:
                li[j], li[j + 1] = li[j + 1], li[j]
                print('running:', li)


# li = [random.randint(0, 10000) for i in  range(100)]
li = [6, 1, 8, 5, 7, 4, 2, 9, 3]
print('before:', li)
bubble_sort(li)
print('after:', li)