class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        max_num=len(nums)

        sum_acc_nums=max_num*(max_num+1)//2
        sum_nums=sum(nums)
        missing=sum_acc_nums-sum_nums
        
        return missing
