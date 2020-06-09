## Django 의 MVC 패턴 

<br>

MVC  패턴이란, Model, View, Controller 로 이루어진 구조를 의미. 

<br>웹 프로그래밍만을 위한 내용이 아닌, 소프트웨어 개발 방법 methodology 이다. 

특정 소프트웨어를 아래 3 단계로 나누어서 개발한다는 방법이다. 

<br>

- Model 
- View
- Controller 

<br>

많은 웹사이트와 웹 프레임워크들이 MVC패턴을 기반으로 만들어져 있고, 웹 프로그래밍 개발자들에게는 친숙한 개발 패턴이다. 

<br>

각, Model, View, 그리고 Controller 부분들이 의미하는바는 아래와 같이 요약할수 있다. 

<br>

- Model - 웹에서 백앤드에 존재하는 데이터베이스를 의미, 알고리즘이나 쿼리 등도 의미하지만, 어떤것을 이루는 데이터라고 보는것이 편함 
- View - 사용자에게 보여지는 것, 웹에서는 당연히 화면을 이야기 할것이고, HTML 파일을 사용자에게 보여주었다면, 화면에 나타나는 겨로가물이 View 가 될것이다. 
- Controller - Model 과 View 를 제어하는 역할을 하는데. 사용자가 view 를 통해 controller 에 요청을 보내면, Controller 는 특정한 프로세스를 처리한다. 예를들면, model 에서 데이터를 가져오거나, 처리된 결과를 View  로 다시 보내어, 사용자에게 표시하는것. 





<br>실제 Django 에서는, MVC 패턴이 이루어 지는데. 

<br>

| 파일      | 패턴       |
| --------- | ---------- |
| models.py | Model      |
| views.py  | Controller |
| templates | View       |

<br>

<br>

## Model 에 대한 정리 

<br>

데이터베이스는, 데이터가 저장되는 테이블로, models.py 파일에서 정의가 된다. 

<br>데이터는 특정 테이블에 저장되고, 테이블을 만들 때 설정한 데이터의 형태를 따르고. 데이터베이스는 이렇게 특정 테이블들의 집합으로 이루어진다. 

<br>

데이터베이스에 저장된 테이블에 있는 데이터들을 저장하거나, 필요한 데이터를 꺼내어 사용하는데. 

<br>

<br>

Django 에서 데이터를 사용하기위해 설정해야 할것은 크게 2가지이다. 

<br>

1. 어떤 데이터베이스를 사용할것인지 설정해 준다.<br>예) SQLite, Oracle, PostgreSQL 등등 
2. 테이블에 대한 형태를 정의해 준다 <br>



<br>

하나의 모델은, 하나의 클래스로 되어 있으며, models.py  파일에 데이터에 대한 정보를 정의해 주었으면, 

<br>Django 서버에 실제로 적용을 해주어야 한다. models.py 에 작성된 모델을 바탕으로 동일한 테이블을 데이터베이스에 만들어 주기 위해서, python manage.py makemigrations 커맨드를 사용한다. 

<br>

makemigrations 명령어를 입력하면, migrations 이란것을 만들어서, 데이터베이스에 대한 초안을 만들어 낸다. 이때 생성되는 파일이 0001_initial.py 같은 파일이다. 

<br>

이 생성된 migrations 를 진짜로 데이터베이스 테이블로 만들어 내려면, 아래 명령어를 실행 해 주어야 한다. 

<br>

python manage.py migrate 

<br>

위 명령어를 사용하면, 데이터베이스가 생성이 되는데. 

<br>제대로 만들어졌는지 확인하기 위해서, dbshell 에 접근해 볼수 있다. 

<br>

<br>

```shell
python manage.py dbshell
```

<br>* 해당 Db 프로그램이 경로에 깔려 있어야 작동한다. 

<br>

## Views 에 대한 정리 

<br>

views.py 파일은, 들어온 요청을 내부적으로 어떻게 처리할지에 대한 함수와 클래스가 존재한다. 

<br>URL 을 통하여 요청이 들어오면, views.py 파일에 존재하는 적절한 함수나 클래스를 호출하여 작업을 수행한후에. 결과물을 templates 에 돌려준다. 

<br>



<br>

## Templates 에 대한 정리 

<br>

Django 에서 templates 는, views 가 처리한 내용을 전달받아 표시하는 파일이다. 

<br>보통은, html 파일로 되어 있어서. 웹에 표시가 된다. 

<br>



