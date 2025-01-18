#Leetcode 3. Longest Substring Without Repeating Characters
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        m = float("-inf")  #initialize max as lowest possible val which in python is -inf
        st = set()  #
        i = 0  #left part of window
        for j in range(len(s)):  #right pointer j of the window
            while s[j] in st:  
                m = max(m, len(st))  #Update max found so far
                st.remove(s[i])  
                i += 1  #move left pointer and remove the value from set

            st.add(s[j])  

        m = max(m, len(st))  #checking again when loop ends
        return m 
