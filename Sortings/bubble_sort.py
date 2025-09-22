from random import randint as rnd

def bubble_sort(nums):
    for i in nums:
        flag = False
        for j in range(len(nums)-1):
            if nums[j]>nums[j+1]:
                flag=True
                nums[j],nums[j+1] = nums[j+1],nums[j]
        if not flag:
            break
    return nums

nums = [rnd(0,10) for i in range(10)]

print(bubble_sort(nums))