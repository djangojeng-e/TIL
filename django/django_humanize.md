# Humanize 



A set of Django Template filters are used for adding a "human touch" to data.



It enables to convert data into more familiar form to human. 

To activate these filters, add 



```python
# settings.py 
# Add 'django.contrib.humanize' in INSTALLED_APPS

INSTALLED_APPS = [ 
	'django.contrib.humanize',
]

```



At the top lines, insert {% load humanize %} 



```html
{% load humanize %} 
```





## apnumber



For numbers 1-9, returns the number spelled out. 



e.g



- 1 becomes **one**
- 2 becomes **two**
- 10 becomes 10. 



You can pass in either an integer or a string representation of an integer. 





## intcomma



Converts an integer or float (or a string representation of either) to a string containing commas every three digits. 



Examples 



- 4500 -> 4,500
- 4500.2 -> 4,500.2
- 45000 -> 45,000
- 4500000 -> 4,500,000





## intword 



Converts a large integer (or a string representation of an integer) to a friendly text representation. 



Examples:



- 1000000 becomes 1.0 **million.** 
- 1200000 becomes 1.2 **million.**
- 1200000000 becomes 1.2 **billion**





## naturalday 



For dates that are the current day or within one day, return 'today' 'tomorrow' or 'yesterday'

Otherwise, format the date using the passed in format string. 



Examples 

Today's date 2 Feb 2019 

- 2 Feb 2019 becomes Today 
- 1 Feb 2019 becomes yesterday 
- 3 Feb 2019 becomes tomorrow 



## naturaltime 



For datetime values, returns a string representing how many seconds, minutes or hours ago it was - falling back to the timesince format if the value is more than a day old. In case the datetime value is in the future the return value will automatically use an appropriate phrase 





Examples (when ‘now’ is 17 Feb 2007 16:30:00):

- `17 Feb 2007 16:30:00` becomes `now`.
- `17 Feb 2007 16:29:31` becomes `29 seconds ago`.
- `17 Feb 2007 16:29:00` becomes `a minute ago`.
- `17 Feb 2007 16:25:35` becomes `4 minutes ago`.
- `17 Feb 2007 15:30:29` becomes `59 minutes ago`.
- `17 Feb 2007 15:30:01` becomes `59 minutes ago`.
- `17 Feb 2007 15:30:00` becomes `an hour ago`.
- `17 Feb 2007 13:31:29` becomes `2 hours ago`.
- `16 Feb 2007 13:31:29` becomes `1 day, 2 hours ago`.
- `16 Feb 2007 13:30:01` becomes `1 day, 2 hours ago`.
- `16 Feb 2007 13:30:00` becomes `1 day, 3 hours ago`.
- `17 Feb 2007 16:30:30` becomes `30 seconds from now`.
- `17 Feb 2007 16:30:29` becomes `29 seconds from now`.
- `17 Feb 2007 16:31:00` becomes `a minute from now`.
- `17 Feb 2007 16:34:35` becomes `4 minutes from now`.
- `17 Feb 2007 17:30:29` becomes `an hour from now`.
- `17 Feb 2007 18:31:29` becomes `2 hours from now`.
- `18 Feb 2007 16:31:29` becomes `1 day from now`.
- `26 Feb 2007 18:31:29` becomes `1 week, 2 days from now`.





## ordinal 



Converts an integer to its ordinal as a string 



Examples: 



1 becomes 1st. 

2 becomes 2nd. 

3 becomes 3rd. 



You can pass in either an integer or a string representation of an integer. 



# Example 



```html
{% extends 'base.html' %}
{% load humanize %} 

{% block content %} 


<ul>
    <li> Price : {{ product.price|intcomma }}</li>
    <li> Registered Time : {{ registered_time|naturaltime }} </li>
    <li> Registered Day : {{ registered_day|naturalday }}</li>
    
</ul>



{% endblock %} 
```





