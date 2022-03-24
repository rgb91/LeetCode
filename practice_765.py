class Solution(object):
    def union(self, groups, p1, p2):
        group_p1 = groups[p1]
        for i in range(len(groups)):
            if groups[i] == group_p1:
                groups[i] = groups[p2]
        return groups

    def minSwapsCouples(self, row):
        """
        :type row: List[int]
        :rtype: int
        """
        groups = [0]*len(row)
        g = 0
        for i in range(0, len(row), 2):
            groups[i] = g
            groups[i+1] = g
            g += 1
        
        # indices = [i for i in range(len(row))]
        # print(indices)
        # print(row)
        # print(groups)
        swaps = 0
        N_groups = len(groups) // 2
        for g in range(N_groups):
            person1 = row[2*g]
            person2 = row[2*g+1]
            # print('persons', person1, person2)

            couple_p1 = person1 // 2  # group for person 1
            couple_p2 = person2 // 2  # group for person 2
            # print('couples', couple_p1, couple_p2)
            # print('groups', groups[person1], groups[person2])
            # print()

            if couple_p1 != couple_p2:
                if groups[person1] != groups[person2]:  # FIND: not in the same couple group now
                    swaps += 1
                    groups = self.union(groups, person1, person2)
        
        # print(groups)
        return swaps

if __name__ == '__main__':
    sol = Solution()
    # print(sol.minSwapsCouples([0,2,1,3]))
    print(sol.minSwapsCouples([10,7,4,2,3,0,9,11,1,5,6,8]))
    