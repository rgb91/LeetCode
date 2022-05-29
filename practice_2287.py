class Solution:
    def rearrangeCharacters(self, s: str, target: str) -> int:
        freq_s, freq_t = {}, {}
        for c in s:
            if c in freq_s:
                freq_s[c] += 1
            else:
                freq_s[c] = 1
        for c in target:
            if c in freq_t:
                freq_t[c] += 1
            else:
                freq_t[c] = 1
        
        res = len(s)+1
        for c, f in freq_t.items():
            if c in freq_s:
                if (freq_s[c] // f) < res:
                    res = freq_s[c] // f
            else:
                return 0
        return res