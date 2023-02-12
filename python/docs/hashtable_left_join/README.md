# Hashmap LEFT JOIN
<!-- Short summary or background information -->
This function takes two hashmaps and returns a left joined list of lists. In the output list, each inner list is a key that appeared in the first hashmap, followed by the associated value, followed by the key's value in the second hashmap if it exists, or otherwise None.
## Challenge
<!-- Description of the challenge -->
![Whiteboard Image](./hashtable_left_join%20(1).jpg)
## Approach & Efficiency
<!-- What approach did you take? Why? What is the Big O space/time for this approach? -->
While hashmap lookups can be done in constant time, O(1), all the keys in the first hashmap, and potentially the second hashmap, must be retrieved and added to the new data structure. Therefore, the time complexity is O(n). Since all values must be stored in the new data structure, the space complexity is also O(n).

Time: O(n)

Space: O(n)

