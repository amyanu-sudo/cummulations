# Python code to demonstrate ChainMap and new_child() 
from collections import ChainMap
dic1 = { 'a' : 1, 'b' : 2 } 
dic2 = { 'b' : 3, 'c' : 4 } 
dic3 = { 'f' : 5 } 
    
# initializing ChainMap 
chain = ChainMap(dic1, dic2) 
    
print ("All the ChainMap contents are : ") 
print (chain) 
    
# using new_child() to add new dictionary 
chain1 = chain.new_child(dic3) 
   
print ("Displaying new ChainMap : ") 
print (chain1)
