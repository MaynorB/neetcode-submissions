class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sol = []
        for i in range(len(nums)):
            tar = target - nums[i]
            nums[i] = -10000001 # honestly probably a better way for this line
            if tar in nums:
                sol.append(i)
                sol.append(nums.index(tar))
                break
        return sol