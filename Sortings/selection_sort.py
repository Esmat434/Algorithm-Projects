from random import randint as rnd

def selection_sort(nums):
    index=None
    for i in range(len(nums)-1):
        for j in range(i+1,len(nums)):
            if nums[i]>nums[j]:
                if index:
                    if nums[index]>nums[j]:
                        index=j
                else:
                    index=j

        if nums[i]>nums[index]:
            nums[i],nums[index] = nums[index],nums[i]

    return nums

nums = [rnd(0,10) for _ in range(10)]
print(selection_sort(nums))