class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dct = {}
        for i in nums:
            if i not in dct:
                dct[i] = 1
            else:
                return True
        return False