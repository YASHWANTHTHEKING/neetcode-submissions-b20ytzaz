from collections import Counter
from typing import List

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        counter = Counter(nums)
       
        return any(count > 1 for count in counter.values())
