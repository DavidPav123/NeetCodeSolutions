class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0 
        
        num_set = list(set(nums))
        
        num_in_row = 1
        current_nums_row = 1
        num_set.sort()

        tracking_num = num_set[0]
        for numbers in range(1, len(num_set)):
            if (tracking_num + 1) != num_set[numbers]:
                if current_nums_row > num_in_row: 
                    num_in_row = current_nums_row
                current_nums_row = 1
            else: 
                current_nums_row += 1      
            tracking_num = num_set[numbers]
        if current_nums_row > num_in_row: 
            num_in_row = current_nums_row

        return num_in_row

        
