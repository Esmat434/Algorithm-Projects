from random import randint as rnd

lst = [rnd(0,100) for _ in range(10)]

def bubble_sort(lst):
    comparisons, swaps = 0,0
    for i in range(len(lst)):
        flag = False
        for j in range(len(lst)-1):
            comparisons+=1
            if lst[j]>lst[j+1]:
                lst[j],lst[j+1] = lst[j+1],lst[j]
                swaps+=1
                flag=True
        if not flag:
            break
    return lst, comparisons, swaps

def insertion_sort(lst):
    new_list=[]
    comparisons, swaps = 0,0
    for i in range(len(lst)):
        if not new_list:
            new_list.append(lst[i])
        else:
            for j in range(len(new_list)):
                comparisons+=1
                if new_list[j]>lst[i]:
                    new_list.insert(j,lst[i])
                    swaps+=1
                    break
            else:
                new_list.append(lst[i])
    return new_list, comparisons, swaps

def selection_sort(lst):
    comparisons, swaps = 0,0
    for i in range(len(lst)-1):
        index=i
        for j in range(i+1,len(lst)):
            comparisons+=1
            if lst[index]>lst[j]:
                index=j
        if index != i:
            lst[i],lst[index] = lst[index],lst[i]
            swaps+=1
    return lst, comparisons, swaps

def combine(lst1,lst2):
    comparisons, swaps = 0,0
    new_lst=[]
    len1 = len(lst1)
    len2 = len(lst2)
    index1=0
    index2=0
    while index1<len1 and index2<len2:
        comparisons+=1
        if lst1[index1]<lst2[index2]:
            new_lst.append(lst1[index1])
            index1+=1
            swaps+=1
        else:
            new_lst.append(lst2[index2])
            index2+=1
            swaps+=1
    new_lst+=lst1[index1:]
    new_lst+=lst2[index2:]
    return new_lst, comparisons, swaps

def merge_sort(lst):
    if len(lst) <= 1:
        return lst, 0, 0
    else:
        mid = len(lst)//2
        left = lst[:mid]
        right = lst[mid:]
    
    left, comp_l, swaps_l = merge_sort(left)
    right, comp_r, swaps_r = merge_sort(right)

    merged, comp_m, swaps_m = combine(left, right)

    total_comp = comp_l + comp_r + comp_m
    total_swaps = swaps_l + swaps_r + swaps_m

    return merged, total_comp, total_swaps
