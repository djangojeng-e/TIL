EC2 - Container(80:8000) -> (screen)runserver:8000 - Django 


EC2 - Container(80:8000) -> Gunicorn:8000 -> Django 
EC2 - Container(80:80) -> Nginx:80 -> Gunicorn:UnixSocket -> Django 


Nginx(Webserver)
	외부에서 오는 요청을 어딘가로 전달 
	정적 컨텐츠 서빙 


Gunicorn(WSGI) 
	웹 서버로 전달된 요청을 파이썬 어플리케이션에게 적절히 번역해서 전달 
	-> 파이썬 애플리케이션의 응답을 적절히 웹 서버에게 번역해서 전달 

Django(Web application) 
	외부에서 오는 요청에 대한 동적 응답을 생성. 



