class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        if(target == 0 and count(0) == 2):
            first = data.index(target)
            second = data.index(target, first + 1)
            return [first, second]
        if len(nums) == 2:
            if nums[0] + nums[1] == target:
                return [0,1]
        check_dict = {}
        for k,v in enumerate(nums):
            target_number = target - v
            if target_number in check_dict:
                return[check_dict[target_number], k]
            else:
                check_dict[v] = k
                