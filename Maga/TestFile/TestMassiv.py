class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        sum = 0
        prevNum = 0
        for i in len(nums):
            prevNum = nums[i + 1]
            sum = nums[i] + prevNum
            if sum == target:
                return [i, i + 1]

nums = [3,2,4]
print(Solution.twoSum(self, nums = nums, target = 6))