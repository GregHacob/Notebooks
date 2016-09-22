import re

def question1(s, t):

    foundAnagram = False
    if len(t) <= len(s):
        if charsExist(s,t):
            for index in findOccurences(s,t[0]):
                for i in range(len(t) + 1):
                    try:
                     if charsExist(s[index-len(t)+i:index+i],t):
                      foundAnagram = True
                    except IndexError:
                     pass         
    
    return foundAnagram

def charsExist(st1, st2):    
    for chr in st2:     
      if chr not in st1:
        return False
    return True

def findOccurences(s, ch):
    return [i for i, letter in enumerate(s) if letter == ch]    
    

    
def question2(a):
   
   charCounts = {}
   a = a.lower()
   a = removeSpecialChars(a)
   
   #Create a dictionary and count the number of each character in the string
   for chr in a:
    if chr in charCounts:
        charCounts[chr]+=1
    else:
        charCounts[chr] = 1
        
   print charCounts
   
   #Find the largest odd value in the dictionary
   maxOdd = getlargestOddValue(charCounts)
   
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
   

def getlargestOddValue(dict):
    return max(i for i in dict.values() if i % 2)

def removeSpecialChars(string):
 return re.sub("[^a-z]","", string)
     
print question2("This is great")   

#print question1("computerscience", "rest")
    

