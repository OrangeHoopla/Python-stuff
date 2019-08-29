class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        size = len(nums)
        res = []
        nums.sort()    
        if size == 0 or nums[0]*4 > target or nums[size - 1]*4 < target:
            return []
        for i in range(size - 3):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            for j in range(i + 1, size - 2):   
                slow = j + 1
                fast = size  - 1        
                while slow < fast:
                    twoSum = nums[slow] + nums[fast]
                    if twoSum == target - nums[i] - nums[j]:
                        res.append(tuple([nums[i], nums[j], nums[slow], nums[fast]]))
                        slow += 1
                        fast -= 1
                    elif twoSum > target - nums[i] - nums[j]:
                        fast -= 1
                    else:
                        slow += 1
        return set(res)                    
                    