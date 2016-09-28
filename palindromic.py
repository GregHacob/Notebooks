import re

class Palindromic():

 def __init__(self, st):
  self.st = st
  
 def longestPalindromic(self):   
   charCounts = {}
   self.st = self.st.lower()
   self.st = self.removeSpecialChars(self.st)
   
   #Create a dictionary and count the number of each character in the string
   for chr in self.st:
    if chr in charCounts:
        charCounts[chr]+=1
    else:
        charCounts[chr] = 1
   
   #Find the largest odd value in the dictionary
   maxOdd = self.getlargestOddValue(charCounts)
  
   #create a list and add the key of the largest odd number value in trhe dictionary, maxOdd times
   palindromic = [charCounts.keys()[charCounts.values().index(maxOdd)]] * maxOdd
   
   #Find all the even values in the dictionary and add 
   #half of the characters to the end of palindromic string and 
   #the other half to the beginning
   for key, value in charCounts.items():
    if not value % 2:
      sub = [key]* (value / 2)

      palindromic[len(palindromic):] = sub
      palindromic[:0] = sub
   
   #return palindromic list as string
   return "".join(palindromic)
   

 def getlargestOddValue(self, dict):
    return max(i for i in dict.values() if i % 2)
 
 def removeSpecialChars(self, string):
    return re.sub("[^a-z]","", string)