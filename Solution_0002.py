from typing import List

class Solution_0002:
    def twoSum( nums: List[int], target: int) -> List[int]:
        num_map = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in num_map:
                return [num_map[complement], i]
            num_map[num] = i
        return []

    print(twoSum([2,11,7,15], 9))