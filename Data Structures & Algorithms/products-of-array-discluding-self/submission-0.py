class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left_products = [1] * len(nums)
        right_products = [1] * len(nums)

        for i in range(1, len(nums)):
            # The left product of the current element is the product of the previous element
            left_products[i] = left_products[i-1] * nums[i-1] 
        
        for i in range(len(nums) -2, -1, -1):
            # The right product of the current element is the product of the next element
            right_products[i] = right_products[i+1] * nums[i+1]
        # The result is the product of the left and right products
        return [left_products[i] * right_products[i] for i in range(len(nums))]
        