class Anagram():
 def __init__(self, s, t):
    self.s = s
    self.t = t
    
 def findAnagram(self): 
    t_length = len(self.t)
    for i in range(len(self.s) - t_length + 1):
     if self.isAnagram(self.s[i:i + t_length], self.t):
      return True
    return False  

 def isAnagram(self,s,t):
    c1 = [0]*26
    c2 = [0]*26
    
    if len(t) == 0:
        return False
     
    if len(s) < len(t):
        return False
        
    for i in range(len(s)):
        pos = ord(s[i])-ord('a')
        if pos < 0:
         return False
        else: 
         c1[pos] = c1[pos] + 1

    for i in range(len(t)):
        pos = ord(t[i])-ord('a')
        if pos < 0:
         return False
        else:
         c2[pos] = c2[pos] + 1

    j = 0
    foundAnagram = True
    while j<26 and foundAnagram:
        if c1[j]>=c2[j]:
            j = j + 1
        else:
            foundAnagram = False

    return foundAnagram 
    


    
