# Hashtables

Hash tables are data structures that utilize key value pairs in the forms of a node or bucket. The structure is primarily used for storage. The hash will change the key into an integer index and store the value at that specific index. With the hash, multiple keys can be stored into the same index. This is known as a collision.

## Challenge

Implement a Hashtable Class with the following methods listed in the API below.

## Approach & Efficiency

This data structure has a time complexity of O(1) and a space complexity of O(n).

## API

* get() - takes a key as input, returns the associated value, or None if the value doesn't exist

* set() - takes a key/value pair and stores them

* has() - takes a key - returns True if the key is in the data structure, otherwise returns false

* keys() - returns a list of all keys in the data structure
