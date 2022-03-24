class Solution(object):
    def countPoints(self, rings):
        """
        :type rings: str
        :rtype: int
        """
        counts = dict(zip([i for i in range(10)], ['']*10))  # rod -> count
        for i in range(0, len(rings), 2):
            color = rings[i]
            rod = int(rings[i+1])

            counts[rod] += color
        # print(counts)
        
        result = 0
        for rod, color in counts.items():
            if 'R' in color and 'B' in color and 'G' in color:
                result += 1
        
        return result


if __name__ == '__main__':
    sol = Solution()
    print(sol.countPoints("B0R0G0R9R0B0G0"))