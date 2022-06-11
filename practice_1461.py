"""
Given a binary string s and an integer k, return true if every binary code of length k is a substring of s. Otherwise, return false.

Example 1:

Input: s = "00110110", k = 2
Output: true
Explanation: The binary codes of length 2 are "00", "01", "10" and "11". They can be all found as substrings at indices 0, 1, 3 and 2 respectively.
Example 2:

Input: s = "0110", k = 1
Output: true
Explanation: The binary codes of length 1 are "0" and "1", it is clear that both exist as a substring. 
Example 3:

Input: s = "0110", k = 2
Output: false
Explanation: The binary code "00" is of length 2 and does not exist in the array.
"""
s = "00110110"
k = 2

def hasAllCodes(s, k):
    total = 2**k
    found, i = False, 0
    memory = {}
    while not found and i<=len(s)-k:
        sub_s = s[i:i+k]
        memory[sub_s] = 1 if sub_s not in memory else memory[sub_s]+1
        if len(memory.keys()) == total: found = True
        i = i + 1
    # print(total, len(memory.keys()))
    # print(memory)
    return found