## Memory view in python
* Python memoryview() function returns the memory views objects. Before learning more about memoryview() function let’s see why do we use this function.

### Why do we use memoryview() function? 
* As Memory view is a safe way to expose the buffer protocol in Python and a memoryview behaves just like bytes in many useful contexts (for example, it supports the mapping protocol) so it provides an adequate replacement if used carefully. The great thing about it is that it uses the buffer protocol beneath the covers to avoid copies and just juggle pointers to data. So before we get into what memory views, we need to first understand Buffer Protocol.

### Buffer Protocol
* Buffer protocol provides a way to access the internal data of an object. This internal data is a memory array or a buffer. It allows one object to expose its internal data (buffers) and the other to access those buffers without intermediate copying. Buffer protocol is only accessible to us at the C-API level and not using our normal codebase. So, to expose the same protocol to a normal Python codebase, memory views are present.

### Memory view
* **Memoryview objects allow Python code to access the internal data of an object that supports the buffer protocol without copying.** The memoryview() function allows direct read and write access to an object’s byte-oriented data without needing to copy it first. That can yield large performance gains when operating on large objects since it doesn’t create a copy when slicing.
* Example 01 : 
```bash
"""
Syntax: memoryview(obj)

Parameters:
* obj – object whose internal data is to be exposed.
* supporting buffer protocol – str and bytearray (but not unicode).

Return Value: Returns a memoryview object. 
"""


byte_array = bytearray('XYZ', 'utf-8')
 
mv = memoryview(byte_array)
 
print(mv[0])
print(bytes(mv[0:1]))
```

* Modify internal data using memoryview
```bash
# Python program to illustrate
# Modifying internal data using memory view
 
# random bytearray
byte_array = bytearray('XYZ', 'utf-8')
print('Before update:', byte_array)
 
mem_view = memoryview(byte_array)
 
# update 2nd index of mem_view to J
mem_view[2] = 74
print('After update:', byte_array) 

"""
Explanation how we modify internal data in above program : Here, we updated the memory view’s 2nd index to ASCII value as 74 (J).
In this memoryview object mem_view references the same buffer or memory and updating the index in mem_view and it also updates 
byte_array.
"""
```

* Example 3: Python memoryview() to bytes:
```bash

# Python program to illustrate memory view
 
# random bytearray
byte_array = bytearray('XYZ', 'utf-8')
 
mem_view = memoryview(byte_array)
print(type(mem_view))
 
byt = bytes(mem_view)
print(type(byt))
```

* Example 4 : python memoryview() to string
```bash
# Python program to illustrate memory view
 
# random bytearray
byte_array = bytearray('XYZ', 'utf-8')
 
mem_view = memoryview(byte_array)
print(type(mem_view))
 
string = str(mem_view)
print(type(string)) 
```

### Importance of buffer protocol and memory views
* By using buffer protocol we can work on large data like we want to work on binary data of an image. Buffer protocol, can create another object access to modify the large data without copying it. This makes the program use less memory and increases the execution speed.

### Important resources
* [Python memory view](https://www.geeksforgeeks.org/memoryview-in-python/)
* [Python memory-view - the conceptual](https://www.youtube.com/watch?v=Put8bdi-PUg)