# Trees

A tree whose elements have at most 2 children is called a `binary tree`. Since each element in a binary tree can have only 2 children, we typically name them the left and right children. 

A `binary Search Tree` is a node-based binary tree data structure that has the following properties:

* The left subtree of a node contains only nodes with keys lesser than the node’s key.

* The right subtree of a node contains only nodes with keys greater than the node’s key.

* The left and right subtree each must also be a binary search tree.

* There must be no duplicate nodes.

## Challenge

1. Create a Node class that has properties for the value stored in the node, the left child node, and the right child node.

2. Create a Binary Tree class

    * Define a method for each of the depth first traversals:

        * pre order
        * in order
        * post order
    Each depth first traversal method should return an `array of values`, `ordered` appropriately.
3. Create a Binary Search Tree class

    * This class should be a sub-class (or your languages equivalent) of the Binary Tree Class, with the following additional methods:
      * Add

          * Arguments: value

          * Return: nothing

          * Adds a new node with that value in the correct location in the binary search tree.
      * Contains
          Argument: value
          Returns: boolean indicating whether or not the value is in the tree at least once.



## Approach & Efficiency

**Binary Tree**

Used the `depth first traversal` where we prioritize going through the height of the tree first


**Binary Search Tree**

Created BinarySearchTree class that inherits the properties of binary tree.

Created an add method that takes in a value. If our binary tree has no root we set it to a new node with our new value, if it had a root we set current to the root, while current is true, we check if the value of the root is the same as the value we want to add if so we return because binarysearch tree cant have duplicate values. if not so we check if the value is less than roots value if so we first make sure our binary tree has a left child we , if true and set current to current,left if not current.left is assigned a node with our node value. if value is > root.value we do the same process but on the right side of our binaryseatchtree

Big O:

Time: O(log(n))

Space:O(n)

Created a contains method that takes in the value we are looking for, we set current to self.root , and then used a while loop to traverse the left side of bst if value is < current.value and traverse right side of bst if value > self.root. value , we would return true if any of the nodes was found to have our value on traversal

Big 0:

Time : O(n)

Space:O(1) no additional space being used during search

## API

**Binary Tree Methods**

pre_order(self): This method will search the binary tree in the order of the root, then left node, then right node. It will return the value of the node searched.

in_order(self): This method will search the binary tree in the order of the left node, then root, then right node. It will return the value of the node searched.

post_order(self): This method will search the binary tree in the order of the left node, then right node, then root. It will return the value of the node searched.

**Binary Search Tree Methods**

add(value): This method will add a node after searching for the location to add it in the tree.

contains(value): This method will search the nodes and return a boolean if the value searching for exists in the tree.

[Link to Code](/python/data_structures/binary_tree.py)

[Link to Code](/python/data_structures/binary_search_tree.py)
