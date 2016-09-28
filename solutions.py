from graph import Graph
from kruskal import Kruskal
from anagram import Anagram
from palindromic import Palindromic
import pdb
 
    
def question1(s, t):
    anagram_obj = Anagram(s,t)
    return anagram_obj.isAnagram()
    
def question2(a):
    palindromic_obj = Palindromic(a)
    return palindromic_obj.longestPalindromic()    
     
def question3(G):
    kruskal_obj = Kruskal(graph)
    mst = kruskal_obj.buildMST()
    return kruskal_obj.adjacencyList(mst)
      
    
print   
print "QUESTION 1"    
print question1("computerscience", "rest")
print "*******************************************"
print

print "QUESTION 2"   
print question2("This is great")  
print "*******************************************"
print

print "QUESTION 3"
graph = Graph()
graph.insert_edge(3,"A","B")
graph.insert_edge(2,"B","C")
graph.insert_edge(9,"B","I")
graph.insert_edge(9,"B","J")
graph.insert_edge(4,"B","D")
graph.insert_edge(2,"C","D")
graph.insert_edge(8,"C","I")
graph.insert_edge(9,"C","E")
graph.insert_edge(9,"D","E")
graph.insert_edge(6,"D","A")
graph.insert_edge(4,"E","F")
graph.insert_edge(7,"E","I")
graph.insert_edge(5,"E","G")
graph.insert_edge(1,"F","G")
graph.insert_edge(4,"F","H")
graph.insert_edge(3,"G","H")
graph.insert_edge(10,"G","I")
graph.insert_edge(10,"H","I")
graph.insert_edge(18,"H","J")
graph.insert_edge(8,"I","J")
graph.insert_edge(9,"J","A")

print question3(graph)     
print "*******************************************"
print
  
