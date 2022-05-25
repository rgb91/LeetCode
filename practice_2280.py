class Solution:
    def minimumLines(self, sp: List[List[int]]) -> int:
        # print(sp)
        sp.sort()
        # print(sp)
        n = len(sp) - 1
        
        for i in range(1, len(sp)-1):
            a, b, c = sp[i-1], sp[i], sp[i+1]
            x_delta_ab = b[0] - a[0]
            y_delta_ab = b[1] - a[1]
            x_delta_bc = c[0] - b[0]
            y_delta_bc = c[1] - b[1]
            
            if y_delta_ab*x_delta_bc == y_delta_bc*x_delta_ab:
                n -= 1
        return n