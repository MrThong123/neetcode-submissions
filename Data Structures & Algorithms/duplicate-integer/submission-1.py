class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        input=set()
        for n in nums:
            if n in input:
                return True
            input.add(n)
        return False