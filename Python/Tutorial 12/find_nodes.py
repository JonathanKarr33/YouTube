"""First part of Sample Google Interview Question
Find the total number of nodes from each value to the root node (1) in this tree
       1
     /   \\
    2      3
   / \\    / \\
  4   5   6   7
 /\\
8  9                       """

number = int(input("Enter a number here: "))
nodes = 0
while (2**(nodes+1)<=number):
  nodes += 1
print (nodes)
  
total_nodes = 0
while(number>0):
  nodes =0
  while (2**(nodes+1)<=number):
   nodes += 1
  number -= 1
  total_nodes += nodes
print(total_nodes)


