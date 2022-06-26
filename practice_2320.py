"""
2320. Count Number of Ways to Place Houses

There is a street with n * 2 plots, where there are n plots on each side of the street. The plots on each side are numbered from 1 to n. On each plot, a house can be placed.
Return the number of ways houses can be placed such that no two houses are adjacent to each other on the same side of the street. Since the answer may be very large, return it modulo 109 + 7.
Note that if a house is placed on the ith plot on one side of the street, a house can also be placed on the ith plot on the other side of the street.

Example 1:
    Input: n = 1
    Output: 4
    Explanation: 
    Possible arrangements:
    1. All plots are empty.
    2. A house is placed on one side of the street.
    3. A house is placed on the other side of the street.
    4. Two houses are placed, one on each side of the street.

Solution Explanation: @vegishanmukh7
Fibonacci Series: The opposite sides are independent to each other. 
So, the total number of ways would be the product of no.of ways of one side and another side.
Let's try to write the result for some numbers:
    1 -> 4 (2*2)
    2 -> 9 (3*3)
    3 -> 25 (5*5)
    4 -> 64 (8*8)
"""
class Solution:
    def countHousePlacements(self, n: int) -> int:
        """
        
        """
        if n==1: return 4
        if n==2: return 9
        
        preprev, prev = 2, 3
        current = 0
        for i in range(n-2):
            current = preprev + prev
            preprev, prev = prev, current
        
        return (current*current)%(10**9+7)