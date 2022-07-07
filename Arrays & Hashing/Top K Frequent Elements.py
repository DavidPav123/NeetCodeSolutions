class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        number_count = dict()
        tracker = []

        for number in nums:
            if number not in number_count.keys():
                    number_count[number] = 1
            else:
                    number_count[number] = number_count[number] + 1

        for keys in number_count:
            tracker.append(number_count[keys])
        
        tracker.sort(reverse=True)
        
        for i in range(k):
            for key in number_count:
                if number_count[key] == tracker[0]: 
                    tracker.append(key)
                    number_count.pop(key)
                    tracker.pop(0)
                    break
                    
        while len(tracker) > k:
            tracker.pop(0)

        return tracker



        



            