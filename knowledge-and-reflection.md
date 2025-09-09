# Overview

These questions are designed to accompany the task "Implementing a Hash Map in Python" in the "Data Structures and Algorithms" module. The questions are intended to test your understanding of hash maps, their implementation in Python, and the process of integrating data from a double linked list into a hash map. You will also be asked to reflect on your learning and the challenges you faced during the task.

# Knowledge questions

The following are all examples of hash functions:

```python
# (1) the simplest hash function (Stupidly Simple Hash)
def ssh(key):
    return 1
```

```python
# (2) hash function that sums the ASCII values of the characters in the key
def sum_of_ascii_values(key: str, size: int) -> int:
    total = 0
    for char in key:
        total += ord(char)
    return total % size
```

A more Pythonic version

```python
# (2a)
def sum_of_ascii_values(key: str, size: int) -> int:
    return sum(ord(char) for char in key) % size
```

A Pearson Hash function

```python
# (3) Pearson hash function
# https://en.wikipedia.org/wiki/Pearson_hashing
import random

random.seed(42)

# This is INCORRECT:
# pearson_table = [random.randint(0, 255) for _ in range(256)]
pearson_table = list(range(256))
random.shuffle(pearson_table)

def pearson_hash(key: str, size: int) -> int:
    hash_ = 0
    for char in key:
        hash_ = pearson_table[hash_ ^ ord(char)]
    return hash_ % size
```

The following is a hash function that uses the built-in `hash` function in Python

```python
# (4) hash function that uses the built-in hash function
def built_in_hash(key: str, size: int) -> int:
    return hash(key) % size
```

Finally, the following is a hash function that uses the `SHA256` hash function from the `hashlib` module

```python
# (5) hash function that uses the SHA256 hash function
# https://docs.python.org/3/library/hashlib.html
# https://en.wikipedia.org/wiki/SHA-2
# https://en.wikipedia.org/wiki/SHA-2#Pseudocode
import hashlib

def sha256_hash(key: str, size: int) -> int:
    return int(hashlib.sha256(key.encode()).hexdigest(), 16) % size
```

1. All of the above functions are hash functions. Explain how so - what key properties do they all share?


