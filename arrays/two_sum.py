# Problem: Two Sum
# Difficulty: Easy
# Link: https://leetcode.com/problems/two-sum/
from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i, n in enumerate(nums):
            comp = target - n
            if comp in seen:
                return [seen[comp], i]
            seen[n] = i
        return []

if __name__ == "__main__":
    print(Solution().twoSum([2,7,11,15], 9))
