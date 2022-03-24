class Solution(object):
    def computeNextIndex(self, i, j, start, end):
        if i == start:
            if j == end:
                inext = i+1
                jnext = j
            else:
                inext = i
                jnext = j+1
        elif i == end:
            if j == start:
                inext = i-1
                jnext = j
            else:
                inext = i
                jnext = j-1
        else:
            if j == start:
                inext = i-1
                jnext = j
            else:  # j == end
                inext = i+1
                jnext = j

        return inext, jnext


    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        # rounds = (n+1) // 2
        sn = 0
        en = n-1
        while sn < en:
            rot_counter = en-sn
            while rot_counter:
                i, j = sn, sn
                store = matrix[i][j]
                n_items = (en-sn+1)*2 + (en-sn-1)*2
                while n_items:                    
                    ii, jj = self.computeNextIndex(i, j, sn, en)
                    # print('current', i, j)
                    # print('next', ii, jj)

                    tmp = matrix[ii][jj]
                    matrix[ii][jj] = store
                    store = tmp

                    i, j = ii, jj
                    n_items -= 1
                
                # for line in matrix:
                #     print(line)
                # print()
                rot_counter -= 1

            sn = sn+1
            en = en-1
        
        return matrix

if __name__ == '__main__':
    sol = Solution()
    input_matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
    
    # for line in input_matrix:
    #     print(line)
    # print()

    sol.rotate(input_matrix)

    for line in input_matrix:
        print(line)
    print()

    for line in [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]:
        print(line)