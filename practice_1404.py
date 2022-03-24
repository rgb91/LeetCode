class Solution(object):
    def addOne(self, s):
        srev = s[::-1]
        srev2 = ''
        carry = True
        for ch in srev:
            if carry:
                srev2 += '0' if ch == '1' else '1'
                carry = False if ch == '0' else carry
            else:
                srev2 += ch
        if carry:
            srev2 += '1'
        return srev2[::-1]
    
    def divByTwo(self, s):
        return s[:-1]

    def numSteps(self, s):
        """
        :type s: str
        :rtype: int
        """
        steps = 0
        while len(s) > 1:
            if s[-1] == '1':
                s = self.addOne(s)
            else:
                s = self.divByTwo(s)
            # print(s)
            steps += 1
        
        return steps

if __name__ == '__main__':
    sol = Solution()
    # print(sol.addOne("10"))
    print(sol.numSteps("11001"))
        