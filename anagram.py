class Anagram():
 def __init__(self, s, t):
    self.s = s
    self.t = t
 
 def isAnagram(self):
    foundAnagram = False
    if len(self.t) <= len(self.s):
        if self.charsExist(self.s,self.t):
            for index in self.findOccurences(self.s,self.t[0]):
                for i in range(len(self.t) + 1):
                    try:
                     if self.charsExist(self.s[index-len(self.t)+i:index+i],self.t):
                      foundAnagram = True
                    except IndexError:
                     pass           
    return foundAnagram

 def charsExist(self, st1, st2):    
    for chr in st2:     
      if chr not in st1:
        return False
    return True

 def findOccurences(delf, s, ch):
    return [i for i, letter in enumerate(s) if letter == ch]    
