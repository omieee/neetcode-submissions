'''
numbers = [1,2,3,4]
target = 3

leftptr = 0
rightptr = len(numbers) - 1

    ->
    while leftptr < rightptr:
        if numbers[leftptr] + numbers[rightptr] > target:
            rightptr -= 1
            continue
        if numbers[leftptr] + numbers[rightptr] < target:
            leftptr += 1
            continue
        if numbers[leftptr] + numbers[rightptr] == target:
            return [leftptr + 1, rightptr + 1]
'''

class Solution:
    
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        leftptr = 0
        rightptr = len(numbers) - 1
        while leftptr < rightptr:
            if numbers[leftptr] + numbers[rightptr] > target:
                rightptr -= 1
                continue
            if numbers[leftptr] + numbers[rightptr] < target:
                leftptr += 1
                continue
            if numbers[leftptr] + numbers[rightptr] == target:
                return [leftptr + 1, rightptr + 1]
        