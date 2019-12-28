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



#  NAMED TUPLE



Choices can be collected into named groups that can be used for organisational purposes.



```python
MEDIA_CHOICES = [
    ('Audio', (
    		('vinyl','Vinyl'),
    		('cd', 'DVD'),
    )
    ),
    ('unknown', 'Unknown'),
]
```





The first element in each tuple is the name to apply to the group. **The second element is an iterable of 2-tuples with each 2-tuple containing a value and human-readable name for an option.** 





# db_column 



Field.db_column 



The name of the database column to use for this field. If this isn't given, Django will use the field's name 





# db_index 



Field.db_index 



If True, a databse index will be created for this field. 







# db_tablesapce 



**Field.db_tablespace**



The name of the database tablespace to use for this field's index. If this field is indexed. The default is the project's Default_index_tablespace setting. If set, or the db_tablespace of the model. 



