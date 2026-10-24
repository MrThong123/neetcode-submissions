class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
       seen=set()
       for i in nums:
            if i in seen:
                return True
            seen.add(i)
       return False
        # if len(nums)!=len(set(nums)):
        #     return True
        # return False