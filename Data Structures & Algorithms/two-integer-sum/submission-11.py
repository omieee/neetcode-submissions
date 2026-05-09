class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        check_dict = {}
        for k,v in enumerate(nums):
            target_number = target - v
            if target_number in check_dict:
                return[check_dict[target_number], k]
            else:
                check_dict[v] = k
                