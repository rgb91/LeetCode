"""
Given two strings s and p, return an array of all the start indices of p's anagrams in s. You may return the answer in any order.
An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

Input: s = "cbaebabacd", p = "abc"
Output: [0,6]
Explanation:
The substring with start index = 0 is "cba", which is an anagram of "abc".
The substring with start index = 6 is "bac", which is an anagram of "abc".

Input: s = "abab", p = "ab"
Output: [0,1,2]
Explanation:
The substring with start index = 0 is "ab", which is an anagram of "ab".
The substring with start index = 1 is "ba", which is an anagram of "ab".
The substring with start index = 2 is "ab", which is an anagram of "ab".
"""

class Solution(object):
    def getCharFrequencies(self, st):
        char_freqs = dict()
        for c in st:
            if c not in char_freqs:
                char_freqs[c] = 1
            else:
                char_freqs[c] += 1
        return char_freqs

    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        
        p_freq = self.getCharFrequencies(p)
        # print('p', p_freq)
        sub_freq = dict()

        result = []
        for start in range(len(s)-len(p)+1):
            end = start + len(p)
            substring = s[start : end]

            # print(start, end)
            if start == 0:
                sub_freq = self.getCharFrequencies(substring)
            else:
                if s[end-1] not in sub_freq:
                    sub_freq[s[end-1]] = 1
                else:
                    sub_freq[s[end-1]] += 1
                
                sub_freq[s[start-1]] -= 1
                if sub_freq[s[start-1]] == 0:
                    del sub_freq[s[start-1]]
            
            # print(sub_freq)

            if sub_freq == p_freq:
                result.append(start)
        
        return result


if __name__ == '__main__':
    sol = Solution()
    print(sol.findAnagrams("abab", "ab"))
