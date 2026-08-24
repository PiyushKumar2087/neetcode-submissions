class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen={}
        ans=[]

        for i,val in enumerate(nums):
            num=target-val
            if num in seen:
                ans.append(seen[num])
                ans.append(i)
                return ans
            else:
                seen[val]=i
                i=i+1
        return ans