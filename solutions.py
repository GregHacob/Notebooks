from graph import Graph
from kruskal import Kruskal
from anagram import Anagram
from palindromic import Palindromic
from binarysearchtree import BST
from lca import LCA
from linkedlist import LinkedList, Node
import pdb
 
    
def question1(s, t):
    anagram_obj = Anagram(s,t)
    return anagram_obj.findAnagram()
    
def question2(a):
    palindromic_obj = Palindromic(a)
    return palindromic_obj.longestPalindromic()    
 
     
def question3(G):
    kruskal_obj = Kruskal(G)
    mst = kruskal_obj.buildMST()
    return kruskal_obj.adjacencyList(mst)

def question4(T, r, n1, n2):      
    bst_obj = BST(r)
    bst_obj.populateBSTfromMatrix(T)  
    #print bst_obj.print_tree()
    
    lca_obj = LCA(bst_obj, n1, n2)
    return lca_obj.findLCA()

def question5(ll,n):
    if ll.nthToLast(n):  
     return ll.nthToLast(n).data
    else:
     return None    
    
    
print   
print "TEST CASES FOR QUESTION 1" 
print "*******************************************"
#Should print True   
print question1("computerscience", "crest")
#Should print False   
print question1(" ", "test")
#Should print False   
print question1("!$%#@^&@#", "")
print "*******************************************"
print

print   
print "TEST CASES FOR QUESTION 2" 
print "*******************************************"
#Should print None
print question2("abcdefghijklmnopqrstuvwxyz")   
#Should print dogeeseseegod
print question2("This is a palindrome -- Do Geese See God!")
#Should print aa
print question2("aa")
print "*******************************************"
print

print   
print "TEST CASES FOR QUESTION 3" 
print "*******************************************"

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

#Should print 
#{'A': [('B', 3)], 'C': [('B', 2), ('D', 2), ('I', 8)], 'B': [('C', 2), ('A', 3)], 'E': [('F', 4), ('I', 7)], 'D': [('C', 2)], 'G': [('F', 1), ('H', 3)], 'F': [('G', 1), ('E', 4)], #'I': [('E', 7), ('C', 8), ('J', 8)], 'H': [('G', 3)], 'J': [('I', 8)]}
print question3(graph)  
#The link below is the picture of the above spanning tree for the graph
#https://en.wikipedia.org/wiki/Minimum_spanning_tree#/media/File:Minimum_spanning_tree.svg

graph1 = Graph()
graph1.insert_edge(1,"A","B")
graph1.insert_edge(5,"C","D")
#Disconnected graph
#Should print {'A': [('B', 1)], 'C': [('D', 5)], 'B': [('A', 1)], 'D': [('C', 5)]}
print question3(graph1)  

graph2 = Graph()
graph2.insert_edge(1,"A","B")
graph2.insert_edge(2,"A","B")
graph2.insert_edge(3,"A","B")
graph2.insert_edge(4,"A","B")
graph2.insert_edge(5,"A","B")
graph2.insert_edge(5,"A","B")
graph2.insert_edge(6,"A","B")
graph2.insert_edge(7,"A","B")
graph2.insert_edge(8,"A","B")
#should print {'A': [('B', 1)], 'B': [('A', 1)]}
print question3(graph2)  

print "*******************************************"
print


print   
print "TEST CASES FOR QUESTION 4" 
print "*******************************************" 
#Should print 3
print question4([[0, 1, 0, 0, 0],
                 [0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0],
                 [1, 0, 0, 0, 1],
                 [0, 0, 0, 0, 0]],
                 3,
                 1,
                 4)
#Should print 0                 
print question4([],
                 0,
                 0,
                 0)
#Should print 0
print question4([[0, 1, 0, 0, 0],
                 [0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0],
                 [1, 0, 0, 0, 1],
                 [0, 0, 0, 0, 0]],
                 0,
                 911,
                 -4)
print "*******************************************"
print

print   
print "TEST CASES FOR QUESTION 5" 
print "*******************************************"  
ll = LinkedList(Node(1))
for i in range(2,10):
 ll.append(Node(i))
#should print 7
print question5(ll,3)
#should print None
print question5(ll,0)
#should print None
print question5(ll,500)
print "*******************************************"
print

