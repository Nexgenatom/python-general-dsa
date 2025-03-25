nums = [2,7,11,15]
target=17
def findIndex(nums,target):
    ind:list
    for i in nums:
        if target-i in nums:
            for j in nums:
                if j== target-i:
                    ind = [nums.index(j),nums.index(i)] 
    return ind                   
print(findIndex(nums,target))
