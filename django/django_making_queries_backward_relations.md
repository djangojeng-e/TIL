# Time to practice backward relations in model 



Consider the following relationship. 



```python

class Group(models.Model):
    name = models.CharField(max_length=100)
    
class Student(models.Model):
    name = models.CharField(max_length=100)
    group = models.ForeignKey(Group)
    
   
```



A group can have many students 



## Testing Queries 





```python

group1 = Group.objects.create(name='Group 1')
group2 = Group.objects.create(name='Group 2')
Studnet.objects.create(name='stud1', group=group1)
Student.objects.create(name='stud2', group=group1)
Student.objects.create(name='stud3', group=group1)
Student.objects.create(name='stud1', group=group2)

```





