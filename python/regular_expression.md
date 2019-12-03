# Regular Expression



A regular expression is a sequence of characters that define a search pattern. Is a sequence of characters that forms a search pattern. 



It can be used to check if a string contains the specified search pattern. 





# Regular Expression Module



Python has a built-in package called re, this can be used to work with Regular Expressions. 



```python
import re 
```



After re module is imported, you can start using regular expressions: 



# Regular Expression Functions 





- **re.findall** - returns a list containing all matches 
- **re.search** - returns a Match object if there is a match anywhere in the string 
- **re.split** - returns a list where the string has been split at each match 
- **re.sub** - Replaces one or many matches with a string. 



| Character | Description                                 | example  |                                                              |
| --------- | ------------------------------------------- | -------- | ------------------------------------------------------------ |
| []        | A set of characters                         | "[a-m]"  | Identifies lower case charceter between "a" and "m"          |
| .         | Any character                               | "he...o" | Search for a sequence that starts with "he" and three any characters and "o" |
| ^         | Starts with                                 | "^hello" | Check if the string starts with hello                        |
| $         | Ends with                                   | "world$" | Check if the string ends with 'world'                        |
| *         | zero or more occurrences                    | "aix*"   | Check if the string contains "ai" followed by 0 or more "x" characters: |
| +         | one or more occurrences                     | "aix+"   | Check if the string contains "ai" followed by 1 or more "x" characters: |
| {}        | Exactly the specified number of occurrences | "al{2}"  | Check if the string contains "a" followed by exactly two "l" characters |
| ()        | Capture and group                           |          |                                                              |



**Special Squences**

| Character | Description                                                  | example                |      |
| --------- | ------------------------------------------------------------ | ---------------------- | ---- |
| \A        | Returns a match if  the specified characters are at the beginning of the string | "\AThe"                |      |
| \b        | Returns a match where the specified characters are at the beginning or at the end of word. | r"\bain"<br />r"ain\b" |      |
| \B        | Returns a match where the specified characters are present, but **NOT at the beginning (or at the end) of a word** | r"\Bain"<br />r"ain\B  |      |
| \d        | Returns a match where the string contains digits (numbers from 0 - 9) | "\d"                   |      |
| \D        | Returns a match where the string DOES NOT contain digits     | "\D"                   |      |
| \s        | Returns a match where the string contains a white space character | "\s"                   |      |
| \S        | Returns a match where the string DOES NOT contain a white space character | "\S"                   |      |
|           |                                                              |                        |      |







