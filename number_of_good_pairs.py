def numIdenticalPairs(nums):
    numsLen = len(nums)
    goodIntegers = 0
    if(numsLen >= 1 and numsLen <= 100):
        for index in range(numsLen):
            for secondIndex in range(index+1, numsLen):
                if(nums[index] == nums[secondIndex]):
                    goodIntegers += 1
        return goodIntegers
    else:
        return


print(numIdenticalPairs([1, 2, 1]))
