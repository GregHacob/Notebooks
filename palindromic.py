import re

class Palindromic():

 def __init__(self, st):  
    st = st.lower()
    st = self.removeSpecialChars(st)
    self.st = st
 
 def longestPalindromic(self):
    palindromic = [0]*len(self.st)     
    length = len(self.st)
    
    #special cases when the string is empty, has 1, or 2 characters  
    if length == 0:
     return None
    elif length == 1:
     return self.st 
    elif length == 2:
      if self.st[0] == self.st[1]:
        return self.st
      else:
        return None
   
    for i in range(1,len(self.st)-1):
     if i<=length-i:
      c_range = i
     else:
      c_range = length - i - 1
     count = 0
     for j in range(1,c_range+1):
       if self.st[i-j] == self.st[i+j]:
        count+=1
       else:
        break
     palindromic[i] = count   

    max_v = max(palindromic)
    
    #special case when there are no palindromes
    if max_v == 0:
     return None
     
    max_v_index = palindromic.index(max_v)
    return self.st[max_v_index-max_v:max_v_index+max_v+1]   
 
 def removeSpecialChars(self, string):
    return re.sub("[^a-z]","", string)