# You are given two strings word1 and word2. Merge the strings by adding letters in alternating order, starting with word1. If a string is longer than the other, append the additional letters onto the end of the merged string.

# Return the merged string.

 

# Example 1:

# Input: word1 = "abc", word2 = "pqr"
# Output: "apbqcr"
# Explanation: The merged string will be merged as so:
# word1:  a   b   c
# word2:    p   q   r
# merged: a p b q c r

class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        i, j = 0, 0

        result = []

        while i < len(word1) and j < len(word2):
            result.append(word1[i])
            result.append(word2[j])

            i = i + 1
            j = j + 1

        result.append(word1[i:])
        result.append(word2[j:])

        return "".join(result)
    
    
word1 = "abc"
word2 = "pqr"

solution = Solution()

merged_string = solution.mergeAlternately(word1, word2)

print(merged_string)