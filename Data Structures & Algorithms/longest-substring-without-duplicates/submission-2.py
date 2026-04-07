class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i = 0
        j = 0
        longest_substring = ''
        sliding_window_pointers = ()
        unique_ch = set()
        max_length = 0
        while j < len(s):
            if s[j] not in unique_ch:
                unique_ch.add(s[j])
                # print(f"Unique chrs after adding {unique_ch}, j = {j}, i  ={i}")
                j+=1
            else:
                unique_ch.remove(s[i])
                # print(f"Unique chrs after removing {unique_ch}, j = {j}, i = {i}")
                i+=1
            if len(unique_ch) >= max_length:
                max_length = len(unique_ch)
                longest_substring = s[i:j]
                sliding_window_pointers = (i,j)
        print(f"Longest Substring -> {longest_substring} Sliding window pointers {sliding_window_pointers}")     
        return max_length
       
        

         

