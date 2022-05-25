class Solution:
    
    def longestWPI(self, hours: List[int]) -> int:
        start, end = 0, -1
        for i, h in enumerate(hours):
            current_sum += 1 if h > 8 else -1
            end = i if current_sum > 0 else -1
                
        return end-start+1

        