# https://leetcode.com/problems/two-sum/description/
# https://excalidraw.com/#json=gZWdWb8Psl9VQh7Zp_Y-G,UpSy5W7cNsLQ0BpWlptJOw

#time: O(n^2)
#space: O(n)

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums) - 1): # don`t need to check the last element
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
        return [] # no solution found