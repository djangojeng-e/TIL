# Model Field Reference 





## null



Field.null 



If **True**, Django will store empty values as NULL in the database. **Default is False**



**Avoid using null on string-based fields**



### CharField and TextField 



Django convention is to use the empty string, not NULL. 







## blank 



**Field.blank**



If **True**, the field is allowed to be blank. **Default is False.** 



**N.B**	Difference between null and blank. null is purely database-related, whereas blank is validation-related. If True, form validation will allow entry of empty value. If False, the field will be required. 





## choices



**Field.choices**



A sequence consisting itself of iterables of exactly two items (e.g. (A, B), (A,B)) to use as choices for this field. 



#  