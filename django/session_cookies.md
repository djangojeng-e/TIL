# Session and Cookies 



In order to implement a login system in Django, Understanding about session and cookies might be critical. 



Now, session and cookies are different. Let's look at the definitions for each of them and look at the difference between them as well. 





# Session 



A session creates **a file in a temporary directory on the server** where registered session variables and their values are stored. This data will be available to all pages on the site during the visit. 



A session ends when the user closes the browser or after leaving the site, the server will terminate the session after a predetermined period of time, normally 30 minutes duration. 





# Cookies 



Cookies are **text files stored on the client computer** and they are kept of use tracking purpose. Server script sends a set of cookies to the browser. E.g. name, age, or identification number etc. The browser stores this information on a local machine for future use. 



When next time browser sends any request to web server then it sends those cookies information to the server and server uses that information to identify the user. 



