What is the MRO in Python?

MRO stands for Method Resolution Order. Talking of multiple inheritances, 
whenever we search for an attribute in a class, 

Python first searches in the current class. If found, its search is satisfied. If not, it moves to the parent class. 

It follows an approach that is left-to-right and depth-first. It goes Child, Mother, Father, Object. 

We can call this order a linerarization of the class Child; the set of rules applied are the Method Resolution Order (MRO). 

We can borrow the __mro__ attribute or the mro() method to get this. 


