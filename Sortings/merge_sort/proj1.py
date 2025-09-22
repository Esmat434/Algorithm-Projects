from random import randint as rnd
def combine(lst1,lst2):
    new_lst=[]
    len1 = len(lst1)
    len2 = len(lst2)
    index1=0
    index2=0
    while index1<len1 and index2<len2:
        if lst1[index1]<lst2[index2]:
            new_lst.append(lst1[index1])
            index1+=1
        else:
            new_lst.append(lst2[index2])
            index2+=1
    new_lst+=lst1[index1:]
    new_lst+=lst2[index2:]
    return new_lst

def merge_sort(lst):
    if len(lst) == 1:
        return lst
    else:
        mid = len(lst)//2
        left = lst[:mid]
        right = lst[mid:]
    
    left = merge_sort(left)
    right = merge_sort(right)

    return combine(left, right)

length = 10
lst = [rnd(0,10) for _ in range(10)]
print(lst)
print(merge_sort(lst))