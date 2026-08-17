class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        g = []
        n = len(nums)
        for i in range(n):
            num = min(nums)
            ind = nums.index(num)
            g.append(nums[ind])
            del nums[ind]
        return g