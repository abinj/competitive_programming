
def moveZeroes(nums):
    counter = 0
    for i in nums:
        if i != 0:
            nums[counter]=i
            counter+=1

    for i in range(counter,len(nums)):
        nums[i]=0
    
nums= [5,0,6,4,0,3,8,0]
moveZeroes(nums)
print(nums)