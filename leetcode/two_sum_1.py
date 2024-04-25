class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # O(n^2) solution. For O(n*logn) sort and do 2 pointer higher-lower
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i != j and nums[i] + nums[j] == target:
                    return i, j
        