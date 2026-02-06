# HashMap

A HashMap (also known as a Hash Table) is a data structure that implements an associative array abstract data type, a structure that can map keys to values. It uses a hash function to compute an index into an array of buckets or slots, from which the desired value can be found.

## How HashMap Works

HashMaps store data in key-value pairs. When you insert a key-value pair, the HashMap applies a hash function to the key to determine the index where the value should be stored. This allows for fast retrieval of values based on their keys.

### Hash Function

The hash function takes a key and returns an integer that represents the index in the underlying array where the key-value pair should be stored. A good hash function distributes keys uniformly across the array to minimize collisions.

### Collision Resolution

Collisions occur when two different keys hash to the same index. This implementation uses **chaining** to resolve collisions. Each bucket in the array contains a list of key-value pairs that hash to the same index. When a collision occurs, the new key-value pair is added to the list in that bucket.

### Load Factor and Capacity

- **Capacity**: The number of buckets in the HashMap
- **Size**: The number of key-value pairs currently stored
- **Load Factor**: The ratio of size to capacity (size/capacity)

The load factor indicates how full the HashMap is. A higher load factor means more collisions and slower performance. In this implementation, the capacity is fixed, but in more advanced implementations, the HashMap would resize when the load factor exceeds a threshold.

## Implementation Details

This HashMap implementation uses chaining to handle collisions. Each bucket contains a list of key-value pairs that hash to the same index.

### Features

- Dynamic key-value storage
- Collision resolution through chaining
- Average O(1) time complexity for basic operations
- Support for common dictionary-like operations
- Flexible key types (any hashable object)

### Time Complexity

| Operation | Average Case | Worst Case |
|-----------|--------------|------------|
| Access    | N/A          | N/A        |
| Search    | O(1)         | O(n)       |
| Insertion | O(1)         | O(n)       |
| Deletion  | O(1)         | O(n)       |

The worst-case time complexity occurs when all keys hash to the same bucket, creating a single long chain. This is why choosing a good hash function is important.

## Methods

### `__init__(capacity)`
Initializes a new HashMap with the specified capacity.

#### Parameters
- `capacity` (int): The initial capacity of the HashMap (number of buckets)

#### Details
- Creates an empty HashMap with the specified number of buckets
- Each bucket is initialized as an empty list to handle collisions
- The size counter is initialized to 0

### `__len__()`
Returns the number of key-value pairs in the HashMap.

#### Returns
- `int`: The total number of key-value pairs currently stored in the HashMap

#### Details
- This operation runs in O(1) constant time
- The size is maintained internally and incremented/decremented during put/remove operations

### `__contains__(key)`
Checks if a key exists in the HashMap.

#### Parameters
- `key`: The key to check for existence

#### Returns
- `bool`: True if the key exists in the HashMap, False otherwise

#### Details
- Uses the hash function to find the correct bucket
- Searches through the bucket's list to find the key
- Average time complexity: O(1), Worst case: O(n)

### `put(key, value)`
Inserts or updates a key-value pair in the HashMap.

#### Parameters
- `key`: The key to insert or update (can be any hashable type)
- `value`: The value associated with the key

#### Details
- If the key already exists, updates the value
- If the key doesn't exist, adds a new key-value pair
- Increments the size counter when adding a new key
- Average time complexity: O(1), Worst case: O(n)

### `get(key)`
Retrieves the value associated with a given key.

#### Parameters
- `key`: The key whose value to retrieve

#### Returns
- The value associated with the key

#### Raises
- `KeyError`: If the key is not found in the HashMap

#### Details
- Uses the hash function to find the correct bucket
- Searches through the bucket's list to find the key
- Average time complexity: O(1), Worst case: O(n)

### `remove(key)`
Removes a key-value pair from the HashMap.

#### Parameters
- `key`: The key to remove

#### Raises
- `KeyError`: If the key is not found in the HashMap

#### Details
- Finds the key in the appropriate bucket
- Removes the key-value pair from the bucket's list
- Decrements the size counter
- Average time complexity: O(1), Worst case: O(n)

### `keys()`
Returns a list of all keys in the HashMap.

#### Returns
- `list`: A list containing all keys in the HashMap

#### Details
- Iterates through all buckets and collects all keys
- Time complexity: O(n), where n is the total number of key-value pairs

### `values()`
Returns a list of all values in the HashMap.

#### Returns
- `list`: A list containing all values in the HashMap

#### Details
- Iterates through all buckets and collects all values
- Time complexity: O(n), where n is the total number of key-value pairs

### `items()`
Returns a list of all key-value pairs in the HashMap.

#### Returns
- `list`: A list of tuples containing all key-value pairs in the HashMap

#### Details
- Iterates through all buckets and collects all (key, value) tuples
- Time complexity: O(n), where n is the total number of key-value pairs

## Internal Details

### `_hash_function(key)`
Computes the hash value for a given key using a simple polynomial rolling hash function.

#### Parameters
- `key`: The key to hash (will be converted to string)

#### Returns
- `int`: The computed hash value modulo the capacity

#### Algorithm
1. Converts the key to a string representation
2. Applies a polynomial rolling hash algorithm using 31 as the multiplier
3. Returns the hash value modulo the capacity to fit within the array bounds

The polynomial rolling hash formula: `hash = (hash * 31 + ord(char)) % capacity`

## Example Usage

```python
from HashMap import HashMap

# Create a new HashMap with capacity 10
hashmap = HashMap(10)

# Add key-value pairs
hashmap.put("apple", 1)
hashmap.put("banana", 2)
hashmap.put("orange", 3)
hashmap.put("strawberry", 4)

# Retrieve values
print(hashmap.get("apple"))      # Output: 1
print(hashmap.get("banana"))     # Output: 2

# Check if a key exists
print("apple" in hashmap)        # Output: True

# Get all keys, values, and items
print(hashmap.keys())            # Output: ['apple', 'banana', 'orange', 'strawberry']
print(hashmap.values())          # Output: [1, 2, 3, 4]
print(hashmap.items())           # Output: [('apple', 1), ('banana', 2), ('orange', 3), ('strawberry', 4)]

# Remove a key-value pair
hashmap.remove("banana")
print("banana" in hashmap)       # Output: False

# Get the size of the HashMap
print(len(hashmap))              # Output: 3

# Demonstrate collision handling
hashmap.put(1, "one")            # These keys might hash to the same bucket
hashmap.put(11, "eleven")        # depending on the hash function
hashmap.put(21, "twenty-one")    # All three keys will be in the same bucket
```

## Advantages and Limitations

### Advantages
- Fast average-case lookup, insertion, and deletion (O(1))
- Flexible key types (any hashable object)
- Simple to implement and understand

### Limitations
- Worst-case performance is O(n) when many keys hash to the same bucket
- Memory overhead due to the array structure and potential empty buckets
- Fixed capacity (in this implementation) - no automatic resizing
- Performance depends heavily on the quality of the hash function

## Common Use Cases

- Caching and memoization
- Database indexing
- Implementing sets and dictionaries
- Counting occurrences of elements
- Fast lookups in algorithms