import random
import math 

"""""
Kavin Zhu
20167040
“I confirm that this submission is my own work and is consistent with the Queen’s regulations on Academic Integrity” 
"""

class Binary_Tree_Vertex:
    def __init__(self, value, left_child = None, right_child = None):
        self.value = value
        self.left_child = left_child
        self.right_child = right_child

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self,x):
        self.root = rec_insert(self.root,x)

    def search(self,x):
        current = self.root        
        while current != None:
            if current.value == x:
                return current
            elif current.value > x:
                current = current.left_child
            else: 
                current = current.right_child
        return None          #  x is not in the set

    def remove(self,x):
        self.root = rec_remove(self.root,x)

    def height(self):
        return rec_height(self.root)

def rec_insert(current,x):
    if current is None:
        current = Binary_Tree_Vertex(x)
    elif current.value >= x:
        current.left_child = rec_insert(current.left_child,x)
    else:
        current.right_child = rec_insert(current.right_child,x)
    return current

def rec_remove(current, x):
    if current is None:
        return current        # takes care of case where x is not
                                # present in T
    elif current.value < x:
        current.right_child = rec_remove(current.right_child, x)
        return current
    elif current.value > x:
        current.left_child = rec_remove(current.left_child, x)
        return current
    else:                     # found it!
        if current.left_child is None:
            return current.right_child
        elif current.right_child is None:
            return current.left_child
        else:
            tmp = fix_left_subtree(current)
            tmp.right_child = current.right_child
            return tmp

def fix_left_subtree(v):
    temp = v.left_child      # temp is the root of v’s
                                # left subtree
    if temp.right_child is None:
        return temp          # no fix needed
    else:
        parent = None
        current = temp
        while current.right_child != None:
            parent = current
            current = current.right_child
        parent.right_child = current.left_child
        current.left_child = temp
        return current

def rec_height(root):
    if root is None:
        return 0 
    else:
        # Compute the height of each subtree
        leftHeight = rec_height(root.left_child)
        rightHeight = rec_height(root.right_child)
 
        # Use the larger one
        if (leftHeight > rightHeight):
            return leftHeight+1
        else:
            return rightHeight+1

def main():
    n_values = [1000, 2000, 4000, 8000, 16000]
    # iterate through possible n values
    for n in n_values:
        n_heights = []
        # list for possible values to be put into the tree 
        BST_values1 = []
        # append values 1 to n*1.5 into the list of possible values
        for x in range(1,(n*15)//10+1):
            BST_values1.append(x)
        """ 
        for 500 trees, insert n*1.5 random values from the possible values that could be
        put into the tree, into the tree. 
        """ 
        for i in range(1,501):
            my_tree = BinarySearchTree()
            random.shuffle(BST_values1)
            for t in range(1,(n*15)//10+1):
                my_tree.insert(BST_values1[t-1])

            # remove n/2 randomly selected values that are actually in the tree
            random.shuffle(BST_values1)
            for p in range(1,n//2+1):
                my_tree.remove(BST_values1[p-1])
            
            # insert height of tree into list of heights for all generated trees of n
            n_heights.append(my_tree.height())

        """
         finding minimum and maximum and average height 
         for all generated trees of n, also finding percentage of trees 
         on n vertices whose height is >= n/2
        """
        total = 0
        greaterEqualCount = 0
        for height in n_heights:
            total = total + height
            if height >= n//2:
                greaterEqualCount = greaterEqualCount + 1

        average_height = total/len(n_heights)
        percent = (greaterEqualCount/len(n_heights))*100

        k = average_height/(math.log(n))
        t = average_height/n

        print("Max: ", max(n_heights))
        print("Min: ", min(n_heights))
        print("Average height: ", average_height)
        print("Percent: ", percent, "%")
        print("k value: ", k)
        print("t value: ", t)
  
main()
