"""
Developer: Isaac neace
Program: Lab 9
Date: 11/8/18

Description: This program will create a binary tree
             that is sorted by smallest to largest
             values. You can also search for specific
             values and it will do an ordered search
             Finally you can locate the largest and
             the smallest value in the list.

"""

class BinaryTree(object): 

    def __init__(self, root):
        self.key = root
        self.left_child = None
        self.right_child = None

    #searches for a value
    def search(self, item):

        if self.key == item or self == None:

            return self.key

        else:
            
            if self.key > item and self.left_child != None:
                self.left_child.search(item)
                print("Searching left")

            elif self.key <= item and self.right_child != None:
                self.right_child.search(item)
                print("Searching right")
            
    #inserts a value
    def insert(self, new_node):

        if self == None:
            self = new_node

        else:
            current = self

            while current != None:

                parent = current
                if new_node.key < current.key:
                    current = current.left_child
                else:
                    current = current.right_child

            if new_node.key < parent.key:
                parent.left_child = new_node

            else:
                parent.right_child = new_node

    #Searches through a list inorder
    def inorder(self):
        if self.left_child:
            self.left_child.inorder()

        print(self.key)

        if self.right_child:
            self.right_child.inorder()

    
    def get_right_child(self):
        return self.right_child

    def get_left_child(self):
        return self.left_child

    #Finds the smallest value in the tree
    def findSmallest(self):

        if self.left_child == None:
            return self.key
        else:
            self = self.left_child
            return self.findSmallest()

    #Finds the largest value in the tree
    def findLargest(self):
        if self.right_child == None:
            return self.key
        else:
            self = self.right_child
            return self.findLargest()

#Creates a test Tree:
a = BinaryTree(10)
b = BinaryTree(11)
c = BinaryTree(9)
d = BinaryTree(32)
e = BinaryTree(1)
f = BinaryTree(4)

a.insert(b)
a.insert(c)
a.insert(d)
a.insert(e)
a.insert(f)


"""
Output:
>>> a.findLargest()
32
>>> a.findSmallest()
1
>>> a.inorder()
1
4
9
10
11
32
>>> a.search(10)
10
>>> 
"""
