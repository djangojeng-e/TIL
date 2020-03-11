When you exit Python, is all memory deallocated?



<br>

Exiting Python deallocates everything except the followings 



- Modules with circular references 
- Objects referenced from global namespaces 
- Parts of memory reserved by the C library.