class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for num in range(len(nums)):
            search_num = target - nums[num]
            for subnum in range(len(nums)):
                if nums[subnum] == search_num and num != subnum:
                    return [num,subnum]