> All the functions above are hash functions because they contain key properties of a hash function. Some similar key properties they all contain:
> * Deterministic : A hash function must always produce the same output for the same input. 
>  - Example: with the sum of ASCII function  "dog" will always add up to the same total and map to the same index.
>  - The Pearson and SHA-256 versions are deterministic; if we keep the lookup table fixed or the algorithm unchanged, "dog" will alwyas map to the same index everytime. 
> * Fixed Output size or fixed range: Each function takes an input (a string key) of arbitrary length and maps it to an integer of fixed size.
> E.g. 0... size-1. This is achieved by applying % size (modulus of size) in all cases above. Making sure that no matter how long the input is, 
> the result will fit into the hash table of a given slot.  
> * Efficiency: Hash functions process input(s) fast/quickly. All the examples above are fast and reusable, which can be used for dictionary/set operations
>  or in hash table lookups.
>   - The constant hash (ssh) is trivial. 
>   - The sum of ASCII and Pearson functions just loop through characters once. 
>   - Python's built-in hash() is written in C for speed . 
>   - And even SHA-256 is efficient enough to run quickly on small inputs. 
> 
2. What are the advantages and disadvantages of each of the above hash functions? Evaluate in terms of uniformity, determinism, efficiency, collision resistance, sensitivity to input changes, and security[1](#Reference). You may need to do some reasearch to answer this question 😱
- The advantages and disadvantages of each hash function are many, easier to describe in a table like below given their Deterministic, Uniformity, Efficiency, Collision Resistance, Sensitivity, Security Level and an example for what they're best used for: 

> #### Characteristic table
> | Hash Function              | Deterministic | Uniformity      | Efficiency     | Collision <br/>Resistance | Sensitivity | Security Level    | Best Use Cases                                | 
> |----------------------------|---------------|-----------------|----------------|---------------------------|-------------|-------------------|-----------------------------------------------|
> | ssh (simple hash function) | Yes           | None            | Extremely Fast | None                      | None        | None              | Placeholders, testing                         |               
> | Sum of ASCII               | Yes           | Poor            | Fast           | Very Low                  | Low         | None              | Simple, non-critical hashing                  | 
> | Pearson Hash               | Yes           | Moderate - Good | Very Fast      | Moderate                  | Good        | None              | Non-security use, embedded systems            |
> | Built-in `hash` (Python)   | Yes           | Good            | Very Fast      | Acceptable                | Good        | Minimal (for DoS) | General-purpose Python hashing                |              
> | SHA-256 (hashlib)          | Yes           | Very Good       | Slower         | Very High                 | Very High   | Strong            | Security, cryptography, integrity, blockchain |  
> 
> 
> Summary: 
> * Determinism: a hash map always produce the same result for the same input which all the hash functions above show.
> * Uniformity (distribution): This prevents clustering which reduces performance in hash tables. Good hash functions spread values evenly across the available indices (slots) in the table.
> * Efficiency (speed/cost): Hashing should be fast to handle frequent lookups and inserts. Simple hashes like e.g. sum of ASCII are faster while `SHA-256` are slower but stronger.
> * Collision Resistance: collisions are minimized if  a hash function can map different inputs to the same output. Cryptographic hashes make it so collisions are extremely unlikely. 
> * Sensitivity: Refers to a small change in input which should drastically change the output. This prevents predictable collisions and helps with uniformity. Again, Cryptographic hashes helps make this possible.
> * Security: For hash tables, security doesn't matter. For passwords, integrity, or signatures etc. hashes must resist collision attacks. Referring to the website references, only cryptographic hashes (like SHA-256) provide this. 
> * 
3. List the three most important attributes (arranged from most to least) in the context of a hash map? Justify your answer.

> Three most important attributes in the context of a hash map are: 
> 1. Determinism: The same key must always hash to the same bucket(or index), otherwise searching or lookups will fail. Without determinism, we can never retrieve a stored value. For example, 
> If "dog" hashes to index 3 when inserting but later to index 7 when retrieving, the lookup fails. The value isn't really gone - it is still stored at index 3 - but because
> because the hash function now points us to the wrong spot, its 'effectively' lost.
> 2. Efficiency: Hash maps are chosen to be used for their speed. A hash that is slow negates its purpose. Since hash maps are used for fast lookups and inserts, the hash function itself must be fast, otherwise the 
> whole data slows dow. Practically simples hashes (e.g. sum of ASCII, Pearson hashin, Python's built-in hash) are very fast and well suited for hash maps. 
> Whereas, cryptographic hashes (e.g, SHA-256) are far slower because they are designed more to be more secure.
> 3. Uniformity: Hash maps rely on spreading keys evenly across the available indices(slots) in the table. Poor distribution means many collisions, good uniformity matters because hash maps rely on O(1) average time for lookups/inserts. 
> If too many keys land in the same slot while leaving others empty we will get clustering. Clustering makes lookups and inserts slower because multiple keys pike up in the same slot. 
> 

4. Which of the above hash functions would you choose to implement the requirements of the task? Why?

> If I were to implement the requirements into the task maybe the Pearson hash would be better for a mini project. The Sum of ASCII is fast, but has poor uniformity it would not be great compared to the Pearson hashing,
> which is a much better choice in terms of its uniformity to avoid clustering and slow lookups. The Pearson hash also has a O(n) notation over the key's character with fast table lookups, great for a mini projec. 
>

5. In your own words, explain each line in the pearson hash function above in terms of the criteria you listed in question 2.

> `pearson_table = list(range(256))`
> 
> Creates  a table of numbers 0-255. 
> If the table is fixed, the function is deterministic and if it's reshuffled every run it is not. 
> 
`random.shuffle(pearson_table)` 
> Shuffles the table randomly. Efficiency: Done once, not inside the loop.
> 
> `hash_ = 0` 
> Starts the hash value at 0. Same starting point every time means consistent results. 
> 
> `for char in key:` Loops through each character of input string.
> 
> This ensures every character in the key influences the result - sensitivity. Linear time with respect to key length.
> 
>`hash_ = pearson_table[hash_ ^ ord(char)]` 
> Core of the code/algorithm 
> * ord(char) turns the character into its ASCII code
> * hash_ ^ ord(char) combines the current hash value with the character's ASCII code. 
> * The result is used as an index into the table, giving the new `hash_`
> 
> - Uniformity: Table lookup spreads values 0-255. 
> - Sensitivity: A single character change will drastically alter the path through the table. 
> -  Collision resistance: since character order matters it won't collide as easily as the sum-of-ASCII would have. 
> 
> `return hash_ % size`
>  Maps the final  0-255 value into the range of the table size.
> 
> Uniformity: keeps the output in the valid index range, spreads values evenly. 
> Simple modulo operation, efficient. 
> No security, still possible collisions since many different inputs can collapse into the same slot after % size. 
> 
> 
6. Write pseudocode of how you would store Players in PlayerLists in a hash map.


     CLASS PlayerHashMap:
      INITIALIZE with table size(default=10):
     create an array of slots 
     each slot contains an empty PlayerList 
     set count of players to 0
     
     FUNCTION hash_function(key): 
      if key is a Player, use key.uid 
     otherwise use key string 
     apply chosen hash function produce index
            - return index within table size

    FUNCTION get_index(key):
        - if key is a Player → extract uid and hash
        - if key is not string or Player → raise error
        - return index

    FUNCTION insert_or_update(key, name):
        1. Compute index using get_index(key)
        2. Search PlayerList at that index:
            - If player already exists → update name
            - Else → create new Player, insert into list
        3. Increment count if new player was added

    FUNCTION retrieve(key):
        1. Compute index using get_index(key)
        2. Search PlayerList at that index:
            - If found → return Player object
            - Else → raise error (KeyError)

    FUNCTION delete(key):
        1. Compute index using get_index(key)
        2. Attempt to remove node from PlayerList at that index
        3. If successful → decrement count
        4. Else → raise error (KeyError)

    FUNCTION size():
        - return current count of players

    FUNCTION display():
        for each index in table:
            - if PlayerList is not empty:
                - print index and chain of players
        - if all lists are empty → print "HashMap is empty"


## Reflection

1. What was the most challenging aspect of this task?

> The most challenging part of creating the hash map was figuring out how to store each player object in its own slot within the table, instead of putting all players into a single PlayerList.
> It was also difficult to work out how to calculate the correct index for each player. 

2. If you didn't have to use a PlayerList, how would you have changed them implementation of the hash map and why?

> If I didn't use a PlayerList for handling collisions in the hash map, I would have switched to using an open addressing technique instead of separate chaining.
> In this method the hash map is just a simple array, and each slot holds at most one (key, Player) pair. If two players land on the same slot, instead of chaining them together,
> the hash map looks for the next available slot using a rule or set of instructions like moving forward one step at a time, jumping by squares, using another hash etc. 
> This will keep everything stored in one continuous block of memory, which makes it faster to access. Although inserting might be smooth, deleting items maybe trickier because 
> the table needs to be resized when it gets too full or too empty. 

## Reference
This method is called [open addressing][1].

[1]: https://en.wikipedia.org/wiki/Open_addressing

This method is called [open addressing collision handling techniques][2].

[2]: https://www.geeksforgeeks.org/dsa/open-addressing-collision-handling-technique-in-hashing/

Type of Hash  [hash functions and list types][3]

[3]: https://www.geeksforgeeks.org/dsa/hash-functions-and-list-types-of-hash-functions/

Comparing hashing algorithms [pearson hashing][4]

[4]: https://mojoauth.com/compare-hashing-algorithms/sha-256-vs-pearson-hashing

Hash map in python [hash map in python][5]

[5]: https://www.geeksforgeeks.org/python/hash-map-in-python/

Understanding consistent hashing[Robust approach to data distribution][6]


[6]: https://medium.com/@anil.goyal0057/understanding-consistent-hashing-a-robust-approach-to-data-distribution-in-distributed-systems-0e4a0e770897

Hash-functions and list types of hash functions [types of hash function] [7]

[7]: https://www.geeksforgeeks.org/dsa/hash-functions-and-list-types-of-hash-functions/  

### Book References 
1. Bhargava, Aditya Y. Grokking Algorithms : An Illustrated Guide for Programmers and Other Curious People. Shelter Island, Ny, Manning Publications Co, 2016.
2. Marcello La Rocca. Grokking Data Structures. Simon and Schuster, 6 Aug. 2024.

### Key Dimensions of Hash Functions

1. **Uniformity**: the probability of any given hash value within the range of possible hash values should be approximately equal.

2. **Determinism**: a given input will always produce the same output.

3. **Efficiency**: the time complexity of computing the hash value should be constant, the hash function should be fast to compute, and utilize the architecture of the computer effectively

4. **Collision Resistance:** minimize the probability of collisions, through a variety of mechanisms.

5. **Sensitivity to input changes:** small changes in the input should produce large changes in the output.

6. **Security**
   - It should be computationally infeasible to find an input key that produces a specific hash value (non-reversibility)
   - The output hash values should appear random and unpredictable.
