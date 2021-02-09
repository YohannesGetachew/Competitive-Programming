def twoSum(nums, target):
    numsLength = len(nums)
    if(target >= -pow(10, 9) and target <= pow(10, 9)):
        if(numsLength >= 2 and numsLength <= pow(10, 3)):
            for index in range(len(nums)):
                firstNum = nums[index]
                if(firstNum >= -pow(10, 9) and firstNum <= pow(10, 9)):
                    for secondNumIndex in range(index+1, len(nums)):
                        secondNum = nums[secondNumIndex]
                        if(firstNum + secondNum == target):
                            return [index, secondNumIndex]


print(twoSum([2, 4, 8, 9], 17))
