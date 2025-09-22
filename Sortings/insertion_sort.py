from random import randint

def insertion_sort(nums):
    new_list=[]
    for i in nums:
        if not new_list:
            new_list.append(i)
        else:
            flag=False
            for j in new_list:
                if j>i:
                    flag=True
                    index=new_list.index(j)
                    new_list.insert(index,i)
                    break
            if not flag:
                new_list.append(i)
    return new_list

nums = [randint(0,10) for _ in range(10)]
print(insertion_sort(nums))