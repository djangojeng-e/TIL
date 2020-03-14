Q.17. Explain garbage collection with Python.

- Python maintains a count of how many references there are to each object in mememory. 
- When a reference count drops to zero, it means the object is dead and python can free the memory it allocated to that object. 
- The garbage collector looks for reference cycles and cleans them up 
- Python uses heuristics to speed up garbage collection. 
- Recently created objects might as well be dead 
- The garbage collector assigns generations to each object as it is created 
- It deals with the younger generations first. 
