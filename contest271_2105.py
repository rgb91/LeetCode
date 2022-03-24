class Solution(object):
    def minimumRefill(self, plants, capacityA, capacityB):
        """
        :type plants: List[int]
        :type capacityA: int
        :type capacityB: int
        :rtype: int
        """
        refill = 0
        capacityA_max, capacityB_max = capacityA, capacityB
        i, j = 0, len(plants)-1
        while i <= j:
            if i == j:
                if capacityA > capacityB:
                    if capacityA < plants[i]:
                        refill += 1
                        capacityA = capacityA_max  - plants[i]
                else:
                    if capacityB < plants[j]:
                        refill += 1
                        capacityB = capacityB_max - plants[j]
                break

            if capacityA < plants[i]:
                refill += 1
                capacityA = capacityA_max
            capacityA -= plants[i]
            
            if capacityB < plants[j]:
                refill += 1
                capacityB = capacityB_max
            capacityB -= plants[j]

            # print('> i', plants[i], capacityA, '\t> j', plants[j] , capacityB, '\t>', refill)

            i += 1
            j -= 1
        
        return refill

if __name__ == '__main__':
    sol = Solution()
    # print(sol.minimumRefill([2,2,3,3], 5, 5))
    print(sol.minimumRefill([1,2,4,4,5], 6, 5))
        