# First Unique Character

Given a string, write a function to find the first non-repeating character and return its index.

## White Board Process

![First Unique Character](./first_unique_character.jpg)

## Approach and Efficiency

I utilized 3 variables for reference as I traversed the list. A previous, current, and nextUp. On each traversal, I would point the current node to the previous. And then reassign all variables to be their respective next node.

Big O:

- Space: O(1)
- Time: O(n)
