class Solution:
    def longestPalindrome(self, s: str) -> int:
      pal = s[0]
      temp = s[0]

      i = 0

      while i < len(s):
        print(i)
        chr = s[i]
        consec = chr

        left_index = i

        if i+1<len(s):
          while s[i+1] == chr:
            consec += chr
            i+=1
            if i+1 >= len (s):
              print(True) 
              break 

        if len(consec) > len(pal):
          pal = consec

        i += 1
        k = i
        j = 1
        temp_pal = consec

        if k<len(s) and left_index-j >-1:
          while s[k] == s[left_index - j]:
            temp_pal = s[k] + temp_pal + s[k]
            k += 1
            j += 1
            if k>=len(s) or left_index-j <0:
              break
            if s[k] != s[left_index-j]: 
              break
        if len(temp_pal) > len(pal):
          pal = temp_pal


      return pal   
