class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        prefix, suffix, n = 1, 1, len(nums)
        ans = -float(inf)
        for i in range(len(nums)):
            prefix = prefix * nums[i]
            suffix = suffix * nums[n - 1 - i]
            ans = max(prefix, suffix, ans)
            if prefix == 0:
                prefix = 1
            if suffix == 0:
                suffix = 1
        return ans
