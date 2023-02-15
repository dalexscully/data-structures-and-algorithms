# Count Students Left

Given the number of students left, return the number of students won't eat.

## White Board Process

![Count Students Left](./count_students_left.jpg)

## Approach and Efficiency

I utilized 3 variables for reference as I traversed the list. A previous, current, and nextUp. On each traversal, I would point the current node to the previous. And then reassign all variables to be their respective next node.

Big O:

- Space: O(1)
- Time: O(n)